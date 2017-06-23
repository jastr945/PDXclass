'''Delivery Method: Prompt and Dataset

Goal

Analyze the city of Portland, OR public dataset of recorded crimes for most common crime, rarest crime(s), and the year with most crime.
Instructions

The City of Portland has keeps track of crimes in a publicly available dataset!

Print out a summary of the data:

    The specific most common crime type.
    The rarest crimes.
    The year with the most crime.
'''

import csv

def count_crime(crime_incident_data, new_dict={}):
    with open(crime_incident_data, 'r') as text:

        original_dict = csv.DictReader(text)

        for line in original_dict:
            if line['Major Offense Type'] in new_dict:
                new_dict[line['Major Offense Type']] += 1
            else:
                new_dict[line['Major Offense Type']] = 1

        return new_dict


year_2011 = count_crime('/home/polina/projects/class/crime_incident_data_2011.csv')

year_2012 = count_crime('/home/polina/projects/class/crime_incident_data_2012.csv',year_2011)


year_2013 = count_crime('/home/polina/projects/class/crime_incident_data_2013.csv',year_2012)

year_2014 = count_crime('/home/polina/projects/class/crime_incident_data_2014.csv',year_2013)

recent_data = count_crime('/home/polina/projects/class/crime_incident_data_recent.csv',year_2014)


for k, v in recent_data.items():
    if v == max(recent_data.values()):
        print('The most common type of crime is: {}. Number of cases: {}.'.format(k,v))

for k, v in recent_data.items():
    if v == min(recent_data.values()):
        print('The rarest type of crime is: {}. Number of cases: {}.'.format(k,v))


year_summary = {
    'year 2011': sum(count_crime('/home/polina/projects/class/crime_incident_data_2011.csv').values()),
    'year 2012': sum(count_crime('/home/polina/projects/class/crime_incident_data_2012.csv').values()),
    'year 2013': sum(count_crime('/home/polina/projects/class/crime_incident_data_2013.csv').values()),
    'year 2014': sum(count_crime('/home/polina/projects/class/crime_incident_data_2014.csv').values()),
    'recent year': sum(count_crime('/home/polina/projects/class/crime_incident_data_recent.csv').values())
}

for k, v in year_summary.items():
    if v == max(year_summary.values()):
        print('The year with most crime is: {}; the total number of crimes committed during this period is: {}.'.format(k,(max(year_summary.values()))))