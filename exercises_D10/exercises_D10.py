

print("""\nExercises 1\n """)
"""****************************************************************************************"""
import sympy as sym
x ,i,y,z= sym.symbols('x i y z')
expr = x**2 + x**3+21*x**4+1
print (expr.subs(x, 7) )
print(  "b :", sym.expand( (x + y) ** 2 ))
print( "c :", sym.simplify((4*x**3 + 21*x**2 + 10*x+12)))
print(  "d :", sym.limit(1/(x**2),x,sym.oo))
print(  "e :",sym.summation(2*i + i - 1, (i, 5, n)))
print(  "f :",sym.integrate(sym.sin(x)+sym.exp(x)*sym.cos(x)+sym.tan(x) , x))
print(  "g :",sym.factor(x**3 +12*x*y*z+3*y**2*z))
print(  "h :",sym.solveset(x-4,x))
print(  "i :",sym.Matrix([[5, 12, 40], [30, 70, 2]]) * sym.Matrix([2, 1, 0]))
print(  "j :")
from sympy import symbols
from sympy.plotting import plot
x = symbols('x')
plot(x**3+3, (x, -10, 10))

print(  "k :")
from sympy.plotting import plot3d
x, y = symbols('x y')
f=x**2*y**3
plot3d(f, (x, -6, 6), (y, -6, 6))



print()
print("""\nExercises 2\n """)
"""****************************************************************************************"""

import xlsxwriter
workbook = xlsxwriter.Workbook('D10.xlsx')
worksheet = workbook.add_worksheet()
data=['This is Example','My fist export example',1,2,3]
format1=workbook.add_format({'bold':True, 'font_color':'red','font_size':20})
format2=workbook.add_format({'font_size':20})
worksheet.set_column('A:A', 20)
worksheet.write('A1', data[0],format1)
worksheet.write('A2', data[1], format2)
for x in range(2):
    worksheet.write(x+2, 0, x+1)
worksheet.write('A5', data[4],format1)
workbook.close()

print()
print("""\nExercises 3\n """)
"""****************************************************************************************"""

from xlrd import open_workbook
wb = open_workbook('D10_read.xlsx')

for s in wb.sheets():
    print ("Sheet:", s.name)
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print(values)
    print()


















