def main(n):
    size = len(n)
    k = 2**size
    subsets = []

    for i in range(k):
        bit = bin(i).replace('0b','')
        bit = (size - len(bit)) * '0' + bit
        st = ''
        for k in range(len(bit)):
            if bit[k] == '1':
                st += n[k]
        if st != '' and int(st) != 0:
            subsets.append(int(st))

    steps = 0
    for i in subsets:
        if (i % 25 == 0 ) and len(str(i)) > steps:
            steps = len(str(i))

    print(size - steps)
def interface():
    t  = int(input())
    for i in range(t):
        main(input())
interface()