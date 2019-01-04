""" print 1 2 3 4
          2 3 4
          3 4
          4           """
for i in range(4):
    for j in range(4-i):
        print(j+i+1, end = "")
    print()


""" print APQR
          ABQR
          ABCR
          ABCD   """

list1 = "APQR"
list2 = "ABCD"
for i in range(4):
        print(list2[:i+1], end = "")
        print(list1[i+1:])
