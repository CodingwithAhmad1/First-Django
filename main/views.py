from sympy import *
import cmath 
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# import HttpResponse, HttpResponseRedirect


# Create your views here.  # this will store the different views of our app
# we can create multiple views
# 'python manage.py runserver' to run server


def home(response):  # this is the home page
    return render(response, "main/home.html", {})

def base_calc(response):  # this is the home page
    return render(response, "main/base_calc.html", {})

def addition(response):  # this is the addition page
    return render(response, "main/addition.html", {})

def motion(response):  # this is the addition page
    return render(response, "main/motion.html", {})

def trignometry(response):  
    return render(response, "main/trignometry.html", {})

def result(response):  # this is the result page
    return render(response, "main/result.html", {})


def about(response):  # this is the about page
    return render(response, "main/about.html", {})

def base(response):  # home page with calculators
    return render(response, "main/base.html", {})



def base_home(response):  # home page with calculators
    return render(response, "main/base_home.html", {})

def algebra(response): 
    return render(response, "main/algebra.html", {})

def calculators(response): 
    return render(response, "main/calculators.html", {})

def algebra1(response):  # home page with calculators
    return render(response, "main/algebra1.html", {})


def algebra_res1(request):
    a = int(0 if request.GET['num1'] =="" else request.GET['num1'])
    b = int(0 if request.GET['num2'] =="" else request.GET['num2'])
    c = int(0 if request.GET['num3'] =="" else request.GET['num3'])
    
    d = (b**2 - 4*a*c)
    
    x,y,z = symbols('x,y,z', real=True)
    sol_1 = (-b -cmath.sqrt(d))/ 2*a
    sol_2 = (-b + cmath.sqrt(d))/ 2*a
    sol_1 = str(sol_1)
    sol_2 = str(sol_2)
    sol_1 = sol_1.replace("0j", " ")
    sol_2 = sol_2.replace("0j", " ")
    sol_1 = sol_1.replace("j", " ")
    sol_2 = sol_2.replace("j", " ")
    sol_1 = sol_1.replace("+", " ")
    sol_2 = sol_2.replace("+", " ")
    sol_1 = sol_1.replace("(", " ")
    sol_2 = sol_2.replace("(", " ")
    sol_1 = sol_1.replace(")", " ")
    sol_2 = sol_2.replace(")", " ")
    expr = a*x**2 + b*x + c
    factorised = str(expr.factor())
    if factorised[1] == "*":
        factorised[1] == ""
        
    return render(request, 'main/algebra_res1.html', {'algebra_1': sol_1, 'algebra_2':sol_2, 'factorised_1': factorised})
