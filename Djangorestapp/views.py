from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
# Create your views here.
#django restframework..
import json
from django.http import JsonResponse
from django.views.generic import View
from Djangorestapp.mixins import HttpResponseMixin
from django.core.serializers import serialize
from Djangorestapp.mixins import SerializeMixin,HttpResponseMixin
import os
#ignoring csrf token..
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from Djangorestapp.utils import is_json
from Djangorestapp.forms import EmployeeForm
#swamy crud
from rest_framework.viewsets import ModelViewSet
from Djangorestapp.serializers import MemberSerializer

#python life
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework import viewsets
#authentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

@api_view()
def hello(request):
    return Response('manusha')




#crud operations..
#create
# @api_view(['GET'])
# def home(request):
#     student = Member.objects.all()
#     serializer = MemberSerializer(student,many=True)
#     return Response(serializer.data)

# #add user..
# @api_view(['POST'])
# def add(request):
#     student = Member.objects.all()
#     serializer = MemberSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# #update user..
# @api_view(['POST'])
# def update(request,id):
#     student = Member.objects.get(id=id)
#     serializer = MemberSerializer(instance=student,data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# #delete user..
# @api_view(['DELETE'])
# def delete(request,id):
#     student = Member.objects.get(id=id)
#     student.delete()
#     return Response("the item has deleted")

#generic api view mixins..
#ListModelMixin
class Memberlistcreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset= Member.objects.all()
    serializer_class = MemberSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)


#CreateModelMixin  this create model mixin is combined in the listmodelmixin it is jumbled vth the listmodelmixin..

# class Membercreate(GenericAPIView,CreateModelMixin):
#     queryset= Member.objects.all()
#     serializer_class = MemberSerializer
#     def post(self,request):
#         return self.create(request)

#RetrieveModelMixin
#All model mixin in the single class..
class Memberdisplay(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset= Member.objects.all()
    serializer_class = MemberSerializer
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)
    def put(self,request,**kwargs):
        return self.update(request,**kwargs)
    def delete(self,request,**kwargs):
        return self.destroy(request,**kwargs)

#UpdateModelMixin
class MemberUpdate(GenericAPIView,UpdateModelMixin):
    queryset= Member.objects.all()
    serializer_class = MemberSerializer
    def put(self,request,**kwargs):
        return self.update(request,**kwargs)

#DestroyModelMixin

class MemberDelete(GenericAPIView,DestroyModelMixin):
    queryset= Member.objects.all()
    serializer_class = MemberSerializer
    def delete(self,request,**kwargs):
        return self.destroy(request,**kwargs)
#we can use the classes in the single class..

#  Durga restframework views..

#Html response..
def emp(request):
    emp_data ={
        'Sno':1,
        'Name':'swamy',
        'Sal':25000,
    }
    resp='<h4>EmpNo:{} <br>EmpName:{}<br>Empsal:{}<br></h1>'.format(emp_data['Sno'],emp_data['Name'],emp_data['Sal'])
    return HttpResponse(resp) #this is response will gets in the html format then user can understand the response but machine can't uderstand..

def dictojson(request):
    emp_data ={
        'Sno':1,
        'Name':'swamy',
        'Sal':25000,
    }
    json_data = json.dumps(emp_data)
    return HttpResponse(json_data,content_type='application/json') #this response will gets in the json format human and machine can understand the response..

def jsonres(request):
    emp_data ={
        'Sno':1,
        'Name':'swamy',
        'Sal':25000,
        'age':22,
    }
    return JsonResponse(emp_data) #this response will gets in the json format human and machine can understand the response..

#class based views..
class JsonCBV(HttpResponseMixin,View):
    def get(self,request,*args,**kwargs):
        json_data= json.dumps({'name':'swamy  is python and php developer','age':22})
        return self.render_to_http_response(json_data)

    def post(self,request,*args,**kwargs):
        json_data= json.dumps({'name':'swamy patel is python and php developer','age':22})
        return self.render_to_http_response(json_data)

    def put(self,request,*args,**kwargs):
        json_data= json.dumps({'name':'swamy patel is python and php developer','age':22})
        return self.render_to_http_response(json_data)

    def delete(self,request,*args,**kwargs):
        json_data= json.dumps({'name':'swamy patel is python and php developer','age':22})
        return self.render_to_http_response(json_data)

