n=int(input("Enter the terms"))
f=0
s=1                                         
if n<=0:
  print("The requested series is",f)
else:
  print(f,s,end=" ")
  for x in range(2,n):
    sum=f+s                           
    print(sum,end=" ")
    f=s
    s=sum
