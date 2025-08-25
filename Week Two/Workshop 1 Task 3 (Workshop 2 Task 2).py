print('A = Length\n', 'B = Weight\n', 'C = Volume\n', 'Q = Quit')
while True:
    Choice = str(input("Enter a Value: "))
    if Choice == 'A':
        while True:
            print("1 = Centimeter to inches\n "
                    "2 = Metre to feet\n",
                    "3 = Kilometre to miles\n",
                    "4 = inch to centimetres\n",
                    "5 = foot to metres\n",
                    "6 = mile to kilometre\n",
                    "0 = go back")
            length_option = int(input("Enter your selection: "))
            if length_option == 1:
                Centimeter = float(input("Enter the Cm Value:  "))
                result = Centimeter * 0.393
                print(Centimeter, 'cm is', result, 'inches')
            elif length_option == 2:
                Metre = float(input("Enter the m Value:  "))
                result = Metre * 3.281
                print(Metre, 'm is', result, 'feet')
            elif length_option == 3:
                Kilometre = float(input("Enter the kg value: "))
                result = Kilometre * 0.621
                print(Kilometre, 'kg is', result, 'miles')
            elif length_option == 4:
                Inch = float(input("Enter the inch value:  "))
                result = Inch * 2.54
                print(Inch, 'inch is', result, 'centimetre')
            elif length_option == 5:
                Foot = float(input("Enter the ft value:  "))
                result = Foot * 0.305
                print(Foot, 'ft is', result, 'metres')
            elif length_option == 6:
                Mile =  float(input("Enter the mile value:  "))
                result = Mile * 1.609
                print(Mile, 'mile is', result, 'kilometres')
            elif length_option == 0:
                break
            else:
                print("Invalid selection. Try again")

    elif Choice == 'B':
        print("1 = grams to ounces\n",
                "2 = kilogram to pounds\n",
                "3 = ounce to grams\n",
                "4 = pounds to kilograms\n",
                "0 = go back")
        while True:
            weight_option = int(input("Enter your: "))
            if weight_option == 1:
                Gram = float(input("Enter the Gram Value:  "))
                result = Gram * 0.035
                print(Gram, 'gram is', result, 'Ounces')
            elif weight_option == 2:
                Kilogram = float(input("Enter the Kilogram Value:  "))
                result = Kilogram * 2.204
                print(Kilogram, 'kg is', result, 'pounds')
            elif weight_option == 3:
                Ounce = float(input("Enter the Ounce Value:  "))
                result = Ounce * 28.35
                print(Ounce, 'ounces is', result, 'Grams')
            elif weight_option == 4:
                Pounds = float(input("Enter the Pounds Value:  "))
                result = Pounds * 0.454
                print(Pounds, 'pounds is', result, 'kilograms')
            elif weight_option == 0:
                break
            else:
                print("Invalid selection. Try again")

    elif Choice == 'C':
        print("1 = millilitre to fluid ounces\n",
                "2 = litre to quarts\n",
                "3 = fluid ounces to millilitres\n",
                "4 = quart to litres\n",
                "0 = go back")
        while True:
            volume_option = int(input("Enter your: "))
            if volume_option == 1:
                Millilitre = float(input("Enter your ml Value:  "))
                result = Millilitre * 0.035
                print(Millilitre, 'ml is', result, 'Fluid Ounces')
            elif volume_option == 2:
                Litre = float(input("Enter your l Value:  "))
                result = Litre * 0.878
                print(Litre, 'l is', result, 'quarts')
            elif volume_option == 3:
                Fluid_ounce = float(input("Enter your fl Value:  "))
                result = Fluid_ounce * 28.413
                print(Fluid_ounce, 'fl is', result, 'millilitres')
            elif volume_option == 4:
                Quart = float(input("Enter your quart Value:  "))
                result = Quart * 1.137
                print(Quart, 'quart is', result, 'litre')
            elif volume_option == 0:
                break
            else:
                print("Invalid selection. Try again")
    elif Choice == 'Q':
        print("Exiting the Converter. Goodbye!")
        break
    else:
        print("Invalid category. Please enter A, B, C or Q")
