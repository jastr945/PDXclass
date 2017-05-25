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

# with open('/home/polina/projects/class/crime_incident_data_2011.csv','r') as text:
#
#     original_dict = csv.DictReader(text)
#     # for line in original_dict:
#     #     print(line['Major Offense Type'])
#
#     new_dict = {}
#
#     for line in original_dict:
#         if line['Major Offense Type'] in new_dict:
#             new_dict[line['Major Offense Type']] += 1
#         else:
#             new_dict[line['Major Offense Type']] = 1
#
#     text_return = ""
#     for k, v in new_dict.items():
#         text_return += '{}: {}\n'.format(k,v)
#     print(text_return)



def count_crime(crime_incident_data):
    with open(crime_incident_data, 'r') as text:

        original_dict = csv.DictReader(text)

        new_dict = {}

        for line in original_dict:
            if line['Major Offense Type'] in new_dict:
                new_dict[line['Major Offense Type']] += 1
            else:
                new_dict[line['Major Offense Type']] = 1

        text_return = ""
        for k, v in new_dict.items():
            text_return += '{}: {}\n'.format(k, v)
        print(text_return)

year_2011 = count_crime('/home/polina/projects/class/crime_incident_data_2011.csv')
print(year_2011)

year_2012 = count_crime('/home/polina/projects/class/crime_incident_data_2012.csv')
print(year_2012)

year_2013 = count_crime('/home/polina/projects/class/crime_incident_data_2013.csv')
print(year_2013

year_2014 = count_crime('/home/polina/projects/class/crime_incident_data_2014.csv')
print(year_2014)

recent_data = count_crime('/home/polina/projects/class/crime_incident_data_recent.csv')
print(recent_data)


# /home/polina/projects/class/crime_incident_data_2012.csv
# /home/polina/projects/class/crime_incident_data_2013.csv
# /home/polina/projects/class/crime_incident_data_2014.csv
# /home/polina/projects/class/crime_incident_data_recent.csv



