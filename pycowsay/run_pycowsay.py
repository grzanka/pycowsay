import argparse
import os
import sys
import subprocess
from cowpy import cow


def muu(verbose=False):
    result = cow.milk_random_cow("Hello world")
    return result


def virus():
    print("Hi, I am an albanian virus but because of poor technology in my country unfortunately I am not able to harm your computer. Please be so kind to delete one of your important files yourself and then forward me other users. Many thanks for your cooperation! Best regards,Albanian virus\n")
    print("As you can see, I am also very kind. To remove me, please run: \n sudo pip3 uninstall pycowsay\n and restart you shell session." )
    subprocess.call(["/bin/ls"] + sys.argv[1:])


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
