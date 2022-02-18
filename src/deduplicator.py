import logging


class Deduplicator(object):
    """
    The Depduplicator provides a public deduplicate() method who act as following:
    - it returns a string that is similar to the first argument, but with certain duplicated characters removed.
    - it remove consecutive sequences of same character to ensure that the length of the sequence is no greater than the second integer argument.
    """

    def __init__(self):
        logging.basicConfig(level=logging.WARNING)
        self.input_string = None
        self.max_occurences = 0

        self.cur_status = {"curCharacter": "", "curOccurences": 0}

    def _init(self, input_string, max_occurences):
        self.input_string = input_string
        self.max_occurences = max_occurences

        self.cur_status = {"curCharacter": "", "curOccurences": 0}

    def _update_status(self, character, occurence_nbr):
        self.cur_status["curCharacter"] = character
        self.cur_status["curOccurences"] = occurence_nbr

    def _process_character(self, character, occurence):
        logging.info("process {} - occurence: {}".format(character, occurence))
        if self.cur_status["curOccurences"] < self.max_occurences:
            occurence += 1
            self._update_status(character, occurence)
            return True
        return False

    def get_next_character(self):
        for character in self.input_string:
            yield character


    def deduplicate(self, input_string, max_occurences):
        new_string = ""

        input_string = str(input_string)
        max_occurences = int(max_occurences)

        self._init(input_string, max_occurences)

        for character in self.get_next_character():
            occurence = 0
            if character != self.cur_status["curCharacter"]:
                self._update_status(character, occurence)
            else:
                occurence = self.cur_status["curOccurences"]

            if self._process_character(character, occurence):
                new_string += character

        return new_string


if __name__ == "__main__":
    deduplicator = Deduplicator()
    new_string = deduplicator.deduplicate("aaaa", 3)
    print(f"{new_string}")
