'''

Polina Jastrzebska

Module Docstring

PEP 257

>>> scrub_numbers('Be9autiful9 i4s be2tter th4an ug42ly')
'Beautiful is better than ugly.'

>>> gentle_clean('Explicit_is-better_than -implicit')
'Explicit is better than implicit.'

>>> clean_data('  42Simple-is_better_than-compl9ex   ')
'Simple is better than complex.'

>>> some_scrubber('F l a t   i s   b e t t e r   t h a n   n e s t e d . ')
'Flat is better than nested.'

>>> mr_clean('Sparse is better than dense')
' S p a r s e   i s   b e t t e r   t h a n   d e n s e '

>>> ms_clean('Readability counts')
'R9y c4s'

>>> strong_cleaner('Err@#%$ors sho@#$@#$uld nev1!$#@er pass sile&I&&*(ntly')
'Errors should never pass silently.'

>>> extracto('1S2pe3cia4l ca5ses ar6en't sp7ecial en8ough to b9reak the r0ules.')
45

'''

import re


def scrub_numbers(raw_data: str):  # take a string and return a string
    """
    This function takes a string and removes all numbers.
    Then returnes the cleaned string.
    """

    cleaned = re.sub('\d', '', raw_data)
    return cleaned


print(scrub_numbers('Be9autiful9 i4s be2tter th4an ug42ly'))


def gentle_clean(raw_data: str):
    '''
   This function removes all '-' and '_' and return a clear string.

    '''

    cleaned = re.sub('\s{2}', ' ', (re.sub('[-_]', ' ', raw_data)))
    return cleaned


print(gentle_clean('Explicit_is-better_than -implicit'))


def clean_data(raw_data: str):
    '''

    This function removes extra spaces at the beginning and the end of the string, removes numbers,
    replaces '-' and '_' characters with single spaces.
    '''

    cleaned = re.sub('[_-]',' ',(re.sub('[\s\d]','',raw_data)))
    return cleaned


print(clean_data('  42Simple-is_better_than-compl9ex   '))


def some_scrubber(raw_data: str):
    '''

    This function removes spaces where they are not needed and keeps them where they are needed.
    '''


    cleaned = re.sub(r'\s+',' ',(re.sub(r'(?<=\w)\s(?=.)','',raw_data)))
    return cleaned


print(some_scrubber('F l a t   i s   b e t t e r   t h a n   n e s t e d . '))


def mr_clean(raw_data: str):
  '''
  This function adds additional spaces before and after each character.
  '''


  cleaned = re.sub(r'$',' ',(re.sub(r'(^)',' ',(re.sub(r'(?=\w)(?<=\w)',' ',(re.sub(r'\s', '   ', raw_data)))))))
  return cleaned


print(mr_clean('Sparse is better than dense'))


def ms_clean(raw_data: str):
    '''

    This function leaves every first and last letter of the word ad replaces the middle with a number.
    '''

    cleaned = re.sub('[ount]{4}','4',(re.sub('[eadabilit]{9}','9',raw_data)))
    return cleaned


print(ms_clean('Readability counts'))


def strong_cleaner(raw_data: str):
    '''

    This function removes all special characters from the string.
    '''


    cleaned = re.sub(r'$','.',(re.sub('[@#$%$!&*(\dI]','',raw_data)))
    return cleaned


print(strong_cleaner('Err@#%$ors sho@#$@#$uld nev1!$#@er pass sile&I&&*(ntly'))


def extracto(raw_data: str):
    '''

    This function extract two numbers from the string and returns their sum.
    '''


    cleaned = list((re.sub('[a-zA-Z\s\.\']+','',raw_data)))

    nums = [int(x) for x in cleaned]

    return(sum(nums))


print(extracto("1S2pe3cia4l ca5ses ar6en't sp7ecial en8ough to b9reak the r0ules."))
print(extracto("3S6pe9cia2l ca5ses ar8en't sp1ecial en4ough to b7reak the r0ules."))
print(extracto("2S4pe6cia8l ca0ses ar2en't sp4ecial en6ough to b8reak the r0ules."))