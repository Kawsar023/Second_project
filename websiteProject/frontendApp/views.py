from django.shortcuts import render
from adminpannel.models import aboutus

def index(request):
    # about_us = aboutus.objects.filter(is_active = True).first()
    about_us = aboutus.objects.filter(is_active = True).last()
    return render(request, 'frontend/index.html',{'about_us' : about_us})

def about(request):
    about_us = aboutus.objects.filter(is_active = True).last()
    return render(request, 'frontend/about.html',{'about_us' : about_us})

# def speakers(request):
#     speak_rs = speakers.objects.filter(is_active = True).last()
#     return render(request, 'frontend/speakers.html',{'speak_rs' : speak_rs})
