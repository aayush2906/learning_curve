"""You are given a string str, you need to print True if cat and hat appear same number of times in str, otherwise print False.

"""
{

def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        mystr=input()
        print(cat_hat(mystr))
        testcases-=1
        
if __name__=='__main__':
    main()
}

def cat_hat(str):
    count_cat=0;
    count_hat=0;
    
    for i in range(0,len(str)+1):
        if "cat" in str[i:i+3]:
            count_cat +=1;
        if "hat" in str[i:i+3]:
            count_hat +=1;
    if(count_cat==count_hat):
        return True;
    else:
        return False;
