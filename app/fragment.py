import re


def return_fragment(phrase):
    """return fragment from text"""
    opend_file = open("text.txt", "r")
    text = opend_file.read()
    # Take paragraph in which there is the right phrase from text 
    result = re.search("\n.*"+phrase+".*\n", text)
    if result:
        fragment = result[0].strip()
        # If fragment close ":"(in russian language most often it means that text ends with a direct speech), that take next paragraph
        if fragment[-1] == ":":
            new_fragment = re.search("\n.*"+phrase+".*\n.*\n", text)
            return new_fragment[0].strip()
        else:
            return fragment

    return "Отрывок не удалось найти..."

