def BMIStandard(BMI):
    if BMI < 18.5:
        return "BMI 過低，體重過輕"
    elif BMI<24:
        return "BMI 正常，標準體位"
    else:
        if BMI < 27:
            return "BMI 過高，體重過重"
        elif BMI < 30:
            return "BMI 過高，輕度肥胖"
        elif BMI < 35:
            return "BMI 過高，中度肥胖"
        else:
            return "BMI 過高，重度肥胖"

weight = int(input("體重(kg): "))
height = int(input("身高(cm): "))

height = height / 100

BMI = round(weight / (height ** 2),2)

#輸出結果，呼叫分類 function
print("\nBMI 計算結果 = " + str(BMI))
print(BMIStandard(BMI))



