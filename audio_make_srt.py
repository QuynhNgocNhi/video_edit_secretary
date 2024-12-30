import datetime

def seconds_to_timecode(seconds):
    td = datetime.timedelta(seconds=seconds)
    total_seconds = td.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    secs = int(total_seconds % 60)
    milliseconds = int((total_seconds % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{milliseconds:03}"

# Function to split text if it's too long
def split_long_line(text, max_chars=125):
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 > max_chars:  # +1 for space
            lines.append(current_line)
            current_line = word
        else:
            if current_line:
                current_line += " "
            current_line += word

    if current_line:
        lines.append(current_line)

    return lines

# Read the subtitles from the text file
with open('subtitles.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

current_time = 0.0  # Start time in seconds
srt_output = ''
gap = 0.5  # Gap between subtitles in seconds (adjust as needed)

for idx, line in enumerate(lines):
    line = line.strip()
    if not line:
        continue  # Skip empty lines

    # Split long lines into smaller ones
    split_lines = split_long_line(line)

    for sub_line in split_lines:
        word_count = len(sub_line.split())
        duration = word_count / 2.5  # Duration in seconds (1 word = ~0.4 seconds)

        start_time = current_time
        end_time = current_time + duration

        # Format the start and end times
        start_timecode = seconds_to_timecode(start_time)
        end_timecode = seconds_to_timecode(end_time)

        # Build the SRT entry
        srt_output += f"{idx + 1}\n"
        srt_output += f"{start_timecode} --> {end_timecode}\n"
        srt_output += f"{sub_line}\n\n"

        # Update the current time for the next subtitle (including the gap)
        current_time = end_time + gap

# Write the SRT output to a file
with open('subtitles.srt', 'w', encoding='utf-8') as f:
    f.write(srt_output)
