from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from accounts.models import User
from .models import CreateProject
from .forms import ProjectCreationForm
from university.models import CreateBid
# Create your views here.


class DashBoardView(View):
    # login_required = True
    tamplate = 'company/dashboard.html'
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        obj = User.objects.all()
        return render(request, self.tamplate, {'obj': obj})


class ProfileView(View):
    tamplate = 'company/compProfile.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.tamplate)


class Collaborations(View):

    tamplate = 'company/collaborations.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.tamplate)


class Projects(View):

    tamplate = 'company/projects.html'

    def get(self, request, *args, **kwargs):
        projects = CreateProject.objects.all()

        return render(request, self.tamplate, {'projects': projects})


class ViewBids(View):

    tamplate = 'company/viewBids.html'

    def get(self, request, *args, **kwargs):
        projects = CreateBid.objects.all()

        return render(request, self.tamplate, {'projects': projects})


class Universities(View):

    tamplate = 'company/universities.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.tamplate)


class CreateProjectView(View):
    template_name = 'company/createProjects.html'

    def get(self, request, *args, **kwargs):
        #GetMethod
        form = ProjectCreationForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        #PostMethod
        form = ProjectCreationForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProjectCreationForm()
        context = {'form': form}
        return render(request, self.template_name, context)