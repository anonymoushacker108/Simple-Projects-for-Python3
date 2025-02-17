gender = str(input("What is your gender (male|female)? "))

if (gender == "male") | (gender == "female") : 
    
    femur_length = int(input("What is your femur's length in centimeters? "))
    
    if gender == "male" :
        height = (2.32 * femur_length) + 65.53
    else:
        height = (2.47 * femur_length) + 54.1

    print ("The height of the given", gender, "is", height, "centimeters")        

else: 
        print ("Error, gender is not male or female")
        