
#Asending order

num = input("Enter element of list for Asending order with comma : ").split(",")
print("List before exiquation : " ,num , "\n")
for j in range(1,len(num)):
    temp = num[j]
    i = j-1
    while(i>=0):

        if(int(num[i]) > int(temp)):
            num[i+1] = num[i]
            if(i==0):
                num[i] = temp
        else:
            num[i+1] = temp
            break
        i -= 1
print("List after exiquation : " ,num , "\n")



#Disending order

num = input("Enter element of list Disending order with comma : ").split(",")
print("List before exiquation : " ,num , "\n")
for j in range(1,len(num)):
    temp = num[j]
    i = j-1
    while(i>=0):

        if(int(num[i]) < int(temp)):
            num[i+1] = num[i]
            if(i==0):
                num[i] = temp
        else:
            num[i+1] = temp
            break
        i -= 1
print("List after exiquation : " ,num , "\n")
