'''
There are two friends, John and Smith, and the parameters j_angry and s_angry to indicate if each is angry. You are in trouble if both of them are angry or no one of them is angry. 
Now, complete the function which returns true if you are in trouble, else return false.
'''
{
#Initial Template for Python 3    
def main():
    testcase = int(input())
    
    # loop for testcases
    while(testcase > 0):
        string = input().split()
        string1 = string[0]
        string2 = string[1]
        if(string1 == 'True'):
            string1 = True
        else:
            string1 = False
        
        if(string2 == 'True'):
            string2 = True
        else:
            string2 = False
            
        print(friends_in_trouble(string1, string2))
        
        testcase -= 1
    
if __name__ == '__main__':
    main()
}

def friends_in_trouble(a_angry, b_angry):
    if (a_angry==0 and b_angry==0)or(a_angry==1 and b_angry==1):
        return True;
    else:
        return False;
