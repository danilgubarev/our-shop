from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import login, logout, authenticate
from django.db.utils import IntegrityError
# from main_page.views import main_page
# Create your views here.


def register(request):
    context = {}
    if request.method == 'POST':
        login = request.POST.get("login")
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        context["login"] = login
        context["username"] = username
        context["password"] = password
        context["confirm_password"] = confirm_password
        
        if login and username and password and confirm_password:
            if len(password) >= 8:
                if password == confirm_password:
                    try:
                        User.objects.create_user(
                            username=login, 
                            password=password,
                            first_name=username, 
        
                        )
                        return redirect('authorization')
                    except IntegrityError:
                        context['error'] = 'Такий користувач вже існує'
                else:
                    context['error'] = 'Паролі не співпадають'
            else:
                context['error'] = 'Кількість символів має бути довшою або дорівнювати 8'
        else:
            context['error'] = 'Заповніть всі поля'

    return render(request, 'registration/registration.html', context)



# создаем функцию для отображения страницы логина 
def view_login(request):
    # Если тип запроса - POST
    if request.method == "POST":
        # Получаем из POST запроса данные которые пользователь ввел в форму и отправил на сервер
        username = request.POST.get("username")
        password = request.POST.get("password")
        # Возвращает None, если такого пользователя нет. Если он есть - возвращает запись юзера из БД
        user = authenticate(request, username=username, password=password)
        # Если пользователь существует то есть не является None 
        if user is not None:
            # создает токен сессии для успешно авторизовавшегося пользователя 
            login(request, user)
            # перенаправляет пользователя на страницу успешной авторизации
            return redirect("main")
        else:
            return render(request, "registration/login.html", context={"text_error" : "Вы ввели неправильный логин или пароль"})
            
    # независими от условий в блоке функции рендерим страницу авторизации 
    return render(request, 'registration/login.html' )



# создаем функцию для выхода из аккаунта 
def user_logout(request):
    # выполняем выход пользователя из аккаунта удаляя сессию
    logout(request)
    # после того как пользователь вышел с аккаунта перенаправляем на страницу логина
    return redirect("authorization")