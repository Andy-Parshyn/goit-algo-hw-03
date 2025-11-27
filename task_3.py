def hanoi (n, a = 'A', b = 'B', c = 'C'):
    if n == 1:
        print(f'Move disk {n} from {a} -> {c}')
        return

    hanoi(n-1, a, c, b) 
    print(f'Move disk {n} from {a} -> {c}')
    hanoi(n-1, b,a,c)


disks = int(input('Set number of disks: '))
print('_'*40)
try:
    hanoi(disks)
except ValueError:
    print('Please set the integer number.')