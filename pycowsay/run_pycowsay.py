import argparse
import os
import subprocess
from cowpy import cow


def muu(verbose=False):
    result = cow.milk_random_cow("Hello world")
    return result


def main():
    """
    Main function, called from CLI script
    :return:
    """
    import pycowsay
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose',
                        action='store_true',
                        help='be verbose')
    parser.add_argument('--version',
                        action='version',
                        version=pycowsay.__version__)
    args = parser.parse_args()

    print(muu(verbose=args.verbose))

if __name__ == '__main__':
    main()
