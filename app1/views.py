from django.shortcuts import render,redirect
from . import forms
from . import models
from .data_analysis import find

def signup(request):
    if request.method=='POST':
        form=forms.signup(request.POST)
        if form.is_valid():
            name1=form.cleaned_data['name']
            email1=form.cleaned_data['email']
            password1=form.cleaned_data['password']
            re_password1=form.cleaned_data['re_password']
            if password1==re_password1:
                try:
                    obj=models.user.objects.get(name=name1,password=password1)
                except:
                    models.user.objects.create(name=name1,email=email1,password=password1)
                return redirect('home')
            else:
                form=forms.signup()
                return render(request, 'signup.html', {'form':forms.signup})
        else:
            form=forms.signup()
            return render(request, 'signup.html', {'form':forms.signup})
    else:
        form=forms.signup()
        return render(request, 'signup.html', {'form':forms.signup})

def login(request):
    if request.method=='POST':
        form=forms.login(request.POST)
        if form.is_valid():
            email1=request.POST['email']
            password1=request.POST['password']
            try:
                obj=models.user.objects.get(email=email1,password=password1)
                return redirect('home')
            except:
                form=forms.login()
                return render(request, 'login.html', {'form':form})
        else:
            form=forms.login()
            return render(request, 'login.html', {'form':form})
    else:
        form=forms.login()
        return render(request, 'login.html', {'form':form})

def home(request):
    return render(request, 'index.html')

def aboutgujarat(request):
    return render(request, 'aboutgujarat.html')

def experience1(request):
    return render(request, 'experience1.html')

def experience2(request):
    return render(request, 'experience2.html')

def experience3(request):
    return render(request, 'experience3.html')

def experience4(request):
    return render(request, 'experience4.html')

def experience5(request):
    return render(request, 'experience5.html')

def experience6(request):
    return render(request, 'experience6.html')

def experience7(request):
    return render(request, 'experience7.html')

def experience8(request):
    return render(request, 'experience8.html')

def experience9(request):
    return render(request, 'experience9.html')

def experience10(request):
    return render(request, 'experience10.html')

def experience11(request):
    return render(request, 'experience11.html')

def experience12(request):
    return render(request, 'experience12.html')

def experience13(request):
    return render(request, 'experience13.html')

def recommendation(request):
    if request.method == "POST":
        form=forms.recommend()
        city=request.POST['city']
        type=request.POST['type']
        season=request.POST['season']
        places,infos = find(city,type,season)
        d = dict()
        for i in range(len(places)):
            d[places[i]]=infos[i]
        if len(places)==0:
            flag=False
        else:
            flag=True
        return render(request,'recommendationpage.html',{'form':form,'dict':d,'flag':flag})
    else:
        form = forms.recommend()
        flag=False
        places=[]
        infos=[]
    return render(request,'recommendationpage.html',{'form':form,'places':places,'infos':infos,'flag':flag})

def hotel(request):
    return render(request,'hotel.html')

def shopping(request):
    return render(request,'shopping.html')

def weather(request):
    return render(request,'weather.html')