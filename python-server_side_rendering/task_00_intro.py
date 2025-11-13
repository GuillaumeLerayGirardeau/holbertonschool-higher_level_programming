#!/usr/bin/python3
import os

"""
Template function that generates invitations
"""

def generate_invitations(template, attendees):

    if template == None:
        print("Template is empty, no output files generated.")
    elif type(template) is not str:
        print(f"Error: template is {type(template)} and not str")
        return
    elif attendees == None:
        print("No data provided, no output files generated.")
    elif type(attendees) is not list:
        print(f"Error: attendees is {type(attendees)} and not list")
        return
    else:
        for element in attendees:
            if type(element) is not dict:
                print(f"Error: attendees is a list with {type(element)} and not only dictionaries")
                return



    for dictionary in attendees:
        for key in dictionary:
            if dictionary[key] == None:
                dictionary[key] = "N/A"
    
    try:
        invit_number = 1
        for i in attendees:
            new_template = template
            new_template = new_template.replace("{name}", i["name"])
            new_template = new_template.replace("{event_title}", i["event_title"])
            new_template = new_template.replace("{event_date}", i["event_date"])
            new_template = new_template.replace("{event_location}", i["event_location"])

            if os.path.exists(f'output_{invit_number}.txt'):
                with open(f"output_{invit_number}.txt", "w") as f:
                    f.write(new_template)
            else:
                with open(f"output_{invit_number}.txt", "x") as f:
                    f.write(new_template)

            invit_number += 1
        
    except Exception as e :
        print(e)
