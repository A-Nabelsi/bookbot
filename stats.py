def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = 0 
        for nums in words:
            num_words += 1
        return f"{num_words} words found in the document"

def get_num_char(file_contents):
    character_dict = {}
    for word in file_contents:
        word = word.lower()
        for c in word:
            if c in character_dict:
                character_dict[c] += 1
            else:
                character_dict[c] = 1
    return character_dict
            

