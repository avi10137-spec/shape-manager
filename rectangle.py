from shape import *
from logger import get_logger
logger=get_logger("rectangle")
class Rectangle(Shape):
    def __init__(self,shape_id,shape_type,length,width):
        super().__init__(shape_id,shape_type)
        self.length=length
        self.width=width
    def get_area(self):
        logger.info("calculate area")
        return str(self.length*self.width)
    def get_perimeter(self):
        logger.info("calculate perimeter")
        return str((self.length*2)+(self.width*2))
    def to_dict(self):
        return {str(self.shape_id):{"length":str(self.length)
            ,"width":str(self.width),"area":self.get_area(),
             "perimeter":self.get_perimeter()}}
