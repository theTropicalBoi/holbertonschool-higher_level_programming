import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error; Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    
    if not template:
        print("Error: Template is empty, no output files generated.")
        return

    if not attendees:
        print("Error: No data provided, no output files generated.")
        return

    for idx, attendee in enumerate(attendees, 1):
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A") if attendee.get("event_date") is not None else "N/A"
        event_location = attendee.get("event_location", "N/A")

        invitation = template.format(
            name=name,
            event_title=event_title,
            event_date=event_date,
            event_location=event_location
        )

        output_filename = f"output_{idx}.txt"
        
        try:
            if os.path.exists(output_filename):
                print(f"Warning: {output_filename} already exists, overwriting it.")
            
            with open(output_filename, 'w') as file:
                file.write(invitation)
            print(f"Invitation for {name} written to {output_filename}.")
        
        except Exception as e:
            print(f"Error: Failed to write to {output_filename}. {str(e)}")
            continue
