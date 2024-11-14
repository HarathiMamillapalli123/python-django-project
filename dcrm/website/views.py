from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html', {})

def chinni(request):
    return render(request,'chinni.html', {})