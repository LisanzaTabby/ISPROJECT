from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('admindash',views.admindash, name='admindash'),
    path('addstudent',views.add_student, name='addstudent'),
    path('trustee', views.trusteeView, name='trustee'),
    path('dataentry', views.DataEntryView, name='dataentry'),
    path('finance', views.FinanceView, name='finance'),
    path('login', views.loginView, name='login'),
    path('signup', views.signupView, name='signup'),
    path('logout', views.logoutView, name='logout'),
]