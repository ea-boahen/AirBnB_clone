#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
e_model = BaseModel()
e_model.name = "My_First_Model"
e_model.my_number = 89
e_model.save()
print(e_model)#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
e_model = BaseModel()
e_model.name = "My_First_Model"
e_model.my_number = 89
e_model.save()
print(e_model)
