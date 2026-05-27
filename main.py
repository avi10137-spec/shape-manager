from shapemanager import ShapeManager
c1 = ShapeManager()
# def add_shape():
#     print("1. circle",
#           "2.squere",
#           "3.rectangle")
#
#     shape=input("enter your choise: ")
#     if shape == "1":
#         radius=int(input("enter radius"))
#     shape=c1.create_shape("circle",radius)
#     print(shape)
#     x=c1.load_from_json("shapes.json")
#     print(x)
#     c1.shapes.append(x)
#     print(c1.shapes)
#     c1.shapes.append(shape)
#     print(c1.shapes)
#     c1.save_to_json("shapes.json",c1.shapes)




def add_shape():
    shape_arg = {}
    user_choice = {"1":"circle","2":"square","3":"rectangle"}
    print("1.circle\n"
          "2.square\n"
          "3.rectangle")
    choice_shape=input("enter your choice: ")
    if choice_shape in user_choice:
        shape_arg[user_choice[choice_shape]]={}
        for arg in c1.shape_cls[user_choice[choice_shape]]["filed"]:
            try:
                parameter = int(input(f"please enter {arg}: "))
                shape_arg[user_choice[choice_shape]][arg]=parameter
            except ValueError as e:
                print( f"int needed {e}")
    else:
        print("invalid input")
    print(shape_arg)
    print(c1.creat_shape(shape_arg))
add_shape()