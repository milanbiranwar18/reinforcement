# Given a list of words in the singular form, return a set of those words in the plural form if they appear more than
# once in the list.
#
# Examples
# pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }
#
# pluralize(["table", "table", "table"]) ➞ { "tables" }
#
# pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }

def pluralize(a_list):
    a_set = set()
    for word in a_list:
        if a_list.count(word) > 1:
            a_str = word + 's'
            a_set.add(a_str)
        else:
            a_set.add(word)
    return a_set


if __name__ == '__main__':
    print(pluralize(["cow", "pig", "cow", "cow"]))
    print(pluralize(["table", "table", "table"]))
    print(pluralize(["chair", "pencil", "arm"]))
