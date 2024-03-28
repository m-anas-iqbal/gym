from django.shortcuts import render,HttpResponse,redirect
from .models import *
def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        getname = request.POST.get('name')
        getemail = request.POST.get('email')
        getmessage = request.POST.get('message')
        # rec = CheckUserName(getUName)
        # if rec == True:
        #     Msg = '0'
        # else:
        dataUser = users(name=getname,email=getemail,password=getmessage)
        dataUser.save()

            # Msg = '1'
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def pricing(request):
    return render(request, 'pricing.html')

def courses(request):
    return render(request, 'courses.html')

def login(request):
    Msg = 0
    if request.method == 'POST':
        getUserName = request.POST.get('tUsername')
        getPassword = request.POST.get('tPass')
        User = users.objects.filter(name=getUserName,password=getPassword).values()
        if User.count() > 0:
            Msg = '2'
            request.session['name'] = str(User.get()['name'])
            request.session['email'] = str(User.get()['email'])
            return redirect('/')
        # return HttpResponse("Success"+str(User.get()['fullname'])+"")
        else:
            Msg = '3'
    return render(request,'login.html',{'Message': Msg})

def register(request):
    if request.method == 'POST':
        getUName = request.POST.get('tUsername')
        getEmail = request.POST.get('tEmail')
        getPass = request.POST.get('tPass')
        # rec = CheckUserName(getUName)
        # if rec == True:
        #     Msg = '0'
        # else:
        dataUser = users(name=getUName,email=getEmail,password=getPass)
        dataUser.save()

            # Msg = '1'
    return render(request, 'login.html')
    # return render(request, 'login.html', {'Message': Msg})


# def CheckUserName(Username):
#     Msg = users.objects.filter(name=Username)
#     Result = False
#     if Msg.count() > 0:
#         Result = True
#     return Result

def checkout(request):
    return render(request, 'checkout.html')

def edit_profile(request):
    return render(request, 'edit_profile.html')

def logout(request):
    request.session['name']  = ""
    request.session['email']  = ""
    return redirect('/login')
# Create your views here.

# Create your views here.
