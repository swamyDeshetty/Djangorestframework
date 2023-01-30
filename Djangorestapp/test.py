#using the functionality of the django in the python.. using http api 
import json
import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT ='api/'
#fetching the single data from the django 
def get_resource(id=None): #if we pass id=None then it is not mandatory to pass id in the url if we pass url if fetch the single data and if we not passed any id in the url it can fetch the all the records 
    data = {}
    if id is not None:
        data = {
            'id':id
        }
    resp= requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
get_resource()
x= input('Enter the id :')
get_resource(x)


#use url or endpoint (listserialize) if want to cl this function...
#fetching the all
# def get_all():
#     resp =requests.get(BASE_URL+ENDPOINT)
#     print(resp.json())
# get_all()

# #use url or endpoint (listserialize) if want to cl this function...
# def create_resouce():
#     new_emp ={
#         'EmpName':'shiva',
#         'Emprole':'Police',
#         'EmpSal': 5000,
#     }
#     resp = requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# create_resouce()
# #use url or endpoint (serialize) if want to cl this function...
# #updating the record
# def update_resource(id):
#     new_emp ={
#          'id':id,
#         'Emprole' :'Jober',
#         }
#     resp = requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# update_resource(20)   #while performing the another operation im commenting the function cal of the all functions becoz the all the functions are in the same class only...

# #use url or endpoint (serialize) if want to cl this function...
#delete operation..
def delete_resource(id):
    data={
        'id':id
    }
    resp = requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
data =input('Enter the id:')
delete_resource(data)