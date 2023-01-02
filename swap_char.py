def char_match(s,t):
    if(len(s)<2):
        return False
    else:
        for i in range(len(s)-1):
            if(s[i]!=t[i]):
                last=s[i+1]
                first=s[i]
                s[i]=last
                s[i+1]=first
                return (s==t)
                
            
        


s=list(input())
t=list(input())
if(s==t):
    print("Yes")
else:
    result=char_match(s,t)
    if(result):
        print("Yes")
    else:
        print("No")
        
    
