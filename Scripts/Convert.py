#!/usr/bin/env python3

import sys
import argparse

sys.path.append('.')
from Util import *

def main():
    parser = argparse.ArgumentParser(description='Convert to another format.')
    parser.add_argument('infile', metavar='input_file', type=str, help='input filename (.xml)')
    parser.add_argument('outfile', metavar='output_file', type=str, help='output filename (.csv)')
    args = parser.parse_args()
    rl = ROMList()
    try:
        rl.loadFromFile(args.infile)
        rl.saveToFile(args.outfile)
    except FormatError as fe:
        return str(fe)
    return 0

if __name__ == '__main__':
    sys.exit(main())
