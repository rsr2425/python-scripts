def get_div_num(n):
    d = []
    limit = int(n**(1.0/2))
    for i in range(1, limit+1):
        if n % i == 0:
            d.append(i)
        if i != n / i and n % i == 0:
            d.append(n/i)
    return len(d)
    
curr_num = 0
counter = 1
while get_div_num(curr_num) < 500:
    curr_num += counter
    counter += 1
    print curr_num

print "The first triangle number with five hundred divsors is: %d" % curr_num
