# Write a function middle(L) which takes a list L as its argument, and returns the item in the middle position of L. (In order that the middle is well-defined, you should assume that L has odd length.) For example, calling middle([8, 0, 100, 12, 1]) should return 100, since it is positioned exactly in the middle of the list.

def middle(L):
    return L[len(L) // 2]


print(middle([8, 0, 100, 12, 1]))
