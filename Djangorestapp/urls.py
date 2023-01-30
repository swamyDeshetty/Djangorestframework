from django.contrib import admin
from django.urls import path
from .import views 
import json
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('hello/', views.hello, name='hello'),
    # # path('home/', views.home, name='home'),
    # path('add/', views.add, name='add'),
    # path('update/<int:id>/', views.update, name='update'),
    # path('delete/<int:id>/', views.delete, name='delete'),

    # #class based views..
    # path('list/', views.Memberlistcreate.as_view()),
    # # path('create/', views.Membercreate.as_view()),
    # # path('display/<int:pk>/', views.Memberdisplay.as_view()),
    # # path('updatemixin/<int:pk>/', views.MemberUpdate.as_view()),
    # path('destroy/<int:pk>/', views.Memberdisplay.as_view()),

    #django rest framework..
    path('helloapi/', views.emp, name='helloapi'),
    path('json/', views.dictojson, name='json'),
    path('jsonres/', views.jsonres, name='jsonres'),
    #class based views..
    path('JsonCBV/', views.JsonCBV.as_view()),    
    path('get_data/<int:id>/', views.EmployeeDetailCBV.as_view()), 
    #crud operations..
    path('serialize/<int:id>/', views.EmployeeSerialize.as_view()),
    path('serialize/', views.EmployeeListSerialize.as_view()),  

    #crud
    path('api/', views.EmployeeCRUDCBV.as_view()),

    #new pythonlifetutorial
    path('home1/', views.swamy, name='home'),
    path('create/', views.create_cricketerlist, name='home'),
    path('update/<int:id>/', views.update_cricketerlist, name='update'),
    path('delete/<int:id>/', views.delete_cricketerlist, name='delete'),
    path('Listdata/', views.Cricketlistcreate.as_view()),  
 
    path('cricketdisplay/<int:pk>/', views.Cricketdisplay.as_view()), 

    # different types of api views 
    path('fetchdata/', views.cricket_api_list.as_view()),  
    path('createAPI/', views.cricket_api_create.as_view()),  
    path('retrieveAPI/<int:pk>', views.cricket_api_retrieve.as_view()),  
    path('updateAPI/<int:pk>', views.cricket_api_update.as_view()), 
    path('deleteAPI/<int:pk>', views.cricket_api_delete.as_view()), 
    path('lc/', views.cricket_api_lc.as_view()), 
    path('rud/<int:pk>', views.cricket_api_RUD.as_view()), 














       

      







    








]
