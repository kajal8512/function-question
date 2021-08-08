'''def check_numbers():
    if num%2==0:
        print("even")
    else:
        print("not even")
num=int(input("enter the no."))
num=int(input("enter the no"))
check_numbers()'''

def check_number_list():
    i=0
    while i<len(list1):
        if list1[i]%2==0:
            if list2[i]%2==0:
                print("even")
            else:
                print("not even")
        else:
            print("no even no.")
        i+=1
list1=[2, 6, 18, 10, 3, 75]
list2=[6, 19, 24, 12, 3, 87]
check_number_list()
