import itertools
import subprocess
import time
import argparse
from multiprocessing import Process
import sys


parser = argparse.ArgumentParser()
parser.add_argument('--password', help="The password to crack")
args = parser.parse_args()
password = args.password


digits = 10
lowerChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upperChars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
              'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['"', "#", "$", "%", "&", "'",
           "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@"]


firstAll = []
firstAll = lowerChars + upperChars + nums + symbols
secondAll = []
secondAll = upperChars + lowerChars + nums + symbols
thirtAll = nums + upperChars + lowerChars + symbols
fourthAll = symbols + lowerChars + upperChars + nums

def bruteForceFirst():
    startTimeP1 = time.time()
    try:
        print("Starting First Process...")
        for r in range(0, digits):
            for s in itertools.product(firstAll, repeat=r):
                chars = ''.join(s)
                if chars == password:
                    print("First Tread Found Password: " + password)
                    stopTimeP1 = time.time()
                    print("Time:", stopTimeP1 - startTimeP1, "\n\n")
                    sys.exit()
    except KeyboardInterrupt:
        sys.exit()


def bruteForceSecond():
    startTimeP2 = time.time()
    try:
        print("Starting Second Process...")
        for r in range(0, digits):
            for s in itertools.product(secondAll, repeat=r):
                chars = ''.join(s)
                if chars == password:
                    print("Second Tread Found Password: " + password)
                    stopTimeP2 = time.time()
                    print("Time:", stopTimeP2 - startTimeP2, "\n\n")
                    sys.exit()
    except KeyboardInterrupt:
        sys.exit()


def bruteForceThirt():
    startTimeP3 = time.time()
    try:
        print("Starting Thirt Process...")
        for r in range(0, digits):
            for s in itertools.product(thirtAll, repeat=r):
                chars = ''.join(s)
                if chars == password:
                    print("Thirt Tread Found Password: " + password)
                    stopTimeP3 = time.time()
                    print("Time:", stopTimeP3 - startTimeP3, "\n\n")
                    sys.exit()
    except KeyboardInterrupt:
        sys.exit()


def bruteForceFourth():
    startTimeP4 = time.time()
    try:
        print("Starting Fourth Process...\n\n")
        for r in range(0, digits):
            for s in itertools.product(fourthAll, repeat=r):
                chars = ''.join(s)
                if chars == password:
                    print("Fourth Tread Found Password: " + password)
                    stopTimeP4 = time.time()
                    print("Time:", stopTimeP4 - startTimeP4, "\n\n")
                    sys.exit()
    except KeyboardInterrupt:
        sys.exit()

p1 = Process(target = bruteForceFirst)
p1.start()
p2 = Process(target = bruteForceSecond)
p2.start()
p3 = Process(target = bruteForceThirt)
p3.start()
p4 = Process(target = bruteForceFourth)
p4.start()

try:
    p1.join()
    p2.join()
    p3.join()
    p4.join()
except KeyboardInterrupt:
    exit()
