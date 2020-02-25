import numpy as np
import itertools
n=int(input("Enter the degree of the polynomial:"))
c=np.zeros(n+2)

for i in range(0,n+1):
	c[i]=input("Enter the coefficient:")

print(c)

d=np.zeros([n+1,n+1])
for j in range (0,n-1):
	d[0,j]=c[2*j]
	d[1,j]=c[(2*j)+1]

for i in range(2,n+1):
	for j in range (0,n-1):
		d[i,j]= (((d[i-1,0]*d[i-2,j+1])-(d[i-1,j+1]*d[i-2,0]))/(d[i-1,0]))
	if(d[i,0]== 0):
		d[i,0]=0.00001

print(d)

x=[]
for i in range (0,n+1):
	x.append(d[i,0])

k=(len(list(itertools.groupby(x, lambda x: x > 0)))-1)
if k==0:
	print("The polynomial has zero poles on right half of s plane")
else:
	print("The no of poles of polynomial on right half of s plane is:",k) 
	
