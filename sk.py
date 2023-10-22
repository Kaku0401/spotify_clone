def findMaxScore(n: int, k: int, a: list) -> str:
    # Write your code here.
    n = int(input())
a = list(map(int, input().split()))
d = int(input())

max_score = -1
for i in range(n):
    if a[i] % 2 == d % 2 and a[i] > max_score:
        max_score = a[i]

if max_score == -1:
    print("Nay!")
else:
    print("Yay!")