import math
while True:
    print("A = Temperature\n"
        "B = Geometry\n"
        "C = Nutrition\n"
        "D = Finance\n",
        "Q = Quit")
    category = str(input("Enter the Value: "))
    if category == 'A':
        while True:
            print("1 = Fahrenheit to Celsius\n"
                  "2 = Celsius to Fahrenheit\n",
                  "0 = go back")
            option = int(input("Enter the the Value: "))
            if option == 1:
                Fahrenheit = float(input("Enter the F value:  "))
                result = (Fahrenheit -32) * 5/9
                print(Fahrenheit, "F is", result, 'Celsius')
            elif option == 2:
                Celsius = float(input("Enter the value:  "))
                result =  (Celsius * 9 /5) + 35
                print(Celsius, "C is", result, 'Fahrenheit')
            elif option == 0:
                break
            else:
                print("Invalid selection. Try again")
    elif  category == 'B':
        while True:
            print("1 = Area of Circle\n"
                  "2 = Circumference of circle\n",
                  "0 = go back")
            geometry_option = int(input("Enter your selection: "))
            if geometry_option == 1:
                radius = float(input("Enter the radius: "))
                area = math.pi * radius ** 2
                print("Area of circle is:", area)
            elif geometry_option == 2:
                radius = float(input("Enter the radius:  "))
                circumference = 2 * math.pi * radius
                print("Circumference of circle is:", circumference)
            elif geometry_option == 0:
                break
            else:
                print("Invalid selection. Try again")
    elif category == 'C':
        while True:
            print("1 = Body Mass\n",
                  "0 = go back")
            nutration_option = int(input("Enter your selection: "))
            if nutration_option == 1:
                weight_kg = float(input("Enter your weight in Kilogram:   "))
                height_m = float(input("Enter your height in meters:   "))
                if height_m <= 0:
                    print("Height must be greater than 0")
                    break
                bmi = weight_kg / (height_m ** 2)
                print("Your BMI is:", bmi)
            elif nutration_option == 0:
                break
            else:
                print("Invalid selection. Try again")
    elif category == 'D':
        while True:
            print("1 = Interest\n",
                  "0 = go back")
            finance_option = int(input("Enter your selection: "))
            if finance_option == 1:
                amount = float(input("Enter the amount:    "))
                annual_rate = float(input("Enter the annual interest rate:   "))
                time_years = float(input("Enter the time in years:   "))
                interest = amount * (annual_rate /100) * time_years
                print("Interest", interest)
            elif finance_option == 0:
                break
            else:
                print("Invalid selection. Try again")
    elif category == 'Q':
        print("Exiting, Goodbye!")
        break
    else:
        print("Invalid category. Please enter A, B, C or Q")





