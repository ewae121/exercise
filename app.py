from src.deduplicator import Deduplicator

if __name__ == "__main__":
    deduplicator  = Deduplicator()
    deduplicated_string = deduplicator.deduplicate("abbbaaa", 2)
    print("{}".format(deduplicated_string))