#crud operations..

#this class without serialization..
class EmployeeDetailCBV(View):
    def get(self,request,id,*args,**kwargs):
        emp_data =Employee.objects.get(id=id)
        dict_format={
            'name':emp_data.EmpName,
            'role':emp_data.Emprole,
            'sal':emp_data.EmpSal
        }
        json_data= json.dumps(dict_format) #converting the dict to json using the dumps..
        return HttpResponse(json_data,content_type='application/json')
#class withserialization..
#retrieving the single data..
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeSerialize(HttpResponseMixin,SerializeMixin,View):#using serialize mixin here..
    def get(self,request,id,*args,**kwargs):
            emp_data = Employee.objects.get(id=id)
            # json_data = serialize('json',[emp_data,])
            json_data = self.serialize([emp_data,])
            # return HttpResponse(json_data,content_type='application/json')
            return self.render_to_http_response(json_data)
    

    #update operation....
    def get_object_by_id(self,id):
        try:
         emp=Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp=None
        return emp
    def put(self,request,id,*args,**kwargs):
        emp = self.get_object_by_id(id) #calling the method in another method using the self.methodname
        if emp is None:
             json_data=json.dumps({'msg':'No record is found'})
             return self.render_to_http_response(json_data,status=400)
        data = request.body #getting the data from the test.py using the request.body method..
        valid_json = is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'plz send the valid json data'})
            return self.render_to_http_response(json_data,status=400)
        provided_data =json.loads(data) #converting the json data to the pythondict data
        orginal_data={
        "EmpName": emp.EmpName,
        "Emprole": emp.Emprole,
         "EmpSal": emp.EmpSal,
        }
        orginal_data.update(provided_data) #updating the original data with the provided with the sum fields..
        form = EmployeeForm(orginal_data,instance=emp) #storing the original data into the employee form...
        if form.is_valid():
            form.save()
            json_data=json.dumps({'msg':'record is updated succesfully'})
            return self.render_to_http_response(json_data)
        elif form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)
    #delete operation
    def delete(self,request,id,*args,**kwargs):
        emp = self.get_object_by_id(id) #calling the method in another method using the self.methodname
        if emp is None:
             json_data=json.dumps({'msg':'No record is found'})
             return self.render_to_http_response(json_data,status=400)
        delete_record = emp.delete()
        print(delete_record)
        json_data=json.dumps({'msg':'record is deleted succesfully'})
        return self.render_to_http_response(json_data)





        
            

#fetching the all data
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeListSerialize(HttpResponseMixin,SerializeMixin,View):
    def get(self,request,*args,**kwargs):
        emp_data = Employee.objects.all()
        # json_data = serialize('json',emp_data) #conveting the queryset to the json using serialize
        # python_dict = json.loads(json_data) #coverting from json to pythondict
        # #print(python_dict)
        # final_list=[]
        # for x in python_dict:
        #     remove_fields= x['fields'] #removing fields from the data #fields is the key for the employee data. thats y i took the fields
        #     final_list.append(remove_fields) #getting the values of the fields..
        # lastlist=json.dumps(final_list) #converting the dict to json..
        #we commented the code .. becoz already wrote in the serialize mixin..

        lastlist = self.serialize(emp_data) #here used the Serialize mixin class to avoid the heavy code in the view..
        # return HttpResponse(lastlist,content_type='application/json') #it original response
        return self.render_to_http_response(lastlist) #taken from the HttpResponseMixin..
    #creating the newuser in the database...
    def post(self,request,*args,**kwargs):
        data =request.body #getting the data from the test.py
        valid_json = is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'plz send the valid json data'})
            return self.render_to_http_response(json_data,status=400)
        empdata =json.loads(data)
        form = EmployeeForm(empdata) #storing the empdata in the form
        if form.is_valid():
            form.save()
            json_data=json.dumps({'msg':'record is stored is succesfully'})
            return self.render_to_http_response(json_data)
        elif form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)


