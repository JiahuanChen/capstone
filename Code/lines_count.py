
import argparse

parser = argparse.ArgumentParser(description="Count the lines of the data")
parser.add_argument('--fname', dest='fname', help='Specify the filename to count lines')
args = parser.parse_args()

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
print(file_len(args.fname))