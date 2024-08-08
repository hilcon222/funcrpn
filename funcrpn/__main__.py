"Main executable"

# Idk if you will read this, but today I'm really happy!

# from funcrpn import stack, operators

NUMBER = 1
OPERATOR = 2


def detect_type(val):
    """Detects the type of the input."""
    try:
        return float(val), NUMBER
    except ValueError:
        return val, OPERATOR


def main():
    "Main function"
    # s = []
    print("ciao")


if __name__ == '__main__':
    main()
