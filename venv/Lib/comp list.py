# Python program to find the common elements in two lists
def common_member(a, b):
    a_set = set(a)
    b_set = set(b)

    if (a_set & b_set):
        print(a_set & b_set)
    else:
        print("No common elements")

a=input(print("Enter the first list"))
b=input(print("Enter the second list"))

common_member(a, b)