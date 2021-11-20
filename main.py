n = int(input('enter the size of list:'))
arr = list(map(int, input('Enter entries with space:').split()))

arr.sort()
k = arr[0]
for i in arr:
    if i > k:
        k = i
for l in range(arr.count(k)):
    arr.remove(k)
print(arr[-1])
