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

# t=[1,23,24,43.45,34.43,True,False,'hoollo moto','ok','hmm',False]
# t1=[];t2=[];t3=[];t4=[];
# for el in t:
#     if type(el)==int:
#         t1.append(el)
#     elif type(el)==str:
#         t2.append(el)
#     elif type(el)==float:
#         t3.append(el)
#     elif type(el)==bool:      
#         t4.append(el)
# print(t1,t2,t3,t4,sep='\n')

# t1=[1,22,33,22,12,12,1]
# t2=[]
# p=set(t1)
# for el in p:
#     t2.append(el)
# print(t2)  

# def greatest_lmost(list):
#     l=len(list)
#     for i in range(l):
#         count=0
#         for j in range(l):
#             if list[i]>list[j]:
#                 count+=1
#         if count==l-1:
#             return list[i]
        
# t=[23,22,11,2313,4232,1212]
# print(greatest_lmost(t))


# n=int(input('enter a number'))
# t=[]
# for i in range(1,n+1):
#     if i!=n//2:
#         t.append(i)
# print(t)

# n=int(input('enter you lucky number: '))
# t1=[]
# t2=[]
# t3=[]
# for i in range(1,n+1):
#     t1.append(i)
#     t2.append(i**2)
#     t3.append(i**3)
# T=[t1,t2,t3]
# print(T)

# n=int(input('enter you lucky number: '))
# num=0
# for i in range(1,n+1):
#     num+=i*(i+1)
# print(num)

# from statistics import mean
# L=[2,34,43,23]
# print(mean(L))

# n=int(input('enter you lucky number: '))
# t=[]
# for i in range(1,n+1):
#     if i%2==0 and i%3!=0:
#         t.append(i)
# print(t)

# L1=[23,21,21,2];L2=[2,35,323,43,323,232]
# t=[]
# for i in range(len(L1)):
#         t.append(L1[i])
#         t.append(L2[i])
# for i in range(len(L1),len(L2)):
#     t.append(L2[i])
# print(t)

# l1=[23,11,80]
# l2=[38,89,12]
# l3=[12,32,31]
# for i in range(3):
#     for j in range(3):
#         l1[j]=l1[j]%10
#         l2[j]=l2[j]%10
#         l3[j]=l3[j]%10

# print([l1,l2,l3])