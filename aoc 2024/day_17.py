a,*_,p=open("input.txt")
a=int(a[12:])
p=eval(p[9:])
n=lambda a,b:b^(a>>b)^next(p[i+1]for i in(6,8,10)if p[i]==1)
k=""
while a:k+=f",{n(a,a&7^p[3])&7}";a>>=3
print(k[1:])
s=lambda a,i:i==len(p)<print(a)or[s(k,i+1)for x in range(8)if n(k:=a<<3|x,x^p[3])&7==p[~i]]
s(0,0)