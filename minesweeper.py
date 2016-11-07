

def decision(n, m, x):
    return n*m-(2 if n == 1 or m == 1 else 4) >= x if n >= 3 or m >= 3 else False

def paint(n, m, x):
    if n == 1 or m == 1:
        out = 'c.' + '.'*(max(n,m)-2-x) + '*'*x
        if m == 1:
            for c in out:
                print(c)
        else:
            print(out)
    else:
        out = ['c.','..']
        # if x<

# ooooo
# ooooo
# ooooo
# ooooo
        for i in range(n):
            print('.'*m)

def main():
    with open('input.txt') as f:
        lines = f.readlines()
    for line in lines[1:]:
        n,m,x = [int(i) for i in line.split()]
        print('Teszteset #{}:'.format(lines.index(line)))
        if decision(n,m,x):
            paint(n,m,x)
        else:
            print('Lehetetlen!')

if __name__ == "__main__":
    main()
