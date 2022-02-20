"""
  Deduplicator module used to deduplicate strings.
"""

import logging

from deduplicator import constants


class Deduplicator:
    """
    The Depduplicator provides a public deduplicate() method who act as following:
    - it returns a string that is similar to the first argument, but with certain
     duplicated characters removed.
    - it remove consecutive sequences of same character to ensure that the length
     of the sequence is no greater than the second integer argument.

    The deduplicate() method start the string deduplication. At the deduplication
    start or end the new events are sent to on_state_changed registered
    callbacks.

    To register a callback use the add_state_changed_cb() method with a method
    as argument with the following prototype:
      my_cb(new_state)
    """

    def __init__(self):
        logging.basicConfig(level=logging.WARNING)
        self.input_string = None
        self.max_occurences = 0

        self.cur_status = {"curCharacter": "", "curOccurences": 0}
        self.on_state_changed_cbs = []

    def add_state_changed_cb(self, call_back):
        """
          Register a callback with a method as argument
        The call_back method must have the following prototype:
            my_cb(new_state)
        """
        self.on_state_changed_cbs.append(call_back)

    def _init(self, input_string, max_occurences):
        self.input_string = input_string
        self.max_occurences = max_occurences

        self.cur_status = {"curCharacter": "", "curOccurences": 0}

    def _update_status(self, character, occurence_nbr):
        self.cur_status["curCharacter"] = character
        self.cur_status["curOccurences"] = occurence_nbr

    def _process_character(self, character, occurence):
        logging.info("process %s - occurence: %d", character, occurence)
        if self.cur_status["curOccurences"] < self.max_occurences:
            occurence += 1
            self._update_status(character, occurence)
            return True
        return False

    def _get_next_character(self):
        for character in self.input_string:
            yield character

    def _change_processing_state(self, state):
        for call_back in self.on_state_changed_cbs:
            call_back(state)

    def deduplicate(self, input_string, max_occurences):
        """
        deduplicate method used to deduplicate strings.
        parameters:
          input_string: string to process
          max_occurences: number of permitted max occurences
        """
        new_string = ""

        input_string = str(input_string)
        max_occurences = int(max_occurences)

        self._init(input_string, max_occurences)
        self._change_processing_state(constants.START_PROCESSING)

        for character in self._get_next_character():
            occurence = 0
            if character != self.cur_status["curCharacter"]:
                self._update_status(character, occurence)
            else:
                occurence = self.cur_status["curOccurences"]

            if self._process_character(character, occurence):
                new_string += character
        self._change_processing_state(constants.STOP_PROCESSING)

        return new_string
