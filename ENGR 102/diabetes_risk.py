import math

def normalizeSex(sex):
    #if sex is female assign the weight .879 else assign 0
    if sex == 'F':
        
        weight = .879
        
    else:
        
        weight = 0
        
    return weight

def normalizeAge(age):
    # age is just a raw number in the calculation so return age
    return age

def normalizeBMI(bmi):
    #based on age it assigns a weight to return when the function is called 
    if bmi < 25:
        
        weight = 0.0
        
    elif bmi >= 25 and bmi <= 27.49:
        
        weight = 0.699
        
    elif bmi >= 27.5 and bmi <= 29.99:
        
        weight = 1.97
        
    elif bmi >= 30.0:
        
        weight = 2.518
        
    return weight






sexInput = input("Enter your sex (M/F):") 
ageInput = input("Enter your age (years):") 
BMIInput = input("Enter your BMI: 26")
hypertensionInput = input("Are you on medication for hypertension (Y/N)?") 
steroidsInput = input("Are you on steroids (Y/N)?") 
cigarettesInput = input("Do you smoke cigarettes (Y/N)?") 
smokePastInput = input("Did you used to smoke (Y/N)?") 
diabetesInput = input("Do you have a family history of diabetes (Y/N)?") 

