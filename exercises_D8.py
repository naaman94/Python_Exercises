import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

print("""\nExercises 1\n """)
"""****************************************************************************************"""
data = [2,4,6,8,10]
s = pd.Series(data)
print(s)

print()
print("""\nExercises 2\n """)
"""****************************************************************************************"""
d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
ds=pd.Series(d1)
print(ds)
print()

print("""\nExercises 3\n """)
"""****************************************************************************************"""
data = [20, 10, 150, 110, 100, 50]
ds=pd.Series(data)

ds.plot.bar(color=['red', 'black', 'green', 'blue','yellow', 'cyan']);
plt.show();


print()
print("""\nExercises 4\n """)
"""****************************************************************************************"""

Data = {'d1':[100,200,5,400,700,100,200,50,400,700],'d2':[140,0,300,400,200,140,0,700,400,200]}
df =pd.DataFrame(Data)
print( df.describe())
df.plot()

print()
print("""\nExercises 5\n """)
"""****************************************************************************************"""
data1= {'X':[78,85,96,80,86],
              'Y':[84,94,89,83,86],
              'Z':[86,97,96,72,83]}
df =pd.DataFrame(data1)
print (df)


print()
print("""\nExercises 6\n """)
"""****************************************************************************************"""

# =============================================================================
# 
# BabyDataSet = list(zip(names,births))
# df = pd.DataFrame(data = BabyDataSet,
# columns=['Names', 'Births'])
# print(df)
# df.plot.pie(y='birth', figsize=(5, 5))
# =============================================================================
births = [968, 155, 77, 578, 973]
names = ['Bob','Jessica','Mary','John','Mel']

df = pd.DataFrame({'births': births,'names':names})
plot = df.plot.pie(y='births', figsize=(5, 5))


print()
print("""\nExercises 7\n """)
"""****************************************************************************************"""
# =============================================================================
# df =pd.read_csv('d8.csv',sep='\t',index_col=0)
# print (df)
# df.to_csv('d8After.csv', sep=',')
# 
# =============================================================================

print()
print("""\nExercises 8\n """)
"""****************************************************************************************"""

dates=pd.date_range('20000101',periods=4)
df = pd.DataFrame(np.random.randn(4, 2), index=dates, columns=['A','B'])

print (df)
print (df.head(2))
print (df[['A']])
print (df[0:1])
print (df['20000102':'20000104'])
print(df.loc['20000102':'20000104', ['A']])
print(df.iloc[:, 1:2])
print(df[df> 0])
print(df[df.B> 0])
df['A'] = [100,200,300,100]
print (df)
print(df[df['A'].isin([200, 300])])








