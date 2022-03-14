from django.shortcuts import render

from testing.forms import Studentform

# Create your views here.
def index(request):
    form = Studentform()
    return render(request,'index.html',{'form':form})

def view(request):
    return render(request,'view.html')
    