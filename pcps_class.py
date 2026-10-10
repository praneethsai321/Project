# a=list()
# n=int(input('enter no of elements: '))
# for i in range(n):
#     d=int(input('enter element'))
#     a.append(d)
#     print(a)
# print(a)

# l=[23,45,2,11]
# t=[]
# f=[]
# for num in l:
#     t.append(num**2)
#     f.append(num**0.5)
# print(t,f)

# def find_even(list):
#     for el in list:
#         if el%2==0:
#             return el
#     else:
#         return 'no even n.o exists'

# l=[11,15,34,55,33]
# print(find_even(l))

# l=[23,45,32,32]
# t=[]
# n=int(input('enter a number'))
# for el in l:
#     el=el+n
#     t.append(el)

# k=[12,23,345,38,38]
# t=[]
# for i in range(len(k)-1):
#     s=abs(k[i]-k[i+1])
#     t.append(s)
# print(t)

# t=[]
# for i in range(1,21):
#     if i%4!=0 :
#         t.append(i)

# print(t)

t1=[1,22,33,22,12,12,1]
t2=[]
p=set(t1)
for el in p:
    t2.append(el)
print(t2)