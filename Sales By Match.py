def sockMerchant(n, ar):
    # Write your code here
    map ={}
    for i in ar:
        if i in map:
            map[i]  += 1
        else:
            map[i] =1;
    pair = 0
    for i in map:
        pair+=int(map[i]/2)
    return pair
sockMerchant(9,[10,20,20,10,10,30,50,10,20])