import math

# Function to get a valid positive float input from the user
def getFloatInput(prompt):
    while True:
        try:
            user_input = input(prompt)
            value = float(user_input)
            if value > 0:
                return value
            else:
                print("Error: The value must be positive.")
        except ValueError:
            print("Error: Invaild input. please enter a valid number.")

#Function to calculate the total gallons of paint needed based on the square footage and coverage 
def getGallonsOfPaint(fSquareFeet, fFeetPerGallon):
    gallons_needed = math.ceil(fSquareFeet / fFeetPerGallon)
    return gallons_needed

#Function to calculate the total labor hours required based on labor hours per gallon and total gallons 
def getLaborHours(fLaborHoursPerGallon, iTotalGallons):
    labor_hours = fLaborHoursPerGallon * iTotalGallons
    return labor_hours

#Function to calculate the labor cost based on labor hours and labor charge
def getLaborCost(fLaborHoursPerGallon, fLaborChargePerHour, iTotalGallons):
    labor_cost = getLaborHours(fLaborHoursPerGallon, iTotalGallons) * fLaborChargePerHour
    return labor_cost

#Function to calculate the paint cost based on the price per gallon and total gallons needed
def getPaintCost(fPaintPrice, iTotalGallons):
    paint_cost = fPaintPrice * iTotalGallons
    return paint_cost

#Function to return the appropriate sales tax rate for the state 
def getSalesTax(state):
    state_tax_rate = {
        'CA': 0.06,
        'MA': 0.0625,
        'ME': 0.085,
        'NH': 0.0,
        'RI': 0.07,
        'VT': 0.06
    }
    return state_tax_rate.get(state.upper(), 0.0)

#Function to display the cost estimate and save it to a text file
def showCostEstimate(fTotalCost, fLaborCost, fPaintCost, fSalesTax, iTotalGallons, state, last_name, fLaborHours):
    print(f"Painting Estimate for {last_name}:")
    print(f"Total Gallons of Paint Needed: {iTotalGallons}")
    print(f"Hours of Labor: {fLaborHours:.1f}")
    print(f"Paint Cost: ${fPaintCost:.2f}")
    print(f"Labor Cost: ${fLaborCost:,.2f}")
    print(f"Sales Tax: ${fSalesTax:,.2f}")
    print(f"Total Cost (Including Tax): ${fTotalCost:,.2f}")

#Create a text file to save the estimate
    file_name = f"{last_name}_PaintJobOutput.txt"
    with open(file_name, 'w') as file:
        file.write(f"painting Estimate for {last_name}:\n")
        file.write(f"Total Gallons of Paint Needed: {iTotalGallons}\n")
        file.write(f"Hours of Labor: {fLaborHours:,.1f}\n")
        file.write(f"Paint Cost: ${fPaintCost:.2f}\n")
        file.write(f"Labor Cost: ${fLaborCost:.2f}\n")
        file.write(f"Sales Tax: ${fSalesTax:.2f}\n")
        file.write(f"Total Cost (Including Tax): ${fTotalCost:.2f}\n")

    print(f"\nOutput has been saved to {file_name}")

#Main Function to gather user input and perform calculations
def main():
    fSquareFeet = getFloatInput("Enter Square Feet of the Wall: ")
    fPaintPrice = getFloatInput("Enter Paint Price per Gallon: ")
    fFeetPerGallon = getFloatInput("Enter Feet per Gallon of Paint: ")
    fLaborHoursPerGallon = getFloatInput("Enter Labor Hours Per Gallon: ")
    fLaborChargePerHour = getFloatInput("Enter Painting Labor Charge per hour: ")

    state = input("State job is in: ")
    last_name = input("Enter customer last name: ")

    #calculations
    iTotalGallons = getGallonsOfPaint(fSquareFeet, fFeetPerGallon)
    fLaborCost = getLaborCost(fLaborHoursPerGallon, fLaborChargePerHour, iTotalGallons)
    fPaintCost = getPaintCost(fPaintPrice, iTotalGallons)
    fSalesTax = getSalesTax(state) * (fLaborCost + fPaintCost)
    fTotalCost = fLaborCost + fPaintCost + fSalesTax
    fLaborHours = getLaborHours(fLaborHoursPerGallon, iTotalGallons)

    showCostEstimate(fTotalCost, fLaborCost, fPaintCost, fSalesTax, iTotalGallons, state, last_name, fLaborHours)

#Run the main function if this script is executed
if __name__ == "__main__":
    main()
        
