def find_diff(lst1,lst2):
    # l1=lst1
    # l2=lst2
    for i in lst1[:]:
        # print(i)
        if i in lst2:
            # print(i)
            lst1.remove(i)
            # print(l1)
            lst2.remove(i)
    return lst1+lst2
r=find_diff(list(input("Name 1 :")),list(input("Name 2 :")))
lst_flames=list("FLAMES")
print(lst_flames[len(r)%6])