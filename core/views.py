from django.shortcuts import render, redirect
from core.froms import ContactForm
from user.admin import UserCreationForm
from django.contrib import messages


def home(request):
    return render(request, "home.html")


def quemsomos(request):
    return render(request, "quemsomos.html")


def home(request):
    return render(request, "home.html")


def register(request):
    success = False
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    elif request.method == 'POST':
        messages.error(request, 'Formulário inválido')
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'registration/reg_form.html', context)


def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    elif request.method == 'POST':
        messages.error(request, 'Formulário inválido')
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)
