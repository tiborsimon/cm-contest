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


def logic(params, buffer):
    for index in params:
        n = params[index]
        result = 'INSOMNIA 'if n == 0 else get_result(n)
        buffer.append('Teszteset #{}: {}'.format(index, result))


def parse_params(lines):
    params = {}
    index = 1
    for line in lines[1:int(lines[0])+1]:
        params[index] = int(line)
        index += 1
    return params


def main():
    buffer = []
    if 2 > len(sys.argv):
        print("Input and output file name parameters are mandatory!")
        return
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    params = parse_params(lines)
    logic(params, buffer)
    with open(sys.argv[2], 'w+') as f:
        for line in buffer:
            f.write('{}\n'.format(line))


if __name__ == "__main__":
    main()
