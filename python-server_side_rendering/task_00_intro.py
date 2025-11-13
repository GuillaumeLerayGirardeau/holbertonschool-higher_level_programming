#!/usr/bin/python3


import os

"""
Template function that generates invitations
"""


def generate_invitations(template, attendees):
    """
    Python function that generate a invitation
    """

    if template is None:
        print("Template is empty, no output files generated.")
        return
    elif not isinstance(template, str) or not isinstance(attendees, list):
        print("Template must be a string and attendees a list of dictionaries")
        return
    elif attendees is None:
        print("No data provided, no output files generated.")
        return

    needed_keys = ["name", "event_title", "event_date", "event_location"]

    for dictionary in attendees:
        if not isinstance(dictionary, dict):
            print("Attendees must be a list of dictionaries")
            return
        for key in dictionary:
            if key not in needed_keys or dictionary[key] is None:
                dictionary[key] = "N/A"

    for dictionary in attendees:
        for key in dictionary:
            if dictionary[key] is None:
                dictionary[key] = "N/A"

    try:
        invit_number = 1
        for attendee in attendees:
            with open(f"output_{invit_number}.txt", "w") as f:
                f.write(template.format(**attendee))

            invit_number += 1

    except Exception as e:
        print(e)
