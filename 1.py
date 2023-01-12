def mult3or5v1(i,num,s=0):
    if i==num: return s
    if i%3==0 or i%5==0: return mult3or5v1(i+1,num,s+i)
    return mult3or5v1(i+1,num,s)
        
def mult3or5v2(num):
    num-=1
    c3=num//3
    c5=num//5
    c15=num//15
    s=0
    s=c3*(c3+1)/2*3
    s+=c5*(c5+1)/2*5
    s-=c15*(c15+1)/2*15
    return(int(s))

for i in range(100):
    if (mult3or5v1(0,i)!=mult3or5v2(i)):
        print(i)
