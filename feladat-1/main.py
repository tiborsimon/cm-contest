import sys

def get_result(n):
    numbers = []
    mult = 1
    while len(numbers) != 10:
        last = mult*n
        for number in list(str(last)):
            if number not in numbers:
                numbers.append(number)
        mult += 1
    return last

def logic(lines, buffer):
    for line in lines:
        n = int(line)
        if n == 0:
            result = 'INSOMNIA'
        else:
            result = get_result(n)
        buffer.append('Teszteset #{}: {}'.format(lines.index(line)+1, result))

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
