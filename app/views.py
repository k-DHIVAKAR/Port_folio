from django.shortcuts import render

# Create your views here.


def index_view(request):
    return render(request,'index.html')

def education_view(request):
    return render(request,'eduction.html')

def skils_view(request):
    return render(request,'skils.html')

def project_view(request):
    return render(request,'project.html')

def details_view(request):
    return render(request,'details.html')

def contact_view(request):
    return render(request,'contact.html')
