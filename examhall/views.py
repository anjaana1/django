from django.shortcuts import render, redirect
from .forms import *
from django.db.models import Q
from django.contrib import messages


"""
View methods for Exam Hall
"""

def check_session(req):
    if req.session.has_key('examhall'):
        return True
    else:
        return False

def signup(req):
    form = CenterForm(req.POST or None)
    if req.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(login)
    data = {
        'form': form
    }
    return render(req, 'signup.html', data)


def login(req):
    if (check_session(req)==True):
        return redirect(index)
    else:
        form = LoginForm(req.POST or None)
        if req.method == "POST":
            if form.is_valid():
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                cond = Q(email = email) and Q(password = password)
                check = Center.objects.get(cond)
                if check:
                    req.session['examhall'] = email
                    return redirect(index)
                else:
                    return redirect(login)
        data = {
            'form': form
        }
        return render(req, 'login.html',data)


def index(req):
    if check_session(req)==False:
        return redirect(login)
    else:
        return render(req, 'examhall/dashboard.html')


def manage_block(req):
    if check_session(req)==False:
        return redirect(login)
    else:
        form = BlockForm(req.POST or None)
        if req.method == "POST":
            if form.is_valid():
                form.save()
                return redirect(manage_block)
            else:
                return redirect(manage_block)
        data = {
            'form':form,
            'blocks':Block.objects.all()
        }
        return render(req, 'examhall/block.html',data)


def manage_room(req):
    if check_session(req)==False:
        return redirect(login)
    else:
        form = RoomForm(req.POST or None)
        if req.method == "POST":
            if form.is_valid():
                form.save()
                return redirect(manage_room)
            else:
                return redirect(manage_room)
        data = {
            'form':form,
            'rooms':Room.objects.all()
        }
        return render(req, 'examhall/room.html',data)


def manage_course(req):
    if check_session(req)==False:
        return redirect(login)
    else:
        form = CourseForm(req.POST or None)
        if req.method == "POST":
            if form.is_valid():
                form.save()
                return redirect(manage_course)
            else:
                return redirect(manage_course)
        data = {
            'form':form,
            'course':Course.objects.all()
        }
        return render(req, 'examhall/course.html',data)


def manage_department(req):
    if check_session(req)==False:
        return redirect(login)
    else:
        form = DepartmentForm(req.POST or None)
        if req.method == "POST":
            if form.is_valid():
                form.save()
                return redirect(manage_department)
            else:
                return redirect(manage_department)
        data = {
            'form':form,
            'department':Department.objects.all()
        }
        return render(req, 'examhall/department.html',data)


def manage_student(req):
    if check_session(req)==False:
        return redirect(login)
    else:
        form = StudentForm(req.POST or None)
        if req.method == "POST":
            if form.is_valid():
                form.save()
                return redirect(manage_student)
            else:
                return redirect(manage_student)
        data = {
            'form':form,
            'student':Student.objects.all()
        }
        return render(req, 'examhall/student.html',data)


def manage_teacher(req):
    if check_session(req)==False:
        return redirect(login)
    else:
        form = TeacherForm(req.POST or None)
        if req.method == "POST":
            if form.is_valid():
                form.save()
                return redirect(manage_teacher)
            else:
                return redirect(manage_teacher)
        data = {
            'form':form,
            'teacher':Teacher.objects.all()
        }
        return render(req, 'examhall/teacher.html',data)



def logout(req):
    del req.session['examhall']
    return redirect(login)
