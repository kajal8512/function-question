def item(a):
    def get_last_item(my_list):
        return my_list[len(a)-1]
    a.remove(get_last_item(a))
    return a
a=[1,4,5,8,9]
print(item(a))