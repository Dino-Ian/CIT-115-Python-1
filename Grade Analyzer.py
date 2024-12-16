import sys

def main():
 s_Username = input("Please enter your name: ")
# try block for receiving input of test scores and giving them a value error if score is below 0 before ending the script.
 try:
     i_Test1 = int(input("Test 1: "))
     i_Test2 = int(input("Test 2: "))
     i_Test3 = int(input("Test 3: "))
     i_Test4 = int(input("Test 4: "))
 except ValueError:
         print("Test scores must be greater than 0.")
         sys.exit()

 if i_Test1 < 0 or i_Test2 < 0 or i_Test3 < 0 or i_Test4 < 0:
     print("Test scores must be greater than 0.")
     sys.exit()

 drop = input("Do you wish to drop the lowest grade Y or N? ").upper()
#Ends script if anything other rhan Y or N inputted.
 if drop not in ['Y', 'N']:
     print("Enter Y or N to drop the lowest grade")
     sys.exit()
 #If Y is inputted to drop lowest test score, the test with the lowest score is removed from the equaltion and the remaining scores are added and divided by 3.
 if drop == 'Y':
     if i_Test1 <= i_Test2 and i_Test1 <= i_Test3 and i_Test1 <= i_Test4:
         #Drops i_Test1
         average = (i_Test2 + i_Test3 + i_Test4) / 3

     elif i_Test2 <= i_Test1 and i_Test2 <= i_Test3 and i_Test2 <= i_Test4:
         #Drops i_Test2
         average = (i_Test1 + i_Test3 + i_Test4) / 3
         
     elif i_Test3 <= i_Test1 and i_Test3 <= i_Test2 and i_Test3 <= i_Test4:
         #Drops i_Test3
         average = (i_Test1 + i_Test2 + i_Test4) / 3
         
     elif i_Test4 <= i_Test1 and i_Test4 <= i_Test2 and i_Test4 <= i_Test3:
         #Drops i_Test4
         average = (i_Test1 + i_Test2 + i_Test3) / 3
     print(f"{s_Username} test average is: {average:.1f}")
#If N is inputted no score is dropped and all 4 scores are added up and divided by 4.
 else:
     average = (i_Test1 + i_Test2 + i_Test3+ i_Test4) / 4
     print(f"{s_Username} test average is: {average:.1f}")
#The average is given a letter grade depending on the values it falls between. 
 if average >= 97.0:
     grade = "A+"

 elif 94.0 <= average <= 96.9:
     grade = "A"

 elif 90.0 <= average <= 93.9:
     grade = "A-"

 elif 87.0 <= average <= 89.9:
     grade = "B+"

 elif 84.0 <= average <= 86.0:
     grade = "B"

 elif 80.0 <= average <= 83.9:
        grade = "B-"

 elif 77.0 <= average <= 79.9:
        grade = "C+"

 elif 74.0 <= average <= 76.9:
        grade = "C"

 elif 70.0 <= average <= 73.9:
        grade = "C-"

 elif 67.0 <= average <= 69.9:
        grade = "D+"

 elif 64.0 <= average <= 66.9:
        grade = "D"

 elif 60.0 <= average <= 63.9:
        grade = "D-"

 else:
     grade = "F"
 print(f"Letter Grade for the test is: {grade}")
     
 input("Press 'enter' to exit")

main()

    
