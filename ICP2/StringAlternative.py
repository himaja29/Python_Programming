str = input("Enter String : ")
def stringAlternative(str):
    temp = ""
    for i in range(len(str)):
        if(i%2)==0:
            temp = temp+str[i]
    print(temp)

stringAlternative(str)