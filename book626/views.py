import os
from .forms import BasicInfoForm
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse


def welcome(request):
    return HttpResponse("Hello there!")


def basic_info(request):
    if request.method == 'Post':
        form = BasicInfoForm(request.POST)
        if form.is_valid():
            info = form.save()
            info.save()
            return HttpResponseRedirect(reverse('book626.views.welcome'))
    else:
        form = BasicInfoForm()

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(request, os.path.join(project_root, 'book626/templates', 'basicinfo.html'), {'form': form})
