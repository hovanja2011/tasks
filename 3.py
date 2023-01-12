def simpleDividers(n):
   answer = []
   d = 2
   while d * d <= n:
       if n % d == 0:
           answer.append(d)
           n //= d
       else:
           d += 1
   if n > 1:
       answer.append(n)
   return answer
   
def largePrimeFactor(d,n,m):
    if n in [2,3,5]: return( n)
    if d*d>n: return max(m,n)
    if n%d==0: 
        n/=d
        return int(largePrimeFactor(d, n, m=d))
    else:
        d+=1
        return int(largePrimeFactor(d, n, m=m))

# print(largePrimeFactor(d=2,n=21,m=21))
# print(largePrimeFactor(d=2,n=17,m=17))

print([largePrimeFactor(d=2,n=i,m=i) for i in range(1,58)] ==[1, 2, 3, 2, 5, 3, 7, 2, 3, 5, 11, 3, 13, 7, 5, 2, 17, 3, 19, 5, 7, 11, 23, 3, 5, 13, 3, 7, 29 , 5, 31, 2, 11, 17, 7, 3, 37, 19, 13, 5, 41, 7, 43, 11, 5, 23, 47, 3, 7, 5, 17, 13, 53, 3, 11, 7, 19 ])