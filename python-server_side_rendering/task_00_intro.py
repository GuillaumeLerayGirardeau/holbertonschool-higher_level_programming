#!/usr/bin/python3
import os

def generate_invitations(template, attendees):

    if template == None:
        print("Template is empty, no output files generated.")
    elif attendees == None:
        print("No data provided, no output files generated.")
    
    try:
        invit_number = 1
        for i in attendees:
            new_template = template
            new_template = new_template.replace("{name}", i["name"])
            new_template = new_template.replace("{event_title}", i["event_title"])
            new_template = new_template.replace("{event_date}", i["event_date"])
            new_template = new_template.replace("{event_location}", i["event_location"])
            print(new_template)

            if os.path.exists(f'output_{invit_number}.txt'):
                with open(f"output_{invit_number}.txt", "w") as f:
                    f.write(new_template)
            else:
                with open(f"output_{invit_number}.txt", "x") as f:
                    f.write(new_template)

            invit_number += 1
        
    except Exception as e :
        print(e)
