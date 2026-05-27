from shape import *
from logger import get_logger
logger=get_logger("squere")
class Squere(Shape):
    def __init__(self,shape_id,shape_type,side):
        super().__init__(shape_id,shape_type)
        self.side=side


    def get_area(self):
        """הפונקציה מחשבת שטח"""
        logger.info("calculate area")
        return str(self.side**2)
    def get_perimeter(self):
        """הפונקציה מחשבת היקף"""
        logger.info("calculate perimeter")
        return str(self.side*4)
    def to_dict(self):
        """ הפונקציה שומרת נתונים לדיקט"""
        return{str(self.shape_id):{"side":str(self.side),
            "area":self.get_area(),"perimeter":self.get_perimeter()}}

if __name__=="__main__":
    s1 = Squere(1, "squere", 5)
    print(s1.get_area())
    print(s1.get_perimeter())
    print(s1.to_dict())
    s2 = Squere(1, "squere", 5)
    print(s2.get_area())
    print(s2.get_perimeter())
    print(s2.to_dict())


