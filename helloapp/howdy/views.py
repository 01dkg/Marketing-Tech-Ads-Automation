# howdy/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import LoginForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

# Add this view
class AboutPageView(TemplateView):
    template_name = "about.html"

def someview(request):
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            print("hello ")
            # do something when valid
    else:
        login_form = LoginForm()
