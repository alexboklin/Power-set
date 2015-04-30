# Python 3.4.2

import re
import time
import argparse

def main():

    start = time.process_time()

    parser = argparse.ArgumentParser(description="Constructs a power set for your items.")
    parser.add_argument("-c", help="cardinality of power set", action="store_true")
    parser.add_argument("-t", help="execution time", action="store_true")
    args = parser.parse_args()

    while True:
        rawInput = input("Provide a list of at leats two items separated by single spaces: ")
        pattern = re.compile(r"^(\S+\s{1})+\S+$")
        result = pattern.match(rawInput)
        if not result:
            print("Wrong input. Try again.")
            continue
        else:
            finalInput = rawInput.split()
            break

    def powerSet(data):
        binaryOutcomes = [ bin(i)[2:].zfill(len(data)) for i in range(2 ** len(data)) ]
        result = []
        for outcome in binaryOutcomes:
            whatToTake = ''
            for m in re.finditer('1', outcome):
                whatToTake += str(data[m.start()])
            result.append(whatToTake)
        return sorted(result, key=len)
        
    output = powerSet(finalInput)
    print("Here is your power set: {}".format(output))

    if args.c:
        print("Your power set contains {} elements".format(2 ** len(finalInput)))

    if args.t:
        print("--- {} seconds ---".format(time.process_time() - start))

if __name__ == "__main__":
    main()  
