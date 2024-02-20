#problem1
"""
a,b=map(int,input().split())
print(a if a>b else b)
"""
#problem2
"""
a,b,c=map(int,input().split())
print(a if a>b and a>c else (b if b>a and b>c else c))
"""
#problem3
"""
a,b,c=map(int,input().split())
f,s=0,0
if a>b:
    f,s=a,b
else:
    f,s=b,a
print(c if c<f and c>s else (f if c>f else s))
"""
#problem4
"""
a,b=map(int,input().split())
print("a < b" if a<b else ("a == b" if a==b else "a > b"))
"""
#problem5 valid traingle
"""
a,b,c=map(int,input().split())
print("Yes" if (a<b+c) and (b<a+c) and (c<a+b) else "No")
"""
#problem6 apples
"""
a,b=map(int,input().split())
print(b-(a*(b//a)))
"""
#problem7 reversing an int
"""
n=int(input())
ans,c=0,0
if n<0:
    c+=1
    n=abs(n)
while n>0:
    r=n%10
    ans=ans*10+r
    n//=10
print(-1*ans if c==1 else ans)
"""
"""
n=int(input())
if n<0:
    n=abs(n)
    n=str(n)
    print("-",int(n[::-1]),sep="")
else:
    n=str(n)
    print(int(n[::-1]))
"""
#problem8 watermelon
"""
w=int(input())
print("YES" if w>2 and w%2==0 else "NO")
"""
#problem9 codechef sum fever
"""
for _ in range(int(input())):
    t=int(input())
    print("YES" if t>98 else "NO")
"""
#problem10
"""
for _ in range(int(input())):
    t=int(input())
    print(100-t)
"""
#problem11 codechef
"""
for _ in range(int(input())):
    n,x=map(int,input().split())
    if n<x or n==x:
        print(0)
    else:
        ans=n-x
        if ans%4==0:
            print(ans//4)
        else:
            print((ans//4)+1)
"""
#problem12
