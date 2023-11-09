
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from rest_framework.views import APIView
from django.urls import path
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template



def email_welcome(email):
    subject = '¡Bienvenido a nuestro sitio!'
    from_email = 'no-reply@gmail.com'
    recipient_list = [email]
    template = get_template('email_template.html')
    context = {}
    content = template.render(context)
    email = EmailMessage(subject, content, from_email, recipient_list)
    email.content_subtype = "html"
    email.send(fail_silently=True)


class Login(APIView):
    template_name = 'login.html'

    def get(self, request):

        if request.user.is_authenticated:
            # El usuario ya está autenticado, redirigirlo a la página de inicio
            return redirect('home')

        return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if request.user.is_authenticated:
            # Si el usuario ya está autenticado, redirigirlo a la página de inicio
            return redirect('home')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('home')

        else:
            messages.error(request, 'Credenciales incorrectas. Por favor, inténtalo de nuevo.')

        return render(request, self.template_name)


class Logout(APIView):

    def get(self, request):
        # Log the user out and redirect to a desired page (e.g., home)
        logout(request)
        return redirect('login')


class Home(APIView):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


class Register(APIView):
    template_name = 'register.html'

    def get(self, request):

        return render(request, self.template_name)

    @method_decorator(csrf_exempt)
    def post(self, request):

        try:

            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']

            if User.objects.filter(username=username).exists():
                return JsonResponse({'message': 'El usuario ya existe'}, status=400)

            else:
                User.objects.create_user(
                    username=username, last_name=last_name, password=password, email=email, first_name=first_name)
                email_welcome(email)
                context = {'message': 'Registro exitoso'}
                return JsonResponse({'message': 'Registro exitoso'}, status=200)

        except KeyError:
            return JsonResponse({'message': 'El nombre de usuario y la password son obligatorios'}, status=400)


class ForgotPassword(APIView):
    template_name = 'forgot-password.html'

    def get(self, request):
        return render(request, self.template_name)


class Charts(APIView):
    template_name = 'charts.html'

    def get(self, request):
        return render(request, self.template_name)


class Material(APIView):
    template_name = 'catalogo.html'

    def get(self, request):
        return render(request, self.template_name)

class RegisterLibros(APIView):
    template_name = 'register-libros.html'

    def get(self, request):
        return render(request, self.template_name)
class UserControl(APIView):
    template_name = 'control-users.html'

    def get(self, request):
        return render(request, self.template_name)


class Dashboard(APIView):
    template_name = 'encuesta_dash.html'

    def get(self, request):
        return render(request, self.template_name)