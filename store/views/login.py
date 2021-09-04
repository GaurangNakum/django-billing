from django.shortcuts import render , redirect , HttpResponseRedirect

from django.contrib.auth.hashers import  check_password
from store.models.employee import Employee
from django.views import  View

# Create your views here.


class Login(View):
    return_url = None
    def get(self,request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')
        
    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        employee = Employee.get_employee_by_email(email)
        error_message = None
        if employee:
            flag = check_password(password ,employee.password )
            
            if flag:
                request.session['employee'] = employee.id
                request.session['employee_email'] = employee.email
                request.session['employee_name'] = employee.first_name
                
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = "Email or Password Invalid !!!"
        else:
            error_message = "Email or Password Invalid !!!"
        
        return render(request,'login.html',{'error' : error_message})

def logout(request):
    request.session.clear()
    return redirect('login')