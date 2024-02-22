#problem1 factorial
"""
def fact(n): return (1 if n<=1 else n*fact(n-1))
print(fact(5))
"""
#problem2 codechef Sugarcane Juice Business
"""
def profit(x):
    x*=0.3
    return int(x*50)
def tc(t):
    if t==0:
        return
    print(profit(int(input())))
    tc(t-1)
tc(int(input()))
"""
#problem3 codechef movies2x
"""
def movie(x,y):
    print (x-y//2)
x,y=map(int,input().split())
movie(x,y)
"""
#problem4
"""
n=int(input())
x=n
c=0
while n!=0:
    n//=10
    c+=1
x+=3*(10**c)
x=x*10+3
print(x)
"""
#problem5
"""
n=int(input())
s=0
while n!=0:
    r=n%10
    s=s*10+r
    n//=10
print(s*10 +3)
"""
