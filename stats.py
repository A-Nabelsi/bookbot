def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = 0 
        for nums in words:
            num_words += 1
        return f"Found {num_words} total words"

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

def sort_on(item):
    return item["num"]

def sorted_dict(character_dict):
    sorted_dict = []       
    for k, v in character_dict.items():
        if k.isalpha():
            sorted_dict.append({"character": k, "num": v})
    sorted_dict.sort(reverse=True, key=sort_on)
    for i in sorted_dict:
        print(f"{i['character']}: {i['num']}")
