from shape import *
from squere import *  # שים לב שאם שינית ל-square, תתקן גם ב-import
from rectangle import *
from circle import *
from logger import get_logger
import json


class ShapeManager:

    shape_cls = {
        "circle": {"cls": Circle, "filed": ["radius"]},
        "squere": {"cls": Squere, "filed": ["side"]},
        "rectangle": {"cls": Rectangle, "filed": ["length", "width"]}
    }

    def __init__(self):
        self.dikt_shapes = {}
        self.data=self.load_from_json("shapes.json")

    def creat_shape(self, shape):
        shape_name = next(iter(shape))
        new_id = len(self.dikt_shapes)
        c1 = self.shape_cls[shape_name]["cls"](new_id, shape_name, **shape[shape_name])
        dikti = c1.to_dict()
        if self.data is None:
            self.data={}
        self.data = self.data | dikti
        self.save_to_json("shapes.json")


        # self.dikt_shapes[new_id] = dikti
        # return self.data

    def get_all_shapes(self):
        print(self.data)
        return self.data

    def update_shape(self, shape_id):
        shape_id = str(shape_id)

        if shape_id not in self.data:
            print("shape not found")
            return

        shape = self.data[shape_id]
        print(shape)
        shape_name = shape["type"]

        for field in self.shape_cls[shape_name]["filed"]:
            value = int(input(f"enter new {field}: "))
            shape[field] = value

        self.save_to_json("shapes.json")




    def delete_shape(self, shape_id):
            del self.data[shape_id]
            self.save_to_json("shapes.json")

    def save_to_json(self, filename):
        try:
            with open(filename, "w") as fil:
                json.dump(self.data, fil,indent=4)
                print("Saved successfully to JSON.")
        except FileNotFoundError:
            print("File or directory not found")

    def load_from_json(self, filename):
        try:
            with open(filename, "r") as fil:
                dikti = json.load(fil)
                if dikti:

                    self.dikt_shapes |= dikti
                return self.dikt_shapes
        except (FileNotFoundError, json.JSONDecodeError):
            print("File empty or not found, starting fresh.")
            self.dikt_shapes = {}
            return self.dikt_shapes





