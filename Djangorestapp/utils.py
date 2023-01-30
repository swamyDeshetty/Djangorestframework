import json
from .models import *
def is_json(data):
    try:
        p_data= json.loads(data) #if the data is succesfully converted to python then the data is the json data
        valid =True
    except ValueError:
        valid = False
    return valid
