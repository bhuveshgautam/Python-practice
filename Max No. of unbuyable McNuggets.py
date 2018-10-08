def mcN1(a,b,c):
    '''Enter no. of packs in which nuggets can be bought'''
    n=0
    ctr=0
    while(ctr<6):
        n=n+1
        p=False
        for i in range(n//a+1):
            for j in range(n//b+1):
                for k in range(n//c+1):
                    if(a*i+b*j+c*k==n):
                        p=True
                        
        if(p==True):
            ctr=ctr+1
        else:
            ctr=0
    print("Largest number of McNuggets that cannot be bought in exact quantity: ")
    return(n-6)
