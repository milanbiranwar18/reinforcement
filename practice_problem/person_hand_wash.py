# It takes 21 seconds to wash your hands and help prevent the spread of COVID-19.
#
# Create a function that takes the number of times a person washes their hands per day N and the number of months they
# follow this routine nM and calculates the duration in minutes and seconds that person spends washing their hands.
#
# Examples
# wash_hands(8, 7) ➞ "588 minutes and 0 seconds"
#
# wash_hands(0, 0) ➞ "0 minutes and 0 seconds"
#
# wash_hands(7, 9) ➞ "661 minutes and 30 seconds"
# Notes
# Consider a month has 30 days


def person_hand_wash(n, nm):
    wash_time_sec = 21
    days_per_month = 30
    total_time_sec = wash_time_sec * n * nm * days_per_month
    return f"{total_time_sec//60} minutes and {total_time_sec%60} seconds"


if __name__ == '__main__':
    print(person_hand_wash(8, 7))
    print(person_hand_wash(0, 0))
    print(person_hand_wash(7, 9))
