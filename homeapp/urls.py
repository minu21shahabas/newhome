from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
       path('',views.home,name='home'),
       path('homes',views.homes,name='homes'),
       path('about',views.about,name='about'),
       path('project',views.project,name='project'),
       path('contact',views.contact,name='contact'),
       path('gal',views.gal,name='gal'),
       path('more',views.more,name='more'),
       path('more1',views.more1,name='more1'),

]