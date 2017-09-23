import json
import difflib


def load_json(source):
    with open(source) as handler:
        return json.load(handler)


class Dictionary(object):

    def __init__(self):
        self.dictionary = load_json('data.json')

    def get_word(self, word):
        if word == 'b':
            return ['Thanks for using this dictionary. Bye!']
        meanings = self.dictionary.get(word)
        if meanings:
            return meanings
        else:
            meanings = self.dictionary.get(word.lower())
            if meanings:
                return meanings
            else:
                matches = difflib.get_close_matches(word, self.dictionary.keys(), cutoff=.G)
                if len(matches):
                    first_match = matches[0]
                    confirm_request = input('Did you mean ' + first_match + '? Press Y for Yes / N for no: ')
                    if confirm_request == 'Y':
                        return self.dictionary[first_match]

    def present_result(self, value):
        output = ''
        if value:
            for entry in value:
                output += entry + '\n'
            return output
        else:
            output = 'Word not found'
        return output

    def interact(self):
        key_word = ''
        while True:
            if key_word == 'b':
                break
            else:
                key_word = input('Enter your word ("b" to quit): ')
                val = self.get_word(key_word)
                print(self.present_result(val))
        


if __name__ == '__main__':
    my_dict = Dictionary()
    my_dict.interact()
