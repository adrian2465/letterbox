import argparse
import random

debug = False

class Wordle:

    def __init__(self, possibilities):
        self.guess = None
        # Generate starter list
        self.starters = [possibilities[i].removeprefix("!")
                         for i in range(0, len(possibilities))
                         if "!" in possibilities[i] and "#" not in possibilities[i]]
        # Remove already-used words.
        self.possibilities = [possibilities[i].removeprefix("!")
                              for i in range(0, len(possibilities))
                              if not possibilities[i].startswith("#")]
        self.exclude_list = ['', '', '', '', '']
        self.num_guesses = 1

    def solve(self, first_word):
        first_word = random.choice(self.starters) if first_word is None else first_word
        if first_word not in self.possibilities:
            raise ValueError(f"{first_word} is not in dictionary.")
        self.guess = first_word
        print("Enter clue for each guess. '-aV--' means 'a' is present but in wrong position, 'V' is in right position.")
        self.num_guesses = 0
        while True:
            self.num_guesses += 1
            clue = input(f"Guess #{self.num_guesses}) {self.guess}: ")
            found_it = True
            for c in clue:
                if not 'A' <= c <= 'Z':
                    found_it = False
                    break;
            if found_it:
                return self.guess

            self.filter_possibilities(clue)
            if len(self.possibilities) > 1:
                self.generate_new_guess()
            else:
                if len(self.possibilities) == 1:
                    self.guess = self.possibilities[0]
                    self.num_guesses += 1
                else:
                    self.guess = None
                break
        return self.guess

    def filter_possibilities(self, clue):
        for i in range(0, len(clue)):
            # Filter wordlist to remove words which do not have the correct letter in the correct place.
            if 'A' <= clue[i] <= 'Z':
                self.possibilities = [p for p in self.possibilities if self.guess[i] == p[i]]
            elif 'a' <= clue[i] <= 'z':
                self.possibilities = [p for p in self.possibilities if self.guess[i] in p and p[i] != clue[i]]
            if  clue[i] == '-':
                self.exclude_list[i] = f"{self.exclude_list[i]}{self.guess[i]}"
        # Filter wordlist to remove words not containing the missing dashed letters.
        for x in self.exclude_list:
            self.possibilities = [p for p in self.possibilities if len(set(p) & set(x)) == 0]

    @staticmethod
    def count(char, word):
        c = char.lower()
        w = word.lower()
        i = 0
        for i in range(0, len(w)):
            if c == w[i]: i += 1
        return i

    def generate_new_guess(self):
        list_to_try = [p for p in self.possibilities if not Wordle.has_repeats(p)]  # Prefer non-repeats
        if len(list_to_try) == 0: list_to_try = self.possibilities
        self.guess = random.choice(list_to_try)

    @staticmethod
    def has_repeats(word):
        for c in word:
            if Wordle.count(c, word) > 1: return True
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Solve Wordle Puzzle")
    parser.add_argument('-w','--first_word', help='Opening word', default=None)
    parser.add_argument('--dictionary', help='Dictionary (list of words)', default="five-letter-words.txt")
    args = parser.parse_args()
    with open(args.dictionary, "r") as f:
        word_list = f.read().lower().split()
    wordle = Wordle(word_list)
    print(f'Solution: {wordle.solve(args.first_word)} in {wordle.num_guesses} guesses')









