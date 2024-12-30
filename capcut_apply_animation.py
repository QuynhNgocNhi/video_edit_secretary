import json

# Function to apply "Zoom In" animation to all videos
def apply_zoom_in_animation(input_json):
    # Parse the input JSON
    data = json.loads(input_json)

    # Define the "Zoom In" animation template
    zoom_in_animation_template = {
        "anim_adjust_params": None,
        "category_id": "6825",
        "category_name": "Out",
        "id": "670504",
        "material_type": "video",
        "name": "Zoom In",
        "panel": "video",
        "path": "/Users/huynhnhi/Library/Containers/com.lemon.lvoverseas/Data/Movies/CapCut/User Data/Cache/effect/670504/01497dc221d288e623a10cac94a5ceca",
        "platform": "all",
        "request_id": "",
        "resource_id": "6798332801864176142",
        "type": "out"
    }

    # Loop through each video in the "videos" section
    for video in data['materials']['videos']:
        # Find the corresponding segment duration for this video in the tracks section
        for track in data['tracks']:
            for segment in track['segments']:
                if segment['material_id'] == video['id']:
                    # Set the animation duration based on the segment duration
                    animation_duration = segment['source_timerange']['duration']
                    
                    # Create the animation data for this video
                    zoom_in_animation = zoom_in_animation_template.copy()
                    zoom_in_animation['duration'] = animation_duration
                    zoom_in_animation['start'] = 0

                    # Apply the animation to the corresponding "material_animations" section
                    for animation in data['materials']['material_animations']:
                        if animation['id'] in segment['extra_material_refs']:
                            animation['animations'].append(zoom_in_animation)

    # Return the modified JSON as a string
    return json.dumps(data, indent=4)

# Main function to read the input file, process it, and write the output file
def process_json_file(input_file_path, output_file_path):
    # Read the input JSON file
    with open(input_file_path, 'r') as infile:
        input_json = infile.read()

    # Apply the Zoom In animation logic
    output_json = apply_zoom_in_animation(input_json)

    # Write the output JSON to a new file
    with open(output_file_path, 'w') as outfile:
        outfile.write(output_json)

    print(f"Processed JSON has been written to {output_file_path}")

# Example usage: specify the input and output file paths
if __name__ == "__main__":
    input_file = 'input.json'  # Replace with your input file path
    output_file = 'output.json'  # Replace with your desired output file path

    process_json_file(input_file, output_file)
