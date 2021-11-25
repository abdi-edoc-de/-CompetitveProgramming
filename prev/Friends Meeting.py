def main():
    friend_a = int(input())
    friend_b = int(input())

    mid = (friend_a + friend_b) // 2
    print(int(sum(abs(mid - friend_a)) + sum(abs(friend_b - mid))))
def sum(n):
    return (n * (n + 1))/2
main()