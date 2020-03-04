import string
def create_phone_number(n):
    # your code here
    str_phone =""
    for num in n:
        str_phone += (str(num))
        new_Str = "("+str_phone[0:3]+") "+str_phone[3:6]+"-"+str_phone[6:10]
    print(new_Str)

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) #(123) 456-7890

