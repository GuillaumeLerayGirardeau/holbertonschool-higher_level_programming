#!/usr/bin/python3


import os

"""
Template function that generates invitations
"""


def generate_invitations(template, attendees):

    if template is None:
        print("Template is empty, no output files generated.")
        return
    elif not isinstance(template, str):
        print(f"Error: template is {type(template)} and not str")
        return
    elif attendees is None:
        print("No data provided, no output files generated.")
        return
    elif not isinstance(attendees, list):
        print(f"Error: attendees is {type(attendees)} and not list")
        return
    else:
        for element in attendees:
            if type(element) is not dict:
                print(f"Error: attendees is a list with \
                      {type(element)} and not only dictionaries")
                return

    needed_keys = ["name", "event_title", "event_date", "event_location"]

    for dictionary in attendees:
        for keys in needed_keys:
            if keys not in dictionary:
                dictionary[keys] = "N/A"
        for key in dictionary:
            if dictionary[key] is None:
                dictionary[key] = "N/A"

    try:
        invit_number = 1
        for i in attendees:
            new_template = template
            new_template = new_template.replace("{name}", i["name"])
            new_template = new_template.replace(
                "{event_title}", i["event_title"])
            new_template = new_template.replace(
                "{event_date}", i["event_date"])
            new_template = new_template.replace(
                "{event_location}", i["event_location"])

            with open(f"output_{invit_number}.txt", "w") as f:
                f.write(new_template)

            invit_number += 1

    except Exception as e:
        print(e)
