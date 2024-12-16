#Function to return float input from user
def getFloatInput(prompt):
    while True:
        try:
            user_input = float(input(prompt))

            if user_input > 0:
                return user_input
            else:
                print("Error: Please enter a non-zero positive value.:")

        except ValueError:
            print("Error: Please enter a valid number.")

#Function to calculate the median of a list
def getMedian(sales_list):
    sales_list.sort()
    n = len(sales_list)
    if n % 2 == 1:
        return sales_list[n // 2]
    else:
        mid1 = sales_list[n // 2-1]
        mid2 = sales_list[n //2]
        return (mid1 + mid2) / 2

#Main function to manage the sales data and calculations
def main():
    sales_data = []

    while True:
        sale_price = getFloatInput("Enter property sales value: ")
        sales_data.append(sale_price)

        while True:
            another = input("Enter another value Y or N: ").strip().upper()
            if another == "Y":
                break
            elif another == "N":
                break
            else:
                print("Invalid input. Please enter Y or N.")

        if another == 'N':
            break

    sales_data.sort()
    for i, value in enumerate(sales_data, start=1):
        print(f"Property {i}: ${value:,.2f}")
        
        

    min_value = sales_data[0]
    max_value = sales_data[-1]
    total_value = sum(sales_data)
    average_value = total_value / len(sales_data)
    median_value = getMedian(sales_data)
    commission_value = total_value * 0.03

    print(f"Minimum:      ${min_value:,.2f}")
    print(f"Maximum:      ${max_value:,.2f}")
    print(f"Total:        ${total_value:,.2f}")
    print(f"Average:      ${average_value:,.2f}")
    print(f"Median:       ${median_value:,.2f}")
    print(f"Commission:   ${commission_value:,.2f}")


if __name__ == "__main__":
    main()
    
            
                
    
