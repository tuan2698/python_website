from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/home.html',{'email': 'Example@Example.com', 'skills': ['Python', 'Django', 'JavaScript'],'favorite_color' :'Blue'})

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def resume(request):
    return render(request, 'pages/resume.html')

def error(request, exception):
    return render(request, 'pages/error.html', status=404)