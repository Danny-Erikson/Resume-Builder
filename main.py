import sys
from router import route


def main():
    if len(sys.argv) < 2:
        print("Usage: resume <action> [options]")
        print("Example: resume build dense")
        return

    action = sys.argv[1].lower()
    extra_args = sys.argv[2:]

    route(action, extra_args)


if __name__ == "__main__":
    main()
