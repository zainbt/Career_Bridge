from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from accounts.models import User
from .models import CreateProject
from .forms import ProjectCreationForm
from university.models import CreateBid
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import UsersSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


# Create your views here.


class DashBoardView(View):
    permission_classes = [IsAuthenticated]

    # login_required = True
    tamplate = 'company/dashboard.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        obj = User.objects.all()
        return render(request, self.tamplate, {'obj': obj})


class ProfileView(View):
    permission_classes = [IsAuthenticated]
    tamplate = 'company/compProfile.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, self.tamplate)


class Collaborations(View):
    permission_classes = [IsAuthenticated]

    tamplate = 'company/collaborations.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, self.tamplate)


class Projects(View):
    permission_classes = [IsAuthenticated]

    tamplate = 'company/projects.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        projects = CreateProject.objects.all()

        return render(request, self.tamplate, {'projects': projects})


class ViewBids(View):
    permission_classes = [IsAuthenticated]

    tamplate = 'company/viewBids.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        projects = CreateBid.objects.all()

        return render(request, self.tamplate, {'projects': projects})


class Universities(View):
    permission_classes = [IsAuthenticated]

    tamplate = 'company/universities.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, self.tamplate)


class CreateProjectView(View):
    template_name = 'company/createProjects.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        # GetMethod
        form = ProjectCreationForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # PostMethod
        form = ProjectCreationForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProjectCreationForm()
        context = {'form': form}
        return render(request, self.template_name, context)


class UserApi(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated]
