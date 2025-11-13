#!/usr/bin/python3

import os


def generate_invitations(template, attendees):
    ''' 
    Python function that generate invitation from a template
    '''

    if not isinstance(template, str) or not isinstance(attendees, list):
        print('template must be a string and attendees a list of'
              'dictionaries.')
        return

    elif template is None or len(template) <= 0:
        print('Template is empty, no output files generated.')
        return

    elif len(attendees) <= 0 or attendees is None:
        print('No data provided, no output files generated.')
        return

    dict_model = ['name', 'event_title', 'event_date', 'event_location']

    for dictionary in attendees:
        if not isinstance(dictionary, dict):
            print('template must be a string and attendees a list'
                  ' of dictionaries.')
            return
        for key in dict_model:
            if key not in dictionary or dictionary[key] is None:
                dictionary[key] = 'N/A'
    try:
        i = 0
        for dictionary in attendees:
            i += 1
            with open(
                    f'output_{i}.txt', 'w', encoding='utf-8') as invitation:
                invitation.write(template.format(**dictionary))

    except Exception:
        raise