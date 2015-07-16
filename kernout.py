#!/usr/bin/python

import sys
import os
import time
import random
from pygments.lexers.c_cpp import CLexer
from pygments.formatters import TerminalFormatter
from pygments import highlight


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
