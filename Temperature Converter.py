def User_Info():
    sUser_name = input("Welcome to Ian's Temperature Converter Please enter your name: ")

    while True:
        temp_input = input(f"Welcome {sUser_name}! What is the current temperature?(F/C): ")
        iUnit = temp_input[-1].upper()

        if iUnit in['F', 'C']:
            try:
                iUser_temp = float(temp_input[:-1])
        
                if iUnit == 'F':
                    if iUser_temp > 212:
                        print("Error: Temp can not be greater than 212F")
                        break
                
                    iCelsius_temp = (5.0/9) * (iUser_temp-32)
                    print(f"The Celsius equivalent is: {iCelsius_temp:.1f}")
                    break

                elif iUnit == 'C':
                    if iUser_temp > 100:
                        print("Error: Temp can not be greater than 100C")
                        break

                    iFahrenheit_temp = ((9.0/5.0)*(iUser_temp)+32)
                    print(f"The Fahrenheit equivalent is: {iFahrenheit_temp:.1f}")
                    break

            except ValueError:
                print("Error: Please enter a valid number for the temperature (e.g., 100F or 37C.")

        else:
            print("Error: The temperature must include either 'F' or 'C'.")
    
def End():
    input("Thank you for using Ian's Temperature Converter, Press 'enter' to exit")

User_Info()
End()
