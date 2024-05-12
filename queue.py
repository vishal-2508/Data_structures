# your code is wrong

def fun():
    t = "local chnage"
    v =	"remote change"

						#Queue in DBMS
front = -1
rear = delete_index = -1
size = int(input("Enter size of list : "))
print("[1] Insert element \n[2] Delete element \n[3] Quit")
while True:
    #delete_index = rear
    num = int(input("Enter your choice : "))
    if(num==1):
        if(front==-1 and rear==-1):
            front += 1
            rear += 1
        elif(rear<size-1):
            rear += 1
        else:
            print("Isfull")
        print("insert element front = ", front , " , rear = " ,rear)
        delete_index = rear
    elif(num==2):
        if(front<rear):
            front += 1
        elif((front==rear and front!=-1) and delete_index==rear):
            front += 1
            rear += 1
        else:
            print("Isempty")
            print("last position of rear for delition : ",delete_index)
            front = -1
            rear = -1
        print("delete element front = ", front , " , rear = " ,rear)
    else:
        break
