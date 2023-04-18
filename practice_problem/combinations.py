# Given a lists of words, print all combinations of phrases that can be formed by picking one word from each list.
#
# Input:
# lists =
# [
#  ['John', 'Emma'],
#  ['Plays', 'Hates', 'Watches'],
#  ['Cricket', 'Soccer', 'Chess']

# Output:
#  'John Plays Cricket',
#  'John Plays Soccer',
#  'John Plays Chess',
#  'John Hates Cricket',
#  'John Hates Soccer',
#  'John Hates Chess',
#  'John Watches Cricket',
#  'John Watches Soccer',
#  'John Watches Chess',
#  'Emma Plays Cricket',
#  'Emma Plays Soccer',
#  'Emma Plays Ch
def combinations(a_lists):
    for name in a_lists[0]:
        for activity in a_lists[1]:
            for game in a_lists[2]:
                sentence = name + " " + activity + " " + game
                print(sentence)


if __name__ == '__main__':
    lists = [
     ['John', 'Emma'],
     ['Plays', 'Hates', 'Watches'],
     ['Cricket', 'Soccer', 'Chess']
        ]
    combinations(lists)
