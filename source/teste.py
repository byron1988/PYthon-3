L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]

def remove_dups(L1, L2):
    L1_copy = L1[:]
    print(L1_copy)
    for e in L1_copy:
        if e in L2:
             L1.remove(e)
 

remove_dups(L1, L2)
print("l1", L1)
print("l2", L2)
