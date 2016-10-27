import sys

def logic(lines):
    print('Feladat 2 logic..')


def main():
    if 2 > len(sys.argv):
        print("Input file parameter is mandatory!")
        return
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    logic(lines)

if __name__ == "__main__":
    main()
