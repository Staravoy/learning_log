from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as auth_logout


def register(request):
    # Реєстрація нового користувача
    if request.method != 'POST':
        # Показати порожню форму реєстрації
        form = UserCreationForm()
    else:
        # Опрацювати заповнену форму
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Авторизувати користувача та скерувати його на головну сторінку
            login(request, new_user)
            return redirect('learning_logs:index')
    # Показати порожню або не дійсну форму
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def logout(request):
    # Вихід з облікового запису
    logout(request)
    return redirect(request, 'registration/logged_out.html')
