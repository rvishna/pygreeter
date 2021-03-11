import sys
from typing import List

from pygreeter.exceptions import MissingNameError, PyGreeterError


def main(argv: List[str]) -> int:
    try:
        print(f"Hello, {argv[0]}")
    except IndexError as exc:
        raise MissingNameError from exc
    return 0


if __name__ == "__main__":
    try:
        exit_code = main(sys.argv[1:])
    except PyGreeterError as exc:
        print(f"An error occurred when running pygreeter: {str(exc)}")
        exit_code = 1
    except Exception as exc:
        print(f"An unexpected error occurred when running pygreeter: {str(exc)}")
    finally:
        sys.exit(exit_code)
