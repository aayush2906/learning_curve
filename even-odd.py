'''
The task is to complete the function checkEvenOdd(), which returns True (In python, True starts with caps T) if the number is even, else return False (In Python, False starts with caps F)
'''

{
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        x = int(input())
        
        if(checkOddEven(x)):
            print ("Even")
        else:
            print ("Odd")
        
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
}

def checkOddEven(x):
    if(x % 2 == 0):
      # Complete the statement below
      return 1
    else:
        # Complete the statement below
        return 0
