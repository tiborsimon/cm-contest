import sys

def decision(n, m, x):
    if n == 1 or m == 1:
        return n*m-2 >= x
    if n > 2 and m > 2:
        if ((x%m)%2) and x > m:
            return False
        return n*m-4 >= x
    return False


def paint(n, m, x, buffer):
    if n == 1 or m == 1:
        out = 'c.' + '.'*(max(n,m)-2-x) + '*'*x
        if m == 1:
            for c in out:
                buffer.append(c)
        else:
            buffer.append(out)
    else:
        out = []
        mask = []
        for nn in range(n):
            mask.append([nn in (0,1) and mm in (0,1) for mm in range(m)])
            out.append(list('.'*m))
        out[0][0] = 'c'
        for i in range(x):
            j = i
            jumped = False
            while True:
                mm = -(j%m + 1)
                nn = -(j/m + 1)
                if mask[nn][mm]:
                    j += 1
                    jumped = True
                else:
                    out[nn][mm] = '*'
                    if jumped:
                        mask[nn][mm] = True
                    break
        for line in out:
            buffer.append(''.join(line))


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
    with open(sys.argv[2], 'w+') as f:
        for line in buffer:
            f.write('{}\n'.format(line))

if __name__ == "__main__":
    main()
