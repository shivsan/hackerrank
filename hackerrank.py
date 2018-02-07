def RSum(start, sum, count, d, n):
    if sum == n:
        #print(l)
        return count + 1

    if sum > n or start > int(pow(n, 1/d))+1:
        return count

    count = RSum(start+1, sum, count, d, n)
    #l.append(start)
    count = RSum(start+1, sum + pow(start, d), count, d, n)
    #l.pop()
    return count

def powerSum(n, d):
    # Complete this function
    count = 0
    for i in range(1, int(pow(n, 1/d))):
        count += RSum(i, 0, 0, d, n)
    return count

n = int(input())
d = int(input())
print(RSum(1,0,0,d,n))
#print(PSum(d, n))