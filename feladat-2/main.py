import sys

def step(plates):
    return [0 if p==0 else p-1 for p in plates]


def special_step(plates):
    target = plates[-1]
    plates[-1] = target/2
    plates.append(target-plates[-1])
    return sorted(plates)


def calculate_steps(plates):
    i = 1
    while True:
        plates = step(plates)
        if not sum(plates):
            break
        i += 1
    return i


def logic(params, buffer):
    for plates in params:
        steps = calculate_steps(plates)
        buffer.append('Teszteset #{}: {}'.format(params.index(plates)+1, steps))


def parse_params(lines):
    params = []
    for line in lines[2:int(lines[0])*2+1:2]:
        params.append(sorted([int(p) for p in line.split()]))
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
