# Lists: ordered, mutable, allows duplicate elements

# Be careful when copy a list
list_org = ["banana", "cherry", "apple"]

# list_cpy = list_org # wrong! when list_cpy changes, list_org also changes
# following methods
list_cpy = list_org.copy()
list_cpy = list(list_org)
list_cpy = list_org[:]

list_cpy.append("lemon")

print(list_cpy)
print(list_org)

# advanced trick
mylist = [1, 2, 3, 4, 5, 6]
b = [i*i for i in mylist]

print(mylist)
print(b)
