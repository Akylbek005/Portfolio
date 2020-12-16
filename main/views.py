from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail
from .forms import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def index(request):
    main = ImageGallery.objects.all()
    return render(request, 'main/index.html', {'main': main})


def about(request):
    main = ImageGallery.objects.all()
    return render(request, 'main/about.html', {'main': main})


def contact(request):
    return render(request, 'main/contact.html')


def blog(request):
    return render(request, 'main/blog.html')


def email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = 'New message in portfolio'
            to_email = ['iakylbek005@gmail.com',]
            name = form.cleaned_data['name']
            mail = form.cleaned_data['mail']
            message = form.cleaned_data['message']
            msg = f'Имя: {name} \nПочта: {mail} \nСообщение:{message}'
            send_mail(subject, mail, message, to_email, fail_silently=False)
        return redirect('contact', msg)


@login_required
def dashboard(request):
    return render(request, 'main/index.html', {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'create/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'create/register.html', {'user_form': user_form})
