def get_div_num(n):
    d = []
    limit = int(n**(1.0/2))
    for i in range(1, limit+1):
        if n % i == 0:
            d.append(i)
        if i != n / i and n % i == 0:
            d.append(n/i)
    return len(d)

def rotate(n):
    result = []
    n = str(n)
    for x in range(len(n)):
        result.append(int(n[x:]+n[:x]))
    return result

def get_circp_num(upper_bound):
    counter = 0
    for i in range(1, upper_bound+1):
        print "checking %d" % i
        if get_div_num(i) == 1:
            result = True
            for rotation in rotate(i):
                result = result and (get_div_num(rotation) == 1)
            if result:
                counter+= 1
    return counter

print get_circp_num(1000000)