#total crud operations with single url..
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCRUDCBV(HttpResponseMixin,SerializeMixin,View):
    def get_object_by_id(self,id):
        try:
            emp=Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp=None
        return emp
    def get(self,request,*args,**kwargs):
        data =request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'plz send the valid Json data'})
            return self.render_to_http_response(json_data,status=400)
        pdata = json.loads(data)
        id =pdata.get('id',None) #if id is there will get the corresponding data if id is not there then will get the None
        if id is not None:
            emp = self.get_object_by_id(id)
            if emp is None: #if we seached is not there it will execute this code..
                json_data = json.dumps({'msg':'Your searched id  is not available'})
                return self.render_to_http_response(json_data,status=404)
            json_data = self.serialize([emp,]) #it will execute if the searched is there..
            return self.render_to_http_response(json_data)
        emp_data = Employee.objects.all()
        json_data = self.serialize(emp_data) 
        return self.render_to_http_response(json_data)
    def post(self,request,*args,**kwargs):
        data =request.body #getting the data from the test.py
        valid_json = is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'plz send the valid json data'})
            return self.render_to_http_response(json_data,status=400)
        empdata =json.loads(data)
        form = EmployeeForm(empdata) #storing the empdata in the form
        if form.is_valid():
            form.save()
            json_data=json.dumps({'msg':'record is stored is succesfully'})
            return self.render_to_http_response(json_data)
        elif form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)

    def put(self,request,*args,**kwargs):
        data =request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'plz send the valid json data'})
            return self.render_to_http_response(json_data,status=400)
        pdata = json.loads(data)
        id =pdata.get('id',None) #if id is there will get the corresponding data if id is not there then will get the None
        if id is None:
            json_data=json.dumps({'msg':'To perform updation id is mandatory,please provide the id'})
            return self.render_to_http_response(json_data,status=400)
        emp = self.get_object_by_id(id)
        if emp is None:
             json_data=json.dumps({'msg':'No record is found ,to perform updation '})
             return self.render_to_http_response(json_data,status=400)
        provided_data =json.loads(data) #converting the json data to the pythondict data
        orginal_data={
        "EmpName": emp.EmpName,
        "Emprole": emp.Emprole,
         "EmpSal": emp.EmpSal,
        }
        orginal_data.update(provided_data) #updating the original data with the provided with the sum fields..
        form = EmployeeForm(orginal_data,instance=emp) #storing the original data into the employee form...
        if form.is_valid():
            form.save()
            json_data=json.dumps({'msg':'record is updated succesfully'})
            return self.render_to_http_response(json_data)
        elif form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)
    def delete(self,request,*args,**kwargs):
        data =request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'plz send the valid json data'})
            return self.render_to_http_response(json_data,status=400)
        pdata = json.loads(data)
        id =pdata.get('id',None) #if id is there will get the corresponding data if id is not there then will get the None
        if id is not None:
            emp = self.get_object_by_id(id)
            if emp is None: #if we seached is not there it will execute this code..
                json_data = json.dumps({'msg':'Your searched id  is not available'})
                return self.render_to_http_response(json_data,status=404)
            delete_record=emp.delete()
            print(delete_record)
            json_data=json.dumps({'msg':'record is deleted succesfully'})
            return self.render_to_http_response(json_data)

        json_data=json.dumps({'msg':'To perform deletion id is mandatory,please provide the id'})
        return self.render_to_http_response(json_data,status=400)
        
@api_view(['GET'])       
def swamy(request):
    Cricketer_data= Cricketer.objects.all() #queryset...
    serializer = CricketerSerializer(Cricketer_data,many=True)
    # return Response({'status':200,'payload':serializer.data})
    return Response(serializer.data)

