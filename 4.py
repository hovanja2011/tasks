def largestPal(m):
    s=1
    s1=m
    s2=m
    p=s1*s2
    ps=str(p)
    while s1!=899 :
        if s2==100:
            s1-=1
            s2=s1+1
        s2-=1
        p=s1*s2
        ps=str(p)
        if ps==ps[::-1]:
            s=max(p,s)
    return(s)

print(largestPal(999))
# улучшить...