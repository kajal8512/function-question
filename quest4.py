'''def add_numbers(num1,num2):
    print(num1+num2)
add_numbers(4,5)'''


# def ask_question():
#     i=1
#     while i<=100:
#         print(i, "ek bar")
#         i+=1
# ask_question()


def add_numbers_list():
    list1=[20,30,40]
    list2=[50,60,70]
    i=0
    s=0
    while i<len(list1):
        s=list1[i]+list2[i]
        i+=1
        print(s)
add_numbers_list()