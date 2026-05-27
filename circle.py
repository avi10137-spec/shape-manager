from shape import *
from logger import get_logger
logger=get_logger("circle")
class Circle(Shape):
    def __init__(self,shape_id,shape_type,radius):
        super().__init__(shape_id,shape_type)
        self.radius=radius
    def get_area(self):
        """הפונקציה מחשבת שטח"""
        logger.info("calculate area")
        return str((self.radius**2)*3.14)
    def get_perimeter(self):
        """הפונקציה מחשבת היקף"""
        logger.info("calculate perimeter")
        return str((self.radius*2)*3.14)

    def to_dict(self):
        """הפונקציה שומרת נתונים לדיקט"""
        return {str(self.shape_id):{"radius":str(self.radius),
        "area":self.get_area(),"perimeter":self.get_perimeter()}}


if __name__=="__main__":
    c1 = Circle(1, "circle", 3)
    print(c1.get_area())
    print(c1.get_perimeter())
    print(c1.to_dict())

