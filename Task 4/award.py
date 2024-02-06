#Enter the users qualifying time for each event
print ("Please note overall qualifying time for awards will be 110 mins and less")
# This print statment will assume the user will only input a positive number 
print("Note negative numbers and characters wil not be excepted") 
print()

# The user will be asked to input their finishing times for each catagory, if they enter a negative the code will give an error and end
running = int(input ("Enter your finished running time in minutes: "))
if running < 0 :
    print ("Please start again and enter a valid time")
    exit()

    
swimming = int(input ("Enter your finished swimming time in minutes: "))
if swimming < 0:
    print ("Please start again and enter a valid time")
    exit()
        
cycling = int(input ("Enter your finished cycling time in minutes: "))
if cycling < 0:
    print ("Please start again and enter a valid time")
    exit()

#Print the total time by addding all three times together
qual_time = running + swimming + cycling
print ("Total time to complete triathlon", qual_time,"minutes")
print()


# Set the qualifying criteria and print the type of award to be presented
if qual_time <101 and qual_time >0: # Award time will be equal to and between 0mins & 100mins
    print ("You hav been awarded Provincial Colours")
elif qual_time < 106 and qual_time > 100: # Award time will be equal to and between 101mins & 105mins
    print ("You hav been awarded Provincial Half Colours")
elif qual_time >= 106 and qual_time <= 110: # Award time will be equal to and between 105mins & 110mins
    print ("You hav been awarded Provincial Scroll")
else:
    print ("You recieve no award")
                