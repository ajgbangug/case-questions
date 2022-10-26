INPUT_STRING=''

class LetterFilter:
    def __init__(self, s):
        self.s = s

    def filter_vowels(self):
        vowels = ['a', 'e', 'i', 'o', 'u']
        result_str = [c for c in self.s if c not in vowels]

        return "".join(result_str)

    def filter_consonants(self):
        vowels = ['a', 'e', 'i', 'o', 'u']
        result_str = [c for c in self.s if c in vowels]

        return "".join(result_str)

test1 = LetterFilter(INPUT_STRING)
print(test1.filter_consonants())
print(test1.filter_vowels())
