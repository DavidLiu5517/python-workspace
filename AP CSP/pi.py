import random
count=0
totle=int(input('輸入次數'))
 
for i in range(totle):
  Xrandresult=random.uniform(0,1)
  Yrandresult=random.uniform(0,1)
  if (Xrandresult**2 + Yrandresult**2 <=1):
    count=count+1
    
pii=((count/totle)*4)
print (pii)