#crud operations..
#create
@api_view(['POST'])
def create_cricketerlist(request):
    Cricketer_data= Cricketer.objects.all() #queryset...
    serializer = CricketerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
#update..
@api_view(['POST'])
def update_cricketerlist(request,id):
    Cricketer_data= Cricketer.objects.get(id=id)#queryset...
    serializer = CricketerSerializer(instance=Cricketer_data,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#delete user..
@api_view(['DELETE'])
def delete_cricketerlist(request,id):
    student = Cricketer.objects.get(id=id)
    student.delete()
    return Response("The item has deleted")

#all the classs that re merged into the single class
#class for the fetching the data and creating the another record in the db..
class Cricketlistcreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset= Cricketer.objects.all()
    serializer_class=CricketerSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

# class Cricketcreate(GenericAPIView,CreateModelMixin):
#     queryset= Cricketer.objects.all()
#     serializer_class=CricketerSerializer
#     def post(self,request):
#         return self.create(request)

#all the clases that have primary key value  are merged into the single class..
class Cricketdisplay(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset= Cricketer.objects.all()
    serializer_class=CricketerSerializer
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)
    def put(self,request,**kwargs):
        return self.update(request,**kwargs)
    def delete(self,request,**kwargs):
        return self.destroy(request,**kwargs)


# class CricketUpdate(GenericAPIView,UpdateModelMixin):
#     queryset= Cricketer.objects.all()
#     serializer_class=CricketerSerializer
#     def put(self,request,**kwargs):
#         return self.update(request,**kwargs)
    

# class Cricketdel(GenericAPIView,DestroyModelMixin):
#     queryset= Cricketer.objects.all()
#     serializer_class=CricketerSerializer
#     def delete(self,request,**kwargs):
#         return self.destroy(request,**kwargs)

# we can fetch the data and delete and update data within 3 lines only  using the ListAPIView,CreateAPIview..
class cricket_api_list(ListAPIView):
    queryset = Cricketer.objects.all()
    serializer_class = CricketerSerializer
    
#create API view
class cricket_api_create(CreateAPIView):
    queryset = Cricketer.objects.all()
    serializer_class = CricketerSerializer

#Retrieve API view
class cricket_api_retrieve(RetrieveAPIView):
    queryset = Cricketer.objects.all()
    serializer_class = CricketerSerializer

#Update API View
class cricket_api_update(UpdateAPIView):
    queryset = Cricketer.objects.all()
    serializer_class = CricketerSerializer

#Delete API View
class cricket_api_delete(DestroyAPIView):
    queryset = Cricketer.objects.all()
    serializer_class = CricketerSerializer

#combining both list and create together
class cricket_api_lc(ListCreateAPIView):
    queryset = Cricketer.objects.all()
    serializer_class = CricketerSerializer

#combining the Retrieve,Update,Destroy together..
class cricket_api_RUD(RetrieveUpdateDestroyAPIView):
    queryset = Cricketer.objects.all()
    serializer_class = CricketerSerializer

#view sets..
class CricketerViewset(viewsets.ViewSet):
    def list(self,request):
        queryset =Cricketer.objects.all()
        serializer = CricketerSerializer(queryset,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        id = pk
        if id is not None:
            queryset= Cricketer.objects.get(id=id)
            serializer = CricketerSerializer(queryset)
            return Response(serializer.data)

    def update(self,request,pk):
        id = pk
        queryset= Cricketer.objects.get(pk=id)
        serializer = CricketerSerializer(queryset,data=request.data) #converting the pythonobject to the json..
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data has been updated..'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk):
        id = pk 
        queryset= Cricketer.objects.get(pk=id)
        queryset.delete()
        return Response({'msg':'Data is deleted'})
    
    def create(self,request):
         serializer = CricketerSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Another Data is created'})
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CricketModelviewset(viewsets.ModelViewSet):
    queryset = Cricketer.objects.all()
    serializer_class = CricketerSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]


            





        

        
            
        

        