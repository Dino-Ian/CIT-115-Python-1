
# User inputs
nPV = float(input('Enter the starting principal: '))
nR = float(input('Enter the annual interest rate: '))
nM = float(input('How many times per year is the interest compounded?: '))
nT = float(input('How many years will the account earn interest?: '))

#Formula for future value
nR=nR/100
nFV=nPV*(1+nR/nM)**(nM*nT)

#Print result
int_value = int(nT)
print(f"At the end of {int(nT)} years you will have: ${nFV:,.2f}")

#input to close scrip
input("Press 'enter' to end scrip")






