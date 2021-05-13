from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_page,name='login'),
    path('register/',views.register,name='register'),
    path('savedetails/',views.savedetails,name='savedetails'),
    path('validate/',views.validate,name='validate'),
    path('list/',views.list,name='list'),
    path('save/',views.save,name='save'),
    path('create/',views.create,name='craete'),
    path('<int:id>/details/',views.details,name='details'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('logout/',views.logout_page,name='logout')


]