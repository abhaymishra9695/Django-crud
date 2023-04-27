from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import StudenRegistration
from .models import User
# Create your views here.


#creat and show data
def addshow(request):
    if request.method=="POST":
        fm=StudenRegistration(request.POST)
        # if fm.is_valid():
        #     fm.save()
            # or
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pm=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pm)
            reg.save()
            fm=StudenRegistration()

    else:
         fm=StudenRegistration()
    st=User.objects.all()
         

    return render(request,'addshow.html',{'form':fm,"student":st})

def delet_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        # redirect('/')
        return HttpResponseRedirect('/')

def update_data(request, id):
        if request.method=="POST":
            pi=User.objects.get(pk=id)          
            fm=StudenRegistration(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
            return redirect('addshow')
        else:
            
            pi=User.objects.get(pk=id)  
            fm=StudenRegistration(instance=pi)
        return render(request,'update.html',{'form':fm})













