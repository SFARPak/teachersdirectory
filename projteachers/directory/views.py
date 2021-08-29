import csv, io
import string, random
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

# Create your views here.
from .models import Teacher
from . forms import TeacherModelForm, MyUserForm

def index(request):
    qs = Teacher.objects.all()
    context = {
        'title': 'Home',
            'teacher_list': qs,
        }
    return render(request,'directory/index.html', context )

@login_required
def teacher_profile(request, slug):
    teacher = get_object_or_404(Teacher, slug=slug)
    qs = Teacher.objects.all()
    context = {
        'teacher_list': qs,
        'teacher' : teacher,
        'description':'Adding New Teacher to Directory | Teacher Directory',
        'keywords': ['teacher', 'directory', 'django', 'python']
        }
    return render(request, 'directory/teacher-profile.html', context)

def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@login_required
def bulk_upload(request):
    prompt = {
        'order' : 'The order of CSV should be first_name, last_name, profile_picture, email, phone, room number, subjects.'
    }
    if request.method == "GET":
        return render(request, 'directory/bulk-upload.html', prompt)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not CSV file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Teacher.objects.update_or_create(
            first_name = column[0],
            last_name = column[1],
            image = '/static/images/teachers/'+column[2],
            email = column[3],
            phone = column[4],
            room_no = column[5],
            slug = column[0]+column[1],
            subject = column[6],
        )
    messages.success(request, 'Successfully Imported Bulk Data.')
    context = {}
    return render(request, 'directory/bulk-upload.html', context)

@login_required
def teacher_add(request):
    qs = Teacher.objects.all()
    form = TeacherModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        messages.success(request, 'Teacher Added.')
        form = TeacherModelForm()
    else:
        messages.error(request, '')
    context = {
        'form' : form,
        'teacher_list': qs,
        'title': 'Adding New Teacher to Directory',
        'description':'Adding New Teacher to Directory | Teacher Directory',
        'keywords': ['teacher', 'directory', 'django', 'python']
    }
    return render(request, 'directory/teacher-add.html', context)

@login_required
def teacher_update(request, slug):
    obj = get_object_or_404(Teacher, slug=slug)
    form = TeacherModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Blog Updated.')
    context = {
        "title": f"Update {obj.title}",
        'form' : form,
        'description':'Updating Teacher in Directory | Teacher Directory',
        'keywords': ['teacher', 'directory', 'django', 'python']
        }
    return render(request, 'directory/teacher-update.html', context)

@login_required
def teacher_delete(request, slug):
    obj = TeacherModelForm(Teacher, slug=slug)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Teacher Deleted.')
        return redirect('http://patriotsengineering.com/blog')
    context = {
        'object' : obj,
        'blog_title' : Teacher.title,
        'description':'Deleting Teacher from Directory | Teacher Directory',
        'keywords': ['teacher', 'directory', 'django', 'python']
    }
    return render(request, 'directory/teacher-delete.html', context)

def form(request):
    form = TeacherModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TeacherModelForm()
    
    context = {
                'title': 'Teachers input form',
                'form': form
        }

    return render(request,'directory/form.html', context )

def register_view(request):
    form = MyUserForm()
    if request.method=='POST':
        form = MyUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created.')
    context = {'form': form}
    return render(request,'directory/register.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request,'directory/login.html')