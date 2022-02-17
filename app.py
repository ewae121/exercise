from src.deduplicator import Deduplicator

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="String to deduplicate", type=str)
    parser.add_argument("max_occurences", help="Maximum of duplicated occurences", type=int)
    args = parser.parse_args()

    deduplicator  = Deduplicator()
    deduplicated_string = deduplicator.deduplicate(args.input, args.max_occurences)
    print("{}".format(deduplicated_string))