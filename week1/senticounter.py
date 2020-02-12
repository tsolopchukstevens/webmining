from collections import defaultdict


def get_lex_from_file(file_path):
    try:
        file = open(file_path)
    except FileNotFoundError:
        print("File Not Found: " + str(file_path))
    except IsADirectoryError:
        print("This is a directory: " + str(file_path))
    else:
        with file:
            file_lines = set()
            for line in file.readlines():
                file_lines.add(line.strip())
            return file_lines


def run(input_file_path):
    neg_words = get_lex_from_file("negative-words.txt")
    phrases = get_lex_from_file(input_file_path)
    found_dict = defaultdict(int)
    for phrase in phrases:
        for word in neg_words:
            if word in phrase:
                phrase_iterator = iter(phrase.split(' '))
                done_looping = False
                while not done_looping:
                    try:
                        item = next(phrase_iterator)
                        if item in neg_words:
                            found_dict[item] += 0
                        if item == "the":
                            next_item = next(phrase_iterator)
                            if next_item in neg_words:
                                found_dict[next_item] += 0
                                word_after_neg = next(phrase_iterator)
                                if word_after_neg == "phone":
                                    found_dict[next_item] += 1
                    except StopIteration:
                        done_looping = True
    return found_dict


if __name__ == "__main__":
    print(run("textfile"))
