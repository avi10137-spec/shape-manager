from shape import *
from squere import *
from rectangle import *
from circle import *
from logger import get_logger
import json

class ShapeManager:
    shape_cls = {"circle": {"cls": Circle, "filed": ["radius"]},
                 "squere": {"cls": Squere, "filed": ["side"]},
                 "rectangle": {"cls": "rectangle", "filed": ["length", "width"]}}
    def __init__(self):
        self.shapes=[]
        self.load_from_json("shapes.json")

    def creat_shape(self, shape):
        shape_name = next(iter(shape))
        c1 = self.shape_cls[shape_name]["cls"](1, shape_name, **shape[shape_name])
        x = c1.to_dict()



    def get_all_shapes(self):
       pass
    def update_shape(self, shape_id, new_data):
       pass
    def delete_shape(self, shape_id):
       pass
    def save_to_json(self,filename,dikti):
        try:
            with open(filename,"w")as fil:
                json.dump(dikti,fil)
        except FileNotFoundError:
            print("file not exist")

    def load_from_json(self,filename):
        try:
            with open(filename,"r")as fil:
                dikti=json.load(fil)
                if dikti==None:
                    return ""
                return dikti
        except (FileNotFoundError, json.JSONDecodeError):
            print("file is not empty")
            self.shapes_list = ""
            return self.shapes_list

    # def create_shape(self, shape,*args):
    #     if shape=="circle":
    #         c1=Circle(1,"circle",*args)
    #         dikti=c1.to_dict()
    #         # list_shape.append(dikti)
    #     return dikti
        if shape=="squere":
            s1.Squere(1,"squere",*args)
            print(s1.to_dict())
        if shape=="rectangle":
            r1=Rectangle(1,"rectangle",*args)





