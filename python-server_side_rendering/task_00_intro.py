#!/usr/bin/python3

import os


def generate_invitations(template, attendees):
    ''' a Python function that generates personalized invitation files from a
    template with placeholders and a list of objects.
    Arguments:
    template: text with placeholders
    attendees: a list of dictionaries
    return: Error on failure, nothing on success.'''

    if not isinstance(template, str) or not isinstance(attendees, list):
        print('template must be a string and attendees a list of'
              'dictionaries.')
        return

    elif len(template) <= 0:
        print('Template is empty, no output files generated.')
        return

    elif len(attendees) <= 0:
        print('No data provided, no output files generated.')
        return

    dict_model = ['name', 'event_title', 'event_date', 'event_location']

    for invite in attendees:
        if not isinstance(invite, dict):
            print('template must be a string and attendees a list'
                  ' of dictionaries.')
            return
        for key in dict_model:
            if key not in invite or invite[key] is None:
                invite[key] = 'N/A'
    try:
        i = 0
        for attendee in attendees:
            i += 1
            with open(
                    f'output_{i}.txt', 'w', encoding='utf-8') as invitation:
                invitation.write(template.format(**attendee))

    except Exception:
        raise