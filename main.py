def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_total = word_count(file_contents)
        sorted_characters = unique_character(file_contents)
        print(f"--- Bookbots report of the book Frankenstein ---")
        print(f"{word_total} words found in this book")

        for char, count in sorted_characters:
            print(f"The '{char}' character was found {count} times")
        
        print("--- End of report ---")


def unique_character(file_contents):
    character_dic = {}
    file_contents = file_contents.lower()
    for character in file_contents:
        if character.isalpha():
            if character not in character_dic:
                character_dic[character] = 1
            else:
                character_dic[character] +=1
    char_list = sorted(character_dic.items(), key=lambda item: item[1], reverse=True)
    return char_list



def word_count(file_contents):
    words = file_contents.split()
    return len(words)

main()





