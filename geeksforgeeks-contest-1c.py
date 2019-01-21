{
#Initial Template for Python 3

import math
    
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        a=int(input())
        b=int(input())
        print(nearestPower(a,b))
        testcases-=1
        
if __name__=='__main__':
    main()
}

    
def nearestPower(a,b):
    if a==b:
      return a;
    else:
      x=[]
      for p in range (2,1000):
         x=a**p;
          if(x==b):
              return x;
           else:
              if(b-x<=b//2):
                  return x;
               
