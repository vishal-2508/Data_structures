
"""
							# make pop method
def pop_method(num_list):
    items = ""
    for i in range((len(num_list)-1)):
        if(i==0):
            items = str(num_list[i])
        else:
            items = items + "," + str(num_list[i])
    print("the list items in string formet : ", items)
    return items.split(",")

number = input("Enter items of list with comma : ").split(",")
#a = pop_method(number)
#print(a)
number = pop_method(number)
print("after pop method list : ",number)
"""

"""
							#make append method
def append_method(number,m):
    items = ""
    for i in range((len(number)+1)):
        if(i==0):
            items = str(number[i])
        elif(i<len(number)):
            items = items + "," + str(number[i])
        else:
            items = items + "," + str(m)
    print("the list items in string formet : ", items)
    return items.split(",")

num = input("Enter items of list with comma : ").split(",")
new_number = input("Enter that number which number you want to append : ")
number = append_method(num,new_number)
print("after append method list : ",number)
"""


							#implimentetion of stack using array--> insirt and delition of eliment in the list.
top = -1
list_size = int(input("Enter size of array : "))
print("[1] Remove elenemt \n[2] Add element \n[3] Quit")
while True:
    num = int(input("Enter your choice :  "))
    if(num==1):
        if(top==-1):
            print("stack is underflow.")
        else:
            top -= 1
            print("pop else part | ", top)
    elif(num==2):
        if(top==(list_size-1)):
            print("stack is overflow.")
        else:
            top += 1
            print("append else part | ",top)
    else:
        break










def fun():
    print("sima")
print("hello vishal singh")



def final():
    print("this is second time fun : ")
