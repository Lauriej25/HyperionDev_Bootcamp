#Capstone Project
#The user will be calculating the amount of interest they will earn on an investment or
# the amount they will have to repay on a bond


import math
print ("investment - to calculate the amount of intrest you'll earn on your investment ")
print ("bond       - to calculate the amount you'll have to pay on a loan  ")
print()
#Starting with the amount of intrest the user will earn with either 'simple' or 'compounding' intrest rates
inves_option = input ("either 'investment' or 'bond' from the menu above to proceed: ")
if inves_option.lower() == "investment" :
    depositing = int(input("Enter the amount your depositing : $"))
    intrest_rate = float(input("Enter your intrest rate: %")) /100
    inves_years = int(input ("Enter the number of years you plan on investing: "))
    sim_com = input ("Enter if you would like 'simple' or 'compound' intrest: ")
    P = depositing 
    r = intrest_rate
    t = inves_years

#Simple intrest is -   A = P * (1 + r*t)
    if sim_com.lower () == "simple" :
        A = P * (1 + r * t)
        print ("Your simple intrest earnt will be $",(A-P))

#Compound intrest is -  A = P * math.pow((1+r),t)
    elif sim_com.lower() == "compound" :
        A = (round(P * math.pow((1+r),t),2))
        print ("Your compounded intrest earnt will be $", (A-P))


#Bond repayment formula - repayment = (i * p)/(1-(1+i)**(-n))
elif inves_option.lower() == "bond":
    house_value = int(input("Enter the present value of the house: $"))
    bond_intrest_rate = int(input("Enter your intrest rate: %"))
    repayment_months = int(input ("Enter the number of months you plan on investing: "))
        
    i = ((bond_intrest_rate / 100) / 12)
    P = house_value
    n = repayment_months
    repayment = (i * P)/(1-(1+i)**(-n))
        
    print ("Your monthly repayments will be: $", round((repayment),2))
else: 
     print ("Sorry I do not understand, try again!")
     