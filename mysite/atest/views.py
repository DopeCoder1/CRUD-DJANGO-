from django.shortcuts import render,redirect
from .models import Atestation
from .forms import AtestationForm
from django.views.generic import DetailView,UpdateView,DeleteView

# Create your views here.


def home_page(request):
    students = Atestation.objects.all()
    return render(request,  'atest/home_page.html',{"students":students})

def add_student(request):#CREATE
    error = ""
    form = AtestationForm()
    if(request.method == "POST"):
        form = AtestationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('home_page')
        else:
            error="Form isn't true"

    data = {
    "form":form,
    "error":error,
    }
    return render(request,  'atest/add_student.html',data)

class AtestationRead(DetailView): #READ
    model = Atestation
    template_name = 'atest/read.html'
    context_object_name = 'atestat'

class AtestationUpdate(UpdateView): #UPDATE
    model = Atestation
    template_name = 'atest/add_student.html'
    form_class =  AtestationForm

class AtestationDelete(DeleteView): #DELETE
    model = Atestation
    success_url = '/'
    template_name = 'atest/delete.html'
