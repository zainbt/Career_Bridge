from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import RegisterForm
from django.views.generic import View
from django.contrib.auth.models import auth
from django.contrib import messages
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class BaseIndexView(View):
    templates_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.templates_name)


class LoginView(View):
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST['email']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                if user.user_type == 1:
                    return HttpResponseRedirect(reverse('university:dashboard'))
                elif user.user_type == 2:
                    return HttpResponseRedirect(reverse('company:dashboard'))
                else:
                    messages.info(request, 'The User You Enter are not found')
                    return redirect('accounts:login')
            else:
                messages.info(request, 'invalid credential')
                return redirect('accounts:login')
        else:
            return render(request, self.template_name,)


class RegisterView(View):
    template_name = 'accounts/signup.html'

    def get(self, request, *args, **kwargs):
        #GetMethod
        form = RegisterForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        #PostMethod
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            form = RegisterForm()
        context = {'form': form}
        return render(request, self.template_name, context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        # return HttpResponse('LogOut')
        return HttpResponseRedirect(reverse('accounts:index'))


class Contact(View):
    tamplate = 'accounts/contactUs.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.tamplate)


class AuthenticationView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': request.user,  # `django.contrib.auth.User` instance.

        }
        print('autherization details')
        return Response({"success":"Authorized"})

