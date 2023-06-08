from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'homepage.html')
def homes(request):
    return render(request,'homepage.html')
def about(request):
    return render(request,'aboutus.html')
def project(request):
    return render(request,'project.html')
def contact(request):
    return render(request,'contact.html')
def gal(request):
    return render(request,'gallery.html')
def more(request):
    return render(request,'mores.html')
def more1(request):
    return render(request,'mores1.html')



