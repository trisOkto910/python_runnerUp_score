n = int(input('enter the size of list:'))
arr = list(map(int, input('Enter entries with space:').split()))

arr.sort()

print(f'hasil sorting array {arr}')

print(f'result runner up score {arr[-2]}')
