def smalMult(n):
    p=1
    lst=[2]
    for i in range(3, n+1, 2):
    	if (i > 10) and (i%10==5):
    		continue
    	for j in lst:
    		if j*j-1 > i:
    			lst.append(i)
    			break
    		if (i % j == 0):
    			break
    	else:
    		lst.append(i)

    for i in lst:
        k=i
        while k<=n:
            if k*i>n: break
            k=k*i
        p*=k
    return (p)
    
print(smalMult(20))