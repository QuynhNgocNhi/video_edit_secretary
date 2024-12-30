import re

def srt_to_text(srt_file, text_file):
    with open(srt_file, 'r', encoding='utf-8') as file:
        srt_content = file.readlines()

    # Regular expression to match SRT timing lines and empty lines
    timing_regex = re.compile(r'^\d{1,2}:\d{2}:\d{2},\d{3}')
    output_text = []

    for line in srt_content:
        line = line.strip()
        # Skip lines that are empty, numbers, or timing lines
        if not line or line.isdigit() or timing_regex.match(line):
            continue
        output_text.append(line)

    # Write the extracted text to a new file
    with open(text_file, 'w', encoding='utf-8') as output_file:
        output_file.write("\n".join(output_text))

# Example usage
srt_to_text('subtitles.srt', 'subtitles.txt')
