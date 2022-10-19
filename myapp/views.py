from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Users
from .models import ContactData


# Create your views here.
def home(request):
    if request.method == "POST":
        email = request.POST['usermail']
        psw = request.POST['userpsw']
        data = Users.objects.filter(email=email).values()

        if len(data) >0:
            if data[0]['password'] == psw:
                request.session['name'] = data[0]['name']
                return render(request, "dashboard.html", {'username': data[0]['name']})
            else:
                return render(request, 'register.html')
        else:
            return render(request, 'register.html')
    return render(request, 'Login.html')


def register(request):
    if request.method == "POST":
        u_name = request.POST['username']
        uname = u_name + "_xenon"
        u_email = request.POST['useremail']
        psw = request.POST['userpassword']
        user_inst = Users.objects.create(name=u_name, email=u_email, username=uname, password=psw)
        return redirect('/')
    return render(request, "register.html")




def logout(request):
    try:
        del request.session['name']
        print("logged out")
    except KeyError:
        pass
    return redirect('/')


def contact(request):
    if(request.method == "POST"):
        name= request.POST['userName']
        con_no = request.POST['ContactNo']
        con_inst = ContactData.objects.create(name=name,Contact_no=con_no)
        return redirect('/')
    return render(request, "Contact.html")