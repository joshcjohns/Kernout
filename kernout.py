#!/usr/bin/python

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
group.add_argument("-f", "--file", type=file, help="Print a C source file of\
                   your choice rather than a kernel file.")
parser.parse_args()

def random_file():
    """Return a random source file from the specified directory."""
    file_list = []
    extensions = ['.c','.h','.S']
    for root, dirnames, filenames in os.walk('kern'):
        for filename in filenames:
            ext = os.path.splitext(filename)[1].lower()
            if ext in extensions:
                file_list.append(os.path.join(root, filename))
    return random.choice(file_list)








def print_code_timed():
    """Print source file to the screen with consistent timing."""
    with open(random_file()) as code:
        i = 0
        while i<100:
            current_line = code.readline()
            while current_line:
                print highlight(current_line,CLexer(),TerminalFormatter()),
                time.sleep(0.05)
                current_line = code.readline()
            code.seek(0)
            i += 1
        
def print_code_random_time():
    """Print source file to the screen with randomized timing."""
    with open(random_file()) as code:
        i = 0
        while i<100:
            current_line = code.readline()
            while current_line:
                print highlight(current_line,CLexer(),TerminalFormatter()),
                time.sleep(random.triangular(0,1.0,0.001))
                current_line = code.readline()
            code.seek(0)
            i += 1

print_code_random_time()
