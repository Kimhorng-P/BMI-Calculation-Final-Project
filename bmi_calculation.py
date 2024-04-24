
def bmi_calculate(weight, height):
    bmi_score = round((weight/ height **2), 1)
        
    if bmi_score < 18.5:
        result = "underweight"
        
    elif 18.5 < bmi_score < 24.5:
        result =  "normal"

    elif 25 <bmi_score < 29.9:
        result =  "overweight"

    elif 30 < bmi_score < 39.9:
        result =  "obese"

    else: 
        result = "extremely obese"

    return result, bmi_score