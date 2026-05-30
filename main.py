from shapemanager import ShapeManager
c1 = ShapeManager()



def add_shape(c):
    shape_arg = {}
    user_choice = {"1": "circle", "2": "squere", "3": "rectangle"}
    print("1.circle\n2.square\n3.rectangle")
    choice_shape = input("enter your choice: ")
    if choice_shape in user_choice:
        selected_shape = user_choice[choice_shape]
        shape_arg[selected_shape] = {}

        for arg in c1.shape_cls[selected_shape]["filed"]:
            try:
                parameter = int(input(f"please enter {arg}: "))
                shape_arg[selected_shape][arg] = parameter
            except ValueError as e:
                print(f"int needed {e}")
                return
    else:
        print("invalid input")
        return



def main(c):
    while True:
        print("1.add shape\n2.show all shape\n3"
              ".update shape\n4.delete shape\n5.exit")
        chois=input("enter your choise")
        if chois == "1":
            add_shape(c1)
        if chois =="2":
           c1.get_all_shapes()
        if chois == "3":
            shape_id = input("enter shape id: ")
            c1.update_shape(shape_id)

            c1.update_shape(c1)
        if chois =="4":
            num_shape = input("enter num shape")
            c1.delete_shape(num_shape)
        if chois =="5":
            break







if __name__=="__main__":
    main(c1)


