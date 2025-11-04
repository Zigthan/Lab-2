def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    BMI = weight / (height  * height)

    print("BMI = " + str(BMI))

    if BMI < 18.5:
        print ("You are underweight.")
        return -1
    elif BMI >= 18.5 and BMI < 24.9:
        print ("You are normal weight.")
        return 0
    elif BMI >=25 and BMI <29.9:
        print ("You are overweight.")
        return 1
    else: 
        print ("You are obese.")

    

calculate_bmi(weight=95, height=1.80)

