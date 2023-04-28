# #273. Integer to English Words
# Hard
# 2.6K
# 5.8K
# Companies
# Convert a non-negative integer num to its English words representation.
#
#
#
# Example 1:
#
# Input: num = 123
# Output: "One Hundred Twenty Three"
# Example 2:
#
# Input: num = 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# Example 3:
#
# Input: num = 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

def integer_english(num):
    a_dict = {'1':"One", '2':'Two', '3':'Three', '4':'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Eight', '9':'Nine'
        , '0':'zero', '10':'Ten', '11':"Eleven", '12':'Twelve', '13':'Thirteen', '14':'Fourteen', '15':'Fifteen',
              '16':'sixteen', '17':'seventy', '18':'Eighteen', '19':'Ninty', '20':'Twenty', '30':'Thirty', '40':'Forty',
              '50':'Fifty', '60':'Sixty', '70':'Seventy'
              ,'80':'Eighty', '90':'ninty', '100':'Hundred'}

    num1 = str(num)
    if num1 in a_dict.keys():
        return a_dict.get(num1)
    # elif num1 not in a_dict.keys():
    else:
        a_list = list(num1)
        for i in range(len(a_list)):
            a = num1.split(a_list[int(i)])

        # while num>0:


        # return a_dict.get(num1)


if __name__ == '__main__':
    print(integer_english(123))