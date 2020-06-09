from django.shortcuts import render, HttpResponse, redirect
from .models import Result, Question, Test, Teacher
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
import json

# Create your views here.


def home(request):
    if request.user.is_anonymous:
        return redirect('/login/')
    else:
        current = Teacher.objects.filter(name=request.user.username)[0]
        tests = list(Test.objects.filter(author=current))
        if len(tests) == 0:
            tests = None
        context = {
            'name' : request.user.username,
            'tests': tests
        }

        return render(request, 'home.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        print(User.objects.all())
        users = authenticate(username=username, password=password)
        if users is not None:
            login(request, users)
            return redirect('/')
        else:
            messages.error(request, 'Invalid Username or Password')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/login/')

def start_test(request):
    global test_aval
    if request.method == 'GET' and (request.GET.get('username') is not None):
        # student_name = request.GET.get('username')
        name_test = request.GET.get('email')
        password = request.GET.get('password') 
        subject = request.GET.get('subject')
        class_name = request.GET.get('class')
        # section = request.GET.get('section')
        test_aval = list(Test.objects.filter(name=name_test, password=password, class_name=class_name, subject=subject))
        if len(test_aval) == 0:
            messages.error(request, 'Incorrect Details')
            return redirect('/start_test/')
        else:
            test_aval = test_aval[0]
            questions = list(Question.objects.filter(test=test_aval))
            for index, ques in enumerate(questions):
                ques.options = json.loads(ques.options)
                questions[index] = ques
            context = {
                'test': test_aval,
                'questions': questions,
            }
            return render(request, 'test.html', context)

    return render(request, 'st.html')


def make_test(request):
    if request.is_ajax():
        author = Teacher.objects.filter(name=request.user.username)
        total_questions = int(request.GET.get('totalQuestions'))
        name = request.GET.get('testInfo[name]')
        class_name = request.GET.get('testInfo[class]')
        subject = request.GET.get('testInfo[subject]')
        password = request.GET.get('testInfo[password]')
        questions = []
        questions_info =  []
        for i in range(total_questions):
            sended = dict(request.GET)
            correct_option = sended.get(f'questions[{i}][correct]')[0]
            options = sended.get(f'questions[{i}][options][]')
            ques_name = sended.get(f'questions[{i}][name]')[0]
            index_ques = sended.get(f'questions[{i}][index]')[0]
            this_question = {
                'name': ques_name,
                'correct': correct_option,
                'index': index_ques,
                'options': options
            }
            questions_info.append(this_question)
            questions.append(ques_name)
        
        new_test = Test.objects.create(name=name, no_questions=total_questions, questions= questions, subject=subject, author=author[0], class_name=class_name, password=password)

        new_test.save()

        for ques in questions_info:
            new_ques = Question.objects.create(text=ques['name'], answer=ques['correct'], options=json.dumps(ques['options']), index=ques['index'], test=new_test)

            new_ques.save()

        return JsonResponse({'isSuccess': True})
    return render(request, 'mt.html')


def test_info(request):
    global test_filter
    if request.is_ajax():
        name = request.GET.get('name')
        password = request.GET.get('password')
        test_filter = list(Test.objects.filter(name=name, password=password))[0]
        return JsonResponse({'isSuccess': True})
    
    try:
        results = list(Result.objects.filter(test=test_filter))
        a_results = list(Result.objects.filter(test=test_filter, student_section='A'))
        b_results = list(Result.objects.filter(test=test_filter, student_section='B'))
        c_results = list(Result.objects.filter(test=test_filter, student_section='C'))
        d_results = list(Result.objects.filter(test=test_filter, student_section='D'))

    except NameError as e:
        # Manually typing the url
        return redirect('/')
    if len(a_results) == 0:
        a_results = None
    if len(b_results) == 0:
        b_results = None 
    if len(c_results) == 0:
        c_results = None 
    if len(d_results) == 0:
        d_results = None  

    print(d_results)

    context = {
        'test': test_filter,
        'results': results,
        'Aresults': a_results,
        'Bresults': b_results,
        'Cresults': c_results,
        'Dresults': d_results
    }
    return render(request, 'ti.html', context)

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        teacher1 = Teacher.objects.create(name=username, password=password, email=email)
        teacher1.save()

        user1 = User.objects.create_user(username=username, password=password)
        user1.save()

        return redirect('/login/')

    return render(request, 'register.html')


def result_display(request):
    global all_context
    if request.is_ajax() and (request.GET.get('index[]') is not None):
        send_info = dict(request.GET)
        name = send_info.get('name')[0][:-1]
        section = send_info.get('section')[0][:-1]
        answers = send_info.get('index[]')
        for idx, ans in enumerate(answers):
            try:
                ans = int(ans)
                answers[idx] = ans
            except:
                answers[idx] = -1

        questions5 = list(Question.objects.filter(test=test_aval))

        for index, ques in enumerate(questions5):
                ques.options = json.loads(ques.options)
                questions5[index] = ques

        teacher_current = list(Teacher.objects.filter(name=request.user.username))[0]
        correct_answers = []
        for question in questions5:
            correct_answers.append(int(question.answer))
        full_marks = int(test_aval.no_questions)
        correct_anal = []
        marks_given = full_marks
        for correct, given in zip(correct_answers, answers):
            if correct != int(given) or given == -1:
                marks_given -= 1
                correct_anal.append(False)
            else:
                correct_anal.append(True)
        
        new_result = Result.objects.create(marks=int(marks_given), test=test_aval,student=name, student_class=test_aval.class_name, student_section=section, teacher=teacher_current, subject=test_aval.subject, full_marks=full_marks, given_answers = json.dumps(answers))

        new_result.save()

        all_context = {
            'success': True,
            'marks': marks_given,
            'analysis': correct_anal,
            'correct': correct_answers,
            'given': answers,
            'questions': questions5
        }

        return JsonResponse({
            'success': True
        })

    elif request.is_ajax() and (request.GET.get('is_teacher') is not None):
        name = request.GET.get('name')
        class_name = request.GET.get('class')
        section = request.GET.get('section')
        marks = request.GET.get('marks')
        test_name = request.GET.get('test_name')
        test_password = request.GET.get('test_password')

        current_teacher = list(Teacher.objects.filter(name=request.user.username))[0]

        test_fetched = list(Test.objects.filter(name=test_name, password=test_password, class_name=class_name, author=current_teacher))[0]

        questions_fetched = list(Question.objects.filter(test=test_fetched))

        for index, ques in enumerate(questions_fetched):
                ques.options = json.loads(ques.options)
                questions_fetched[index] = ques

        correct_answers2 = []
        for question in questions_fetched:
            correct_answers2.append(int(question.answer))

        result_fetched = list(Result.objects.filter(test=test_fetched, student=name, student_class=int(class_name), student_section=section, marks=marks, teacher=current_teacher))[0]

        given_anwers = json.loads(result_fetched.given_answers)
        correct_analysis = []
        for correct, given in zip(correct_answers2, given_anwers):
            if correct != int(given) or given == -1:
                correct_analysis.append(False)
            else:
                correct_analysis.append(True)

        all_context = {
            'success': True,
            'marks': marks,
            'analysis': correct_analysis,
            'correct': correct_answers2,
            'given': given_anwers,
            'questions': questions_fetched
        }

        return JsonResponse({'success': True})


    try:
        all_context = all_context
        print(all_context)
        return render(request, 'results.html', all_context) 
    except:
        return redirect('/')

