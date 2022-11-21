n=int(input())
w=''
while n>0:
  b=n%3
  n=n//3
  w+=str(b)
print(w)
