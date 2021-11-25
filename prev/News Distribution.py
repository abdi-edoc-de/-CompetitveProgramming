from math import factorial
def main():
    arr = input().split()

    boys = int(arr[0])
    girls = int(arr[1])
    actors = int(arr[2])
    boyPerm = (factorial(boys)/(factorial(boys-4) * factorial(4)))  
    girlPerm = (factorial(girls) / factorial(girls - 1)) 
    val = actors - 5
    all = boys + girls - 5
    other =  (factorial(all) / (factorial(all - val) * factorial(val) ))
    print(boyPerm * girlPerm * other)
    # print()
main()