from functools import *
L=*open('input.txt'),
@cache
def F(s,k,r):
 if k>r:return len(s)
 M={};i=t=0
 for v in["789456123_0A","_^A<v>"][k>0]:M[v]=i%3,i//3;i+=1
 A,B=M["_"]
 for d,c in zip("A"+s,s):x,y=M[d];X,Y=M[c];a,b=X-x,Y-y;t+=F(("<"*-a+"v"*b+"^"*-b+">"*a)[::-(X==A)*(y==B)-(Y==B)*(x==A)|1]+"A",k+1,r)
 return t
print(*(sum(int((k:=l.strip())[:-1])*F(k,0,n)for l in L)for n in(2,25)))