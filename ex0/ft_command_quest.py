import sys

if __name__ == "__main__":
    argv = sys.argv
    print("=== Command Quest ===")

    # no arguments
    argc = len(argv)
    if argc == 1:
        print("No arguments provided!")
        print(f"Program name: {argv[0]}")
        print(f"Total arguments: {argc}")
    # received arguments from the command line
    else:
        print(f"Program name: {argv[0]}")
        print(f"Arguments received: {argc - 1}")
        i = 1
        while i < argc:
            print(f"Argument {i}: {argv[i]}")
            i += 1
        print(f"Total arguments: {argc}")
