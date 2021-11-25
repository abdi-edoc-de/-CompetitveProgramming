def solve(s):
    vs,res = 0,0
    for i in s:
        if i == "v":
            vs += 1
        else:
            res += 1
            res += vs // 2
            vs = 0
    res += vs // 2
    print(res)



def main():
    t = int(input())
    for _ in range(t):
        s = input()
        solve(s)
print(2456/1111)
print(2210/1111)
main() 
