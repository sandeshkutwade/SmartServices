import email
import imp
from re import U
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string




# Create your views here.
from .models import Order, Partners, Category
from .forms import CreateUserForm, AddPartner, PlaceOrder


# @login_required(login_url='SmartServices:login')
def home(request):
    workers = Partners.objects.all().count()
    Countuser = User.objects.all().count()
    OrderCount = Order.objects.all().count()
    context = {
         'partners': workers,
         'Countuser':Countuser,
         'Ordercount':OrderCount
    }
    return render(request, 'HeaderBase.html',context)

    # return render(request, 'Home.html')


@login_required(login_url='SmartServices:login')
def HirePage(request):
    return render(request, 'MainPages/Categories.html')


def categories(request):
    return {
        'categories': Category.objects.all()
    }

@login_required(login_url='SmartServices:login')
def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    partners = Partners.objects.filter(category=category)
    return render(request, 'MainPages/Hire_Emp.html', {'Category': category, 'partner': partners})

@login_required(login_url='SmartServices:login')
def worker_details(request, slug):
    if request.method == "POST":
        Name = request.POST['name']
        Email = request.POST['email']
        Phone = request.POST['phone']
        Address = request.POST['address']
        Ammount = request.POST['ammount']
        WorkerName = request.POST['workername']

        PlaceOrder = Order(Name = Name, Email = Email, Phone = Phone, Address = Address, Ammount = Ammount, WokerName = WorkerName)
        PlaceOrder.save()
        print(WorkerName)

        return redirect('SmartServices:email')

    worker = get_object_or_404(Partners, slug=slug)
    return render(request, 'MainPages/Single_Detail.html', {'workers': worker})



def BuyPageworker(request, slug):
    worker = get_object_or_404(Partners, slug=slug)
    return render(request, 'MainPages/BuyPage.html', {'workers': worker})

def partnerhome(request):
    return render(request, 'Base.html')


def Aboutus(request):
    return render(request,'PartnerPage/Aboutus.html' )


def Contact(request):
    return render(request,'PartnerPage/Contactus.html' )




# Adding Data into patner model.
def CreatePatner(request):
    if request.method == 'POST':
        form = AddPartner(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('Name')
            messages.success(request, "Welcome To Smart Services  " + user)
         
            return redirect('SmartServices:base')
    else:
        form = AddPartner()
    return render(request, 'MainPages/AddingPartner.html', {'form': form})



## Sending Email 

def SuccesEmail(request):
    import datetime
    NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=2)
    Day = NextDay_Date.day 
    Month = NextDay_Date.month 
    Y = NextDay_Date.year 
       
    tenplate = render_to_string('Email_Pop/EmailTmp.html',{'name':request.user})
    email = EmailMessage(
        ['SMART_SERVICES',Day,Month,Y],
        tenplate,
        settings.EMAIL_HOST_USER,
        [request.user.email],
    )
    email.fail_silently = False
    email.send(NextDay_Date)
    return render(request,'Email_Pop/Pop.html')







def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Acoount Created " + user)

                return redirect('SmartServices:login')

        context = {'form': form}
        return render(request, 'AccountData/Register.html', context)


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('/')

    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')

            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'AccountData/Login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('SmartServices:login')
