def separate_phrase(name_file):
    file = open(name_file, "r", encoding='utf-8')
    lines_phrase = file.readlines()
    list_phrases = []
    for lines in lines_phrase:
        lines = lines.rstrip('\n')
        if not (lines.isnumeric()) and lines:
            list_phrases.append(lines)
    file.close()
    return list_phrases