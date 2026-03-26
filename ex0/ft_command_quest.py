import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)

    print("=== Command Quest ===")
    print(f"Program name: {argv[0]}")
    # no arguments
    if argc == 1:
        print("No arguments provided!")
    # received arguments from the command line
    else:
        print(f"Arguments received: {argc - 1}")
        i = 1
        while i < argc:
            print(f"Argument {i}: {argv[i]}")
            i += 1
    print(f"Total arguments: {argc}")
