from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwags):

        if request.user.is_authenticated:
            return redirect('home')

        else:
            return view_func(request,*args,**kwags)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwags):
           
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request,*args,**kwags)

            else:
                return HttpResponse("You are not authorized to view this page")

        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_func(request,*args,**kwags):
        
        group = None

        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            
        if group == 'ToDoUsers':
            return redirect('user-page')

        if group == 'Admin':
            return view_func(request,*args,**kwags)
            # return redirect('admin/')

    return wrapper_func
