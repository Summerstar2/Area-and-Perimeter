def Continue():
    Again=str(input("Would you like to use this program again? (Yes/No) "))
    if Again=="No":
        return False
    return True
print ("Welcome to this program where you can choose a variety of shapes and get their Area and Perimeter.")
Use=str(input("Would you like to use this program? (Yes/No) "))
if Use=="No":
    quit()
if Use=="Yes":
    while True:
        Shape=str(input("Shapes:\n1)Square\n2)Rectangle\n3)Triangle\n4)Parallelogram\nEnter the name of the shape you want to use - "))
        if Shape=="Square":
            Side=int(input("Enter the length of the side of Square - "))
            Area_ofSquare=Side**2
            Perimeter_ofSquare=4*Side
            Show=str(input("What would you like to see? (Area/Perimeter) "))
            if Show=="Area":
                print ("The Area of the Square is ",Area_ofSquare)
            if Show=="Perimeter":
                print ("The Perimeter of the Square is ",Perimeter_ofSquare)
                Show_again=str(input("Do you want to see the other output? (Yes/No) "))
                if Show_again=="No":
                    print ("Thanks for using this program!")
                    quit()
                if Show_again=="Yes":
                    Show=str(input("What would you like to see? (Area/Perimeter) "))
                    if Show=="Area":
                        print ("The Area of the Square is ",Area_ofSquare)
                    if Show=="Perimeter":
                        print ("The Perimeter of the Square is ",Perimeter_ofSquare)
        elif Shape=="Rectangle":
            Length=int(input("Enter length of Rectangle - "))
            Breadth=int(input("Enter breadth of Rectangle - "))
            Area_ofRectangle=Length*Breadth
            Perimeter_ofRectangle=2*(Length+Breadth)
            Show=str(input("What would you like to see? (Area/Perimeter) "))
            if Show=="Area":
                print ("The Area of the Rectangle is ",Area_ofRectangle)
            if Show=="Perimeter":
                print ("The Perimeter of the Rectangle is ",Perimeter_ofRectangle)
                Show_again=str(input("Do you want to see the other output? (Yes/No) "))
                if Show_again=="No":
                    print ("Thanks for using this program!")
                    quit()
                if Show_again=="Yes":
                    Show=str(input("What would you like to see? (Area/Perimeter) "))
                    if Show=="Area":
                        print ("The Area of the Rectangle is ",Area_ofRectangle)
                    if Show=="Perimeter":
                        print ("The Perimeter of the Rectangle is ",Perimeter_ofRectangle)
        elif Shape=="Triangle":
            Type=str(input("Is the traingle an\n1)Isoceles\n2)Right Angled\n3)Equilateral\nEnter the type - "))
            if Type=="Isoceles":
                Height=int(input("Enter the height of the traingle - "))
                Side=int(input("Enter the length of 1 side - "))
                Base=int(input("Enter the base of the triangle - "))
                Perimeter_ofTriangle=2*(Side)+Base
                Area_ofTriangle=1/2*Base*Height
                Show=str(input("What would you like to see? (Area/Perimeter) "))
                if Show=="Area":
                    print ("The Area of the triangle is ",Area_ofTriangle)
                if Show=="Perimeter":
                    print ("The Perimeter of the triangle is ",Perimeter_ofTriangle)
                    Show_again=str(input("Do you want to see the other output? (Yes/No) "))
                    if Show_again=="No":
                        print ("Thanks for using this program!")
                        quit()
                    if Show_again=="Yes":
                        Show=str(input("What would you like to see? (Area/Perimeter) "))
                    if Show=="Area":
                        print ("The Area of the triangle is ",Area_ofTriangle)
                    if Show=="Perimeter":
                        print ("The Perimeter of the triangle is ",Perimeter_ofTriangle)
            if Type=="Right Angled":
                Height=int(input("Enter the height of the triangle - "))
                Base=int(input("Enter the base of the traingle - "))
                Hypotenuse=int(input("Enter the hypotenuse of the traingle - "))
                Perimeter_ofTriangle=Height+Base+Hypotenuse
                Area_ofTriangle=1/2*Base*Height
                Show=str(input("What would you like to see? (Area/Perimeter) "))
                if Show=="Area":
                    print ("The Area of the triangle is ",Area_ofTriangle)
                if Show=="Perimeter":
                    print ("The Perimeter of the triangle is ",Perimeter_ofTriangle)
                    Show_again=str(input("Do you want to see the other output? (Yes/No) "))
                    if Show_again=="No":
                        print ("Thanks for using this program!")
                        quit()
                    if Show_again=="Yes":
                        Show=str(input("What would you like to see? (Area/Perimeter) "))
                        if Show=="Area":
                            print ("The Area of the triangle is ",Area_ofTriangle)
                        if Show=="Perimeter":
                            print ("The Perimeter of the triangle is ",Perimeter_ofTriangle)
            if Type=="Equilateral":
                Base=int(input("Enter the base of the triangle - "))
                Height=int(input("Enter the height of the triangle - "))
                Area_ofTriangle=1/2*Base*Height
                Perimeter_ofTriangle=3*Base
                Show=str(input("What would you like to see? (Area/Perimeter) "))
                if Show=="Area":
                    print ("The Area of the triangle is ",Area_ofTriangle)
                if Show=="Perimeter":
                    print ("The Perimeter of the triangle is ",Perimeter_ofTriangle)
                    Show_again=str(input("Do you want to see the other output? (Yes/No) "))
                    if Show_again=="No":
                        print ("Thanks for using this program!")
                        quit()
                    if Show_again=="Yes":
                        Show=str(input("What would you like to see? (Area/Perimeter) "))
                        if Show=="Area":
                            print ("The Area of the triangle is ",Area_ofTriangle)
                        if Show=="Perimeter":
                            print ("The Perimeter of the triangle is ",Perimeter_ofTriangle)
        elif Shape=="Parallelogram":
            Base=int(input("Enter the length of the base - "))
            Side=int(input("Enter the length of the side - "))
            Height=int(input("Enter the height - "))
            Perimeter_ofParallelogram=(Base)*2+(Side)*2
            Area_ofParallelogram=Base*Height
            Show=str(input("What would you like to see? (Area/Perimeter) "))
            if Show=="Area":
                print ("The Area of the Parallelogram is ",Area_ofParallelogram)
            if Show=="Perimeter":
                print ("The Perimeter of the Parallelogram is ",Perimeter_ofParallelogram)
                Show_again=str(input("Do you want to see the other output? (Yes/No) "))
                if Show_again=="No":
                    print ("Thanks for using this program!")
                    quit()
                if Show_again=="Yes":
                    Show=str(input("What would you like to see? (Area/Perimeter) "))
                    if Show=="Area":
                        print ("The Area of the Parallelogram is ",Area_ofParallelogram)
                    if Show=="Perimeter":
                        print ("The Perimeter of the Parallelogram is ",Perimeter_ofParallelogram)
        if not Continue():
            break
