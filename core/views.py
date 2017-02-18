from django.shortcuts import render, redirect

# Create your views here.
from user.admin import UserCreationForm


def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home/')
        else:
            form = UserCreationForm()
            args = {'form': form}
            return render(request, 'registration/reg_form.html', args)
