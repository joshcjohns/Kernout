#!/usr/bin/python3

import sys
import os
import time
import random
import argparse
from pygments.lexers.c_cpp import CLexer
from pygments.formatters import TerminalFormatter
from pygments import highlight

parser = argparse.ArgumentParser(description="Print kernel sources to standard\
                                             output.")
group = parser.add_mutually_exclusive_group()
parser.add_argument("-c", "--colorless", action="store_true", help="Disable\
                    syntax highlighting")
parser.add_argument("-m", "--multiple", type=int, help="Specify how many times\
                    the source file is printed. (Default is 100)")
parser.add_argument("-d", "--delay", type=float, help="Specify a consistent\
                    delay in seconds between each line printed.")
group.add_argument("-t", "--throwback", action="store_true", help="Print\
                   random source file from kernel 0.01 instead of 1.0")
group.add_argument("-f", "--file", help="Print a C source file of\
                   your choice rather than a kernel file.")
args = parser.parse_args()
if not args.multiple:
    args.multiple = 100


def random_file():
    """Return a random source file from the specified directory."""
    file_list = []
    extensions = ['.c','.h','.S']
    if args.throwback == True:
        for root, dirnames, filenames in os.walk("kern/linux-0.01/"):
            for filename in filenames:
                ext = os.path.splitext(filename)[1].lower()
                if ext in extensions:
                    file_list.append(os.path.join(root, filename))
    else:
        for root, dirnames, filenames in os.walk("kern/linux-1.0/"):
            for filename in filenames:
                ext = os.path.splitext(filename)[1].lower()
                if ext in extensions:
                    file_list.append(os.path.join(root, filename))
    return random.choice(file_list)


def user_chosen_file():
    """Return a file specified by the user in -f argument."""
    if args.file.endswith(".c") or args.file.endswith(".h") or\
       args.file.endswith(".S"):
        return args.file
    else:
        sys.exit("File must have extension of \".c\", \".h\", or \".S\".")


def final_file():
    """Return the actual file to be printed to standard output."""
    if args.file:
        return user_chosen_file()
    else:
        return random_file()


def print_code():
    """Print source file to the screen."""
    if args.delay:
        if args.colorless:
            with open(final_file()) as code:
                i = 0
                while i < args.multiple:
                    current_line = code.readline()
                    while current_line:
                        print(current_line,end='')
                        time.sleep(args.delay)
                        current_line = code.readline()
                    code.seek(0)
                    i += 1
        else:
            with open(final_file()) as code:
                i = 0
                while i < args.multiple:
                    current_line = code.readline()
                    while current_line:
                        print(highlight(current_line,CLexer(),\
                              TerminalFormatter()),end='')
                        time.sleep(args.delay)
                        current_line = code.readline()
                    code.seek(0)
                    i += 1
    else:
        if args.colorless:
            with open(final_file()) as code:
                i = 0
                while i < args.multiple:
                    current_line = code.readline()
                    while current_line:
                        print(current_line,end='')
                        time.sleep(random.triangular(0,1.0,0.001))
                        current_line = code.readline()
                    code.seek(0)
                    i += 1        
        else:
            with open(final_file()) as code:
                i = 0
                while i < args.multiple:
                    current_line = code.readline()
                    while current_line:
                        print(highlight(current_line,CLexer(),\
                              TerminalFormatter()),end='')
                        time.sleep(random.triangular(0,1.0,0.001))
                        current_line = code.readline()
                    code.seek(0)
                    i += 1
        

print_code()
