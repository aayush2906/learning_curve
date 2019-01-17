n=int(input("Enter number of rows::"))
for i in range(1,n):
    for j in range(1,n):
      if j<=i:
          print(j,end="")
      else:
          print(" ",end="")
    print()
    
    
    '''
1
12
123
1234
12345
'''
