n = int(input())
numbers = [int(val) for val in input().split()]
# numbers.sort()
min_odd = 9999999999999999
odd_sum = 0
ans = 0

for i in range(n):
    if numbers[i] % 2 == 0:
        ans += numbers[i]
    else:
        odd_sum += numbers[i]
        min_odd = min(numbers[i], min_odd)

if odd_sum % 2 == 0:
    print(ans + odd_sum)
else:
    print(ans + (odd_sum - min_odd))

