n = int(input().strip())
if n % 2 == 0 and (2 <= n <= 5 or n > 20):
    print("Not Weird")
else:
    print("Weird")