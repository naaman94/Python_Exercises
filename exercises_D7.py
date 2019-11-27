
import numpy as np
import matplotlib.pyplot as plt

print("""\nExercises 1\n """)
"""****************************************************************************************"""
z0= np.zeros( (1,10) )
print (z0)

z1= np.ones( (1,10) , dtype=np.int16 )
print (z1)

z2= np.ones( (1,10) , dtype=np.int16 )*5
print (z2)

print("""\nExercises 2\n """)
"""****************************************************************************************"""

a = np.arange(30,70)
print(a)

print("""\nExercises 3\n """)
"""****************************************************************************************"""

b = np.arange(30,70,2)
print(b)

print("""\nExercises 4\n """)
"""****************************************************************************************"""

c = np.identity(3)
print(c)


print("""\nExercises 5\n """)
"""****************************************************************************************"""

d =np.random.random_sample()
print(d)

print("""\nExercises 6\n """)
"""****************************************************************************************"""
m = np.arange(12).reshape(3, 4)
for x in m:
    for y in x:
        print(y)


print("""\nExercises 7\n """)
"""****************************************************************************************"""
e = np.arange(1,20)
for i,x in enumerate(e):
    if (x>=9 and x<15) :
        e[i]=x*-1
        print(x)
print(e)

print("""\nExercises 8\n """)
"""****************************************************************************************"""

f1=[1,8,3,5]
f2=np.random.randint(0,11,4)

print (f1*f2)

print("""\nExercises 9\n """)
"""****************************************************************************************"""
g=np.array([[3,7,2,1,8,7,19,15],[10,2,7,4,5,5,9,1]])
g1=g.shape
print ("number of row:",g1[0],"\nnumber of Col:",g1[1])

print("""\nExercises 10\n """)
"""****************************************************************************************"""
h = np.random.random((3,3,3))
print(h)

print("""\nExercises 11\n """)
"""****************************************************************************************"""

a=np.array([9,-1,2,5])
b=np.array([1,-6,0,10])
c=np.array([[1,8,2,5],[3,1,7,9]])

print("a-b: ",a-b)
print("a*b: ",a*b)
print("a.dot(b): ",a.dot(b))
print("a*2: ",a*2)
print("np.sin(a): ",np.sin(a))
print("a<3: ",a<3)
print("a.sum(): ",a.sum())
print("a.sum(axis=0): ",a.sum(axis=0))
print("c.sum(): ",c.sum())
print("c.sum(axis=0): ",c.sum(axis=0))
print("a.min(): ",a.min())
print("a.max(): ",a.max())
print("a.mean(): ",a.mean())
print("a average(): ",np.average(a))
print("a median(): ",np.median(a))
print("a std(): ",np.std(a))
print("a var(): ",np.var(a))
print("c.cumsum(): ",c.cumsum())
print("a[1:2] : ",a[1:2])
print("a[2:] : ",a[2:])
print("c[-1] : ",c[-1])

print("""\nExercises 12\n """)
"""****************************************************************************************"""
x=range(1,50)
y=[value *3 for value in x]
plt.plot(x,y )
plt.title("Draw a line")
plt.ylabel('Y Axix')
plt.xlabel('X Axix')
plt.show()


print("""\nExercises 13\n """)
"""****************************************************************************************"""
"""
x=np.arange(10,30,0.1)
x1=[10,20,30]
y1=[20,40,1]

x2=[10,20,30]
y2=[40,10,30]
plt.plot(x1,y1, label = r"line 1" )
plt.plot(x2,y2 , label = r"line 2" )


plt.title("Two or more lins on same plot with suitable legends")
plt.ylabel('Y Axix')
plt.xlabel('X Axix')
plt.legend(loc='upper right')
plt.show
"""

print("""\nExercises 14\n """)
"""****************************************************************************************"""
'''
t=np.arange(0.,5.,0.2)
t2=t**2
t3=t**3
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3,'g^')
plt.show
'''

print("""\nExercises 15\n """)
"""****************************************************************************************"""

x=["Python","Java","PHP","JavaScript","c#","C++"]
y_pos = np.arange(len(x))
popularity=[22.2,17.6,8.8,8,7.7,6.7]

plt.bar(y_pos, popularity,color=['black', 'red', 'green', 'blue', 'cyan'])
plt.xticks(y_pos, x)
plt.ylabel('Usage')
plt.title('Programming language usage')
plt.show()







