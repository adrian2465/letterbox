import argparse

_end = "_end_"
debug = False


class Trie:

    def __init__(self, words):
        self._root = dict()
        for word in words:
            current_dict = self._root
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
            current_dict[_end] = _end

    @property
    def root(self):
        return self._root

    def is_a_word_node(self, node: dict):
        return node.get(_end) is not None

    def get_children(self, node):
        return node.items()


class Letterbox:

    def __init__(self, letterbox_string, all_words_from_dictionary):
        letterbox = list()
        corners = letterbox_string.split("-")
        for corner in corners:
            letterbox.append([c for c in corner])
        self._flattened_letterbox = set()
        for edge in letterbox:
            self._flattened_letterbox = self._flattened_letterbox.union(edge)
        self._adjacency_matrix = []
        for c1 in self._flattened_letterbox:
            for c2 in self._flattened_letterbox:
                for edge in letterbox:
                    if c1 in edge and c2 in edge:
                        self._adjacency_matrix.append(f"{c1}{c2}")
        self._allowed_words = [w.lower() for w in all_words_from_dictionary if self._is_allowed(w)]
        self._trie = Trie(self._allowed_words)

    def _is_adjacent(self, c1, c2):
        if c1 is None: return False
        return (c1 + c2) in self._adjacency_matrix

    def _is_allowed(self, word):
        letter_set = set(word)
        if not letter_set.intersection(self._flattened_letterbox) == letter_set:
            return False
        c_prev = None
        for c_curr in word:
            if self._is_adjacent(c_prev, c_curr):
                return False
            c_prev = c_curr
        return True

    def _is_a_word_node(self, node):
        return self._trie.is_a_word_node(node)

    def _all_words_from_this_node_down(self, node, word_fragment):
        valid_word_list = []
        for ni in node.items():
            subnode = ni[1]
            if subnode == _end: continue  # Ignore the _end child - it signifies that the PARENT is a word. Additional children, however, indicate longer words.
            word_to_evaluate = word_fragment + ni[0]
            if self._is_a_word_node(subnode):
                valid_word_list.append(word_to_evaluate)
            for w in self._all_words_from_this_node_down(subnode, word_to_evaluate):
                valid_word_list.append(w)
        return valid_word_list


    @property
    def all_possible_words(self):
        return self._all_words_from_this_node_down(self._trie.root, '')

    def all_subsequent_words(self, prev_word):
        first_letter = prev_word[-1]
        subnode = self._trie.root.get(first_letter)
        if subnode is None:
            return []
        return self._all_words_from_this_node_down(subnode, first_letter)

    def is_complete(self, words):
        letters_used = set()
        for word in words:
            for c in word:
                letters_used = letters_used.union(c)
        rc = letters_used.intersection(self._flattened_letterbox) == self._flattened_letterbox
        if rc:
            return True
        else:
            if (debug): print(f"{words} is lacking {self._flattened_letterbox - letters_used}")

    @property
    def solutions(self):
        solutions = []
        for first_word in self.all_possible_words:
            for subsequent_word in self.all_subsequent_words(first_word):
                if self.is_complete([first_word, subsequent_word]):
                    solutions.append(f"{first_word}-{subsequent_word}")
        return solutions


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Solve Letterbox Puzzle")
    parser.add_argument('--puzzle', help='Dash-separated list of strings representing the corners of the puzzle. For example asd-feg-jiy-uiu', required=True)
    parser.add_argument('--dictionary', help='Dictionary (list of words)', default="words.txt")
    args = parser.parse_args()
    with open(args.dictionary, "r") as f:
        all_words_from_dictionary = f.read().lower().split()
    print(f"Solutions for letterbox {args.puzzle}: ")
    solutions = Letterbox(letterbox_string=args.puzzle, all_words_from_dictionary=all_words_from_dictionary).solutions
    for solution in solutions:
        print(f" * {solution}")







