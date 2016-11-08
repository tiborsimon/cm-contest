import sys

def decision(n, m, x):
    if n == 1 or m == 1:
        return n*m-2 >= x
    if n > 2 and m > 2:
        full_rows =  get_full_rows(n, m, x)
        if full_rows < n-2:
            if (m - x + full_rows*m) == 1 and x/m == n-3:
                return False
        if full_rows >= n-2:
          if ((x-full_rows*m)%2) and x > m:
              return False
        return n*m-4 >= x
    return False

def get_full_rows(n, m, x):
    lines = x/m
    return lines - (lines -n+2) if lines > n-2 else lines

def paint(n, m, x, buffer):
    if n == 1 or m == 1:
        out = 'c.' + '.'*(max(n,m)-2-x) + '*'*x
        if m == 1:
            for c in out:
                buffer.append(c)
        else:
            buffer.append(out)
    else:
        out = [list('.'*m) for _ in range(n)]; out[0][0] = 'c'
        full_rows = get_full_rows(n, m, x)
        if full_rows < n-2:
            full_rows += 1
        threshold = full_rows * m
        for i in range(x):
            if i < threshold:
                mm = -(i%m + 1)
                nn = -(i/m + 1)
                if x-i == 1 and -mm == m-1:
                    nn -= 1
                    mm = -1
            else:
                j = i-threshold
                nn = 1 - j%2
                mm = -1 * (j/2+1)
            out[nn][mm] = '*'
        for line in out:
            buffer.append(''.join(line))


def logic(lines, buffer):
    for line in lines:
        n,m,x = [int(i) for i in line.split()]
        buffer.append('Teszteset #{}:'.format(lines.index(line)+1))
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
        lines = lines[1:int(lines[0])+1]
    logic(lines, buffer)
    with open(sys.argv[2], 'w+') as f:
        for line in buffer:
            f.write('{}\n'.format(line))

if __name__ == "__main__":
    main()
