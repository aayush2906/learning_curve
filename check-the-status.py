'''
Given two integer variables a and b, and a flag which is boolean. The task is to check the status and return accordingly.
Return "True" if either a or b (one of them) is positive. Except if the flag is True, then return True only if both of the variables a and b are negative.
'''
{

def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        a = int(input())
        b = int(input())
        flag = input()
        
        if(flag == "True"):
            flag = True
        else:
            flag = False
        
        if(check_status(a, b, flag) is True):
            print ("True")
        else:
            print ("False")
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
}

def check_status(a, b, status):
    if status==True:
        if a<0 and b<0:
            return True
        else:
            return False
    elif status==False:
        if (a>0 or b>0) and (a<0 or b<0):
            return True
        else:
            return False;
