from shape import *
from logger import get_logger
logger=get_logger("circle")
pi=3.14
class Circle(Shape):
    def __init__(self,shape_id,shape_type,radius):
        super().__init__(shape_id,shape_type)
        self.radius=radius
    def get_area(self):
        logger.info("calculate area")
        return str((self.radius**2)*3.14)
    def get_perimeter(self):
        logger.info("calculate perimeter")
        return str((self.radius*2)*3.14)

    def to_dict(self):
        return {str(self.shape_id):{"radius":str(self.radius),
        "area":self.get_area(),"perimeter":self.get_perimeter()}}
