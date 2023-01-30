from django.http import HttpResponse
from django.core.serializers import serialize
from django.http import HttpResponse
import json
class HttpResponseMixin(object):
    def render_to_http_response(self,json_data):
        return HttpResponse(json_data,content_type='application/json',status=200)
        #it is mainly is used for code reusability//
class SerializeMixin(object):
    def serialize(self,emp_data):
        json_data = serialize('json',emp_data)
        python_dict = json.loads(json_data)
        final_list=[]
        for x in python_dict:
            remove_fields= x['fields'] #removing fields from the data #fields is the key for the employee data. thats y i took the fields
            final_list.append(remove_fields) #getting the values of the fields..
        lastlist=json.dumps(final_list) #converting the dict to json..
        return lastlist
class HttpResponseMixin(object):
    def render_to_http_response(self,json_data,status=200):
        return HttpResponse(json_data,content_type='application/json',status=status)
    

