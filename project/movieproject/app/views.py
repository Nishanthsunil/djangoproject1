from django.shortcuts import render,redirect
from .models import movie
from .forms import movieform

def index(request):
    a=movie.objects.all()
    return render(request,'index.html',{'result':a})

def detail(request,movie_id):
    details=movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'a':details})

def update(request,id):
    instance=movie.objects.get(id=id)  
    form=movieform(request.POST or None,request.FILES,instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/')
    form=movieform(instance=instance)

    return render(request,'edit.html',{'form':form})

def delete(request,id):
    if request.method=='POST':
        a=movie.objects.get(id=id)
        a.delete()
        return redirect('/')
    return render(request,'delete.html')

def add(request):
    form=movieform(request.POST or None , request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/')
    form=movieform()

    return render(request,'add.html',{'form':form})


# Create your views here.
