import json

# Function to remove gaps between video segments in the "tracks" section
def remove_gaps_from_tracks(tracks):
    for track in tracks:
        # Only process video tracks with segments
        if track.get("segments"):
            previous_end_time = None

            for segment in track["segments"]:
                # Check if the segment has a target_timerange (indicating a video segment)
                if "target_timerange" in segment:
                    # If there is a previous segment, adjust the start time to remove gaps
                    if previous_end_time is not None:
                        segment["target_timerange"]["start"] = previous_end_time

                    # Calculate the end time of the current segment
                    start_time = segment["target_timerange"]["start"]
                    duration = segment["target_timerange"]["duration"]
                    previous_end_time = start_time + duration

    return tracks

# Load JSON from a file
with open('updated_video_editing.json', 'r') as file:
    data = json.load(file)

# Process the "tracks" section
if "tracks" in data:
    data["tracks"] = remove_gaps_from_tracks(data["tracks"])

# Save the updated JSON back to a file
with open('updated_video_editing.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Gaps have been removed and the file has been updated.")
