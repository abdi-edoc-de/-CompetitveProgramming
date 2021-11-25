
def maximumToys(prices, k):
    # Write your code here
    arr = sorted(prices)
    m = 0;
    toy_nums =0
    for i in arr:
        if k >= i+m:
            m+=i
            toy_nums +=1
    return toy_nums

print(maximumToys([1,12, 5 ,111, 200 ,1000 ,10],0))