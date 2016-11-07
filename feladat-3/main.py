import sys

def decision(n, m, x):
    if n == 1 or m == 1:
        return n*m-2 >= x
    if n in (3, 4) or m in (3,4):
        return n*m-4 >= x
    if n > 4 and m > 4:
        return n*m-9 >= x
    return False


def paint(n, m, x, buffer):
    if n == 1 or m == 1:
        out = 'c.' + '.'*(max(n,m)-2-x) + '*'*x
        if m == 1:
            for c in out:
                buffer.append(c)
        else:
            buffer.append(out)
    elif n in (3, 4) or m in (3,4):
        out = []
        mask = []
        for nn in range(n):
            mask.append([nn in (0,1) and mm in (0,1) for mm in range(m)])
            out.append(list('.'*m))
        out[0][0] = 'c'
        import pdb; pdb.set_trace()
        for i in range(x):
            j = i
            while True:
                mm = -(j%m + 1)
                nn = -(j/n + 1)
                if mask[nn][mm]:
                    j += 1
                else:
                    out[nn][mm] = '*'
                    break
        for line in out:
            buffer.append(''.join(line))
    elif n > 4 and m > 4:
        buffer.append('larger')


def logic(lines, buffer):
    for line in lines[1:]:
        n,m,x = [int(i) for i in line.split()]
        buffer.append('Teszteset #{}:'.format(lines.index(line)))
        if decision(n, m, x):
            paint(n, m, x, buffer)
        else:
            buffer.append('Lehetetlen!')


def main():
    buffer = []
    if 2 > len(sys.argv):
        print("Input file parameter is mandatory!")
        return
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    logic(lines, buffer)
    import pdb; pdb.set_trace()
    with open(sys.argv[2], 'w+') as f:
        for line in buffer:
            f.write('{}\n'.format(line))

if __name__ == "__main__":
    main()
