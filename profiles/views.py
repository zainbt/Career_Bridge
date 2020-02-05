from django.shortcuts import render
from django.views import View
# Create your views here.


class BlogView(View):
    tamplate = 'profile/blog.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.tamplate)


class ProfilePorjectionView(View):
    tamplate = 'profile/projectForm.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.tamplate)


class AboutView(View):
    tamplate = 'profile/aboutus.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.tamplate)


class FAQ(View):
    template = 'FAQ/faq.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template, *args, **kwargs)


class AccountsFAQ(View):
    template = 'FAQ/accountsFaq.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template, *args, **kwargs)


class BiddingFAQ(View):
    template = 'FAQ/biddingFaq.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template, *args, **kwargs)


class ContactFAQ(View):
    template = 'FAQ/contactFaq.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template, *args, **kwargs)


class ProjectsFAQ(View):
    template = 'FAQ/projectsFaq.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template, *args, **kwargs)




