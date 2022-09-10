"sort()"
# a=[1,5,9,2,3,10]
# a.sort()
# print(a)
# "or"
# print(sorted([6,5,7,2,4,]))

"all()"

# print(all([True,1,2,]))
# print(all([True,"",1,2,]))
# print(all([True," ",1,2,]))
# print(all([True,1,2,False]))
# print(all([True,1,2,None]))
# print(all([True,1,2,0]))


"any()"
# print(all([True,True,1,2,3]))
# print(all([False,False," "]))
# print(all([False,""]))
# print(all([True,False,1,2]))

"bool()"
# print(bool(False)) #False
# print(bool(1)) #True
# print(bool(bool)) #True
# print(bool(True)) #True
# print(bool(0)) #False
# print(bool(None))#False
# print(bool(""))#False
# print(bool(" "))#True

"eval()"
# a=eval("5+6.8-1")
# print(a)
# a=eval("10+5-3")
# b=("10-9.7")
# print(a,type(a))
# print(b,type(b))

"sum()"
# print(sum([1,2,3,4,5]))
# print("sum=",sum([10,20,3,9]))

"reverse()-list"
# for i in reversed([1,2,3,4,5,6,7,8,9]):
#     print(i)

"reverse()-tuple"
# for i in reversed((9,8,7,5,4,3,2,1)):
#     print(i)

"enumerate()"
# a=["rohan","Mohan","johan"]
# b=enumerate(a)
# print(list(b))
# print(tuple(b))
# print(dict(b))

a=["rohan","Mohan","johan"]
b=enumerate(a,-1)
print(list(b))
a=["rohan","Mohan","johan"]
b=enumerate(a,-1)
print(set(b))
a=["rohan","Mohan","johan"]
b=enumerate(a,-1)
print(tuple(b))
a=["rohan","Mohan","johan"]
b=enumerate(a,-1)
print(dict(b))
