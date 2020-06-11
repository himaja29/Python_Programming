lbs_weight_list = []
n = int(input("Enter number of students : "))
for i in range(0,n):
    var = int(input( ))
    lbs_weight_list.append(var)

def lbsToKilograms(lbs_weight_list):
    kilogram_weight_list = []
    for i in lbs_weight_list:
        temp = round(i / 2.2, 2)
        kilogram_weight_list.append(temp)
        temp = 0
    print(kilogram_weight_list)

lbsToKilograms(lbs_weight_list)