'''
The amounts are in hundredths of inches or are a - if the sensor was broken.

Print out a summary of the data:

    The specific date with the most rain.
    The year with the most rain.

Note:

    The header has a totally different format than the data itself. You will have to slice out the header lines from all the lines you read.

    You can split a string by whitespace into a list of strings using .split().

    Extract the date sting from the date columns.

    If there are any days with - for data, explicitly drop them from your dataset.

    Avoid using un-named "pairs" outside of dictionaries.

    If you need to group together individual instances of a date and a rainfall amount use a tuple! ( Or perhaps look at the namedtuple form collections. )

Advanced

    Find and print the day of the year with the most rain on average. E.g. December 30th has 1" of rain on average.

    Allow someone to type in a date in the future and, using the average value for that day of the year, predict the amount of rain.

'''

with open('/home/polina/projects/class/sample.rain','r') as text:
    rains = text.readlines()[11:15]
    # from ipdb import set_trace; set_trace()
    # print(rains)
    for rain in rains:
        print(rain[:-1].split(' '))
            # date_str = line[0]
            # print(date_str)
    #     print(split_str[1:])
    #     w = 0
    #     for i in split_str[1:]:
    #         if i == '':
    #             continue
    #         else:
    #             w += int(i)
    #     print(w)

