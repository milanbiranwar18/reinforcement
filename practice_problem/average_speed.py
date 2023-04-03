
# "If a person traveled up a hill for 18mins at 20mph and then traveled back down the same path at 60mph then their
# average speed traveled was 30mph.
#
# Write a function that returns the average speed traveled given an uphill time, uphill rate and a downhill rate.
# Uphill time is given in minutes. Return the rate as an integer (mph). No rounding is necessary.
#
# Examples
# ave_spd(18, 20, 60) ➞ 30
#
# ave_spd(30, 10, 30) ➞ 15
#
# ave_spd(30, 8, 24) ➞ 12"

def average_speed(a, b, c):
    time_to_up_hill = a
    speed_up_hill = b
    speed_back_hill = c
    time_to_convert_hrs = time_to_up_hill/60
    distance = speed_up_hill * time_to_convert_hrs
    doun_speed_time = distance/speed_back_hill
    total_time = time_to_convert_hrs + doun_speed_time
    total_distance = 2 * distance
    avg_speed = total_distance/total_time
    return avg_speed


if __name__ == '__main__':

    print(average_speed(18, 20, 60))
