def evFib(f1,f2,num,s=10):
    f3=f1+4*f2
    if f3>num: return(s)
    return( evFib(f2,f3,num, s=s+f3))

print(evFib(2,8,4000000))