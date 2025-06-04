from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/home.html',{'email': 'Example@Example.com', 'skills': ['Python', 'Django', 'JavaScript'],'favorite_color' :'Blue'})

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')