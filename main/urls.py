# define the path to our different web pages
# will represent the urls that go to the different views

from django.urls import path
from . import views

urlpatterns = [
    path("base_home/", views.base_home, name="base_home"),
    path("base.html", views.base, name="base"),
    path("addition/", views.addition, name="addition"),
    path("algebra/", views.algebra, name="algebra"),
    path("base_calc/", views.base_calc, name="base_calc"),
    path("result/", views.result, name="view"), 
    path("about/", views.about, name="about"), 
    path("home/", views.home, name="home"),
    path("motion/", views.motion, name="motion"),
    path("trignometry/", views.trignometry, name="trignometry"),
    path("calculators/", views.calculators, name="calculators"),
    path("algebra1/", views.algebra1, name="algebra1"),
    path("algebra_res1/", views.algebra_res1, name="algebra_res1"),
    path("algebra1/algebra_res1", views.algebra_res1, name="algeb_res1"),
    path("", views.base, name="base"), 
    
    # you write the name of the function
]
