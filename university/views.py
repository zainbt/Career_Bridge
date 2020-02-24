from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from accounts.models import User
from company.models import CreateProject
from .forms import ProfileUpdateForm, CreateBidFroms
from .models import *
# Create your views here.


class DashBoardView(View):
    # login_required = True
    tamplate = 'university/dashboard.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        obj = User.objects.all()
        return render(request, self.tamplate, {'obj': obj})


class UProfileView(View):
    tamplate = 'university/uniProfile.html'

    def get(self, request, *args, **kwargs):
        obj = ProfileUpdate.objects.all()

        return render(request, self.tamplate, {'obj': obj})


class ProjectsView(View):
    tamplate = 'university/projects.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.tamplate)


class ClobsView(View):
    tamplate = 'university/collaborations.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.tamplate)


class ProjectFormView(View):
    tamplate = 'profile/projectForm.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.tamplate)


class ProfileView(View):
    template_name = 'university/universityProfile.html'

    def get(self, request, *args, **kwargs):
        #GetMethod
        form = ProfileUpdateForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        #PostMethod
        form = ProfileUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProfileUpdateForm()
        context = {'form': form}
        return render(request, self.template_name, context)


class Bidding(View):
    tamplate = 'university/bidding.html'

    def get(self, request, *args, **kwargs):
        obj = CreateProject.objects.all()
        return render(request, self.tamplate, {'obj': obj})


# class CreateBid(View):
#     tamplate = 'university/createBid.html'
#
#     def get(self, request, *args, **kwargs):
#         obj = CreateBid.objects.all()
#         return render(request, self.tamplate, {'obj': obj})


class CreateBid(View):
    template_name = 'university/createBid.html'

    def get(self, request, *args, **kwargs):
        #GetMethod
        form = CreateBidFroms()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        #PostMethod
        form = CreateBidFroms(request.POST)
        if form.is_valid():
            form.save()
            form = CreateBidFroms()
        context = {'form': form}
        return render(request, self.template_name, context)