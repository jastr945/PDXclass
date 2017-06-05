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

with open('/home/polina/projects/class/sample.rain', 'r') as text:
    rains = text.readlines()[11:]

    maxrain = ('1-JAN-2015', 0)
    newdict = {}


    for rain in rains:
        newlist = rain[11:-1].split(' ')

        sumnumbers = (sum(int(i) for i in newlist if i != '' and i != '-'))

        datestr = rain[:11]

        if sumnumbers > maxrain[1]:
            maxrain = (datestr, sumnumbers)


        if datestr[-4:] not in newdict:
            newdict[datestr[-4:]] = 0
        newdict[datestr[-4:]] += sumnumbers


    print('The largest amount of rain per day: {} inches; date: {}.'.format(maxrain[1], maxrain[0]))
    maxyear = sorted(newdict.items(), key=lambda x: x[1])[-1]
    print('The largest amount of rain per year: {} inches; year: {}'.format(maxyear[1], maxyear[0]))







        # t = (datestr, sumnumbers)
        # print(t)







