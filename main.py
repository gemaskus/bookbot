def readFile(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def getNumWords(split_file_contents):
    return len(split_file_contents)

def getNumEachLetter(file_contents):
    letters = {}
    file_contents = file_contents.lower()
    for letter in file_contents:
        if letter.isalpha():
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters

def sortOn(dict):
    return dict["num"]

def main():
    words = []
    file_contents = readFile("books/frankenstein.txt")
    words = file_contents.split()
    num_words = getNumWords(words)
    letter_nums = getNumEachLetter(file_contents)
    letter_list = []
    for letter in letter_nums:
        print(letter)
        print(letter_nums[letter])
        letter_list.append({"letter": letter, "num": letter_nums[letter]})
    letter_list.sort(reverse=True, key=sortOn)

    print(letter_nums)

if __name__ == "__main__":
    main()