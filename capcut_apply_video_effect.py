import json
import uuid
import copy  # Import the copy module for deepcopy functionality

# Function to generate a unique ID
def generate_unique_id():
    return str(uuid.uuid4()).upper()

# Function to add Zoom Lens effect to the input file
def add_zoom_lens_effect(input_json):
    # Load the input JSON data
    data = json.loads(input_json)
    
    # Define the Zoom Lens effect template
    zoom_lens_effect_template = {
        "adjust_params": [
            {
                "default_value": 0.33,
                "name": "effects_adjust_speed",
                "value": 0.03
            },
            {
                "default_value": 0.3,
                "name": "effects_adjust_range",
                "value": 0.3
            }
        ],
        "algorithm_artifact_path": "",
        "apply_target_type": 2,
        "apply_time_range": None,
        "category_id": "1111",
        "category_name": "Video effects",
        "common_keyframes": [],
        "covering_relation_change": 0,
        "disable_effect_faces": [],
        "effect_id": "11326146",
        "formula_id": "",
        "id": "",
        "name": "Zoom Lens",
        "path": "",
        "platform": "all",
        "render_index": 0,
        "request_id": "",
        "resource_id": "6868546663607177736",
        "source_platform": 0,
        "time_range": None,
        "track_render_index": 0,
        "type": "video_effect",
        "value": 1,
        "version": ""
    }

    # Create a new effect track
    effect_track = {
        "attribute": 0,
        "flag": 0,
        "id": generate_unique_id(),  # Generate a unique ID for the effect track
        "is_default_name": True,
        "name": "",
        "segments": [],
        "type": "effect"
    }
    
    # Ensure the "materials" section contains "video_effects"
    if "materials" not in data:
        data["materials"] = {}
    if "video_effects" not in data["materials"]:
        data["materials"]["video_effects"] = []
    
    # Iterate over video tracks and their segments to add corresponding effects
    for track in data.get("tracks", []):
        if track["type"] == "video":
            for i, segment in enumerate(track["segments"]):
                # Create a new effect segment based on the video segment's timing
                effect_segment = {
                    "caption_info": None,
                    "cartoon": False,
                    "clip": None,
                    "common_keyframes": [],
                    "currect_adjust_mask_index": 0,
                    "desc": "",
                    "enable_adjust": False,
                    "enable_adjust_mask": False,
                    "enable_color_correct_adjust": False,
                    "enable_color_curves": True,
                    "enable_color_match_adjust": False,
                    "enable_color_wheels": True,
                    "enable_lut": False,
                    "enable_smart_color_adjust": False,
                    "enable_track_adjust_mask": False,
                    "extra_material_refs": [],
                    "group_id": "",
                    "hdr_settings": None,
                    "id": generate_unique_id(),  # Generate a unique segment ID
                    "intensifies_audio": False,
                    "is_placeholder": False,
                    "is_tone_modify": False,
                    "keyframe_refs": [],
                    "last_nonzero_volume": 1,
                    "material_id": generate_unique_id(),  # Generate a unique material ID
                    "raw_segment_id": "",
                    "render_index": 11001,
                    "responsive_layout": {
                        "enable": False,
                        "horizontal_pos_layout": 0,
                        "size_layout": 0,
                        "target_follow": "",
                        "vertical_pos_layout": 0
                    },
                    "reverse": False,
                    "source_timerange": None,
                    "speed": 1,
                    "target_timerange": segment["target_timerange"],  # Copy time range from video
                    "template_id": "",
                    "template_scene": "default",
                    "track_attribute": 0,
                    "track_render_index": 1,
                    "uniform_scale": None,
                    "visible": True,
                    "volume": 1
                }
                
                # Add effect segment to effect track
                effect_track["segments"].append(effect_segment)
                
                # Create a new video effect in the materials section
                new_effect = copy.deepcopy(zoom_lens_effect_template)
                new_effect["id"] = effect_segment["material_id"]  # Use the same ID as the segment's material_id
                new_effect["path"] = "/Users/huynhnhi/Library/Containers/com.lemon.lvoverseas/Data/Movies/CapCut/User Data/Cache/effect/11326146/6f7b76eec49d46f9397eafb4980a17d4"  # Example path
                data["materials"]["video_effects"].append(new_effect)
    
    # Add the new effect track to the tracks section
    data["tracks"].append(effect_track)
    
    # Return the modified JSON
    return json.dumps(data, indent=4)

# Main function to read input file, process it, and write to output file
def process_input_file(input_file, output_file):
    # Read the input file
    with open(input_file, 'r') as infile:
        input_json = infile.read()
    
    # Process the input to add Zoom Lens effect
    output_json = add_zoom_lens_effect(input_json)
    
    # Write the output to a new file
    with open(output_file, 'w') as outfile:
        outfile.write(output_json)
    
    print(f"Processed file saved as {output_file}")

# Example usage
input_file = 'input.json'
output_file = 'output.json'
process_input_file(input_file, output_file)
