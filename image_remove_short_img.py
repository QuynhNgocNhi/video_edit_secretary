import os
from PIL import Image
from send2trash import send2trash

# Specify the main folder containing the chapter folders
main_folder_path = './i-cant-wait-to-eat-you'

# Specify the range of chapters to process (inclusive)
start_chapter = 0
end_chapter = 2 # Change this to your desired ending chapter

# Loop through the specified range of chapter numbers
for chapter_number in range(start_chapter, end_chapter + 1):
    chapter_folder = f'chapter-{chapter_number}'
    chapter_path = os.path.join(main_folder_path, 'all_images')
    
    # Check if the chapter folder exists
    if os.path.isdir(chapter_path):
        print(f'Processing folder: {chapter_folder}')
        
        # Loop through all files in the chapter folder
        for filename in os.listdir(chapter_path):
            file_path = os.path.join(chapter_path, filename)
            
            # Check if the file is an image
            try:
                with Image.open(file_path) as img:
                    # Check the height of the image
                    if img.height < 300:
                        send2trash(file_path)  # Move the image to trash
                        print(f'Moved to trash: {filename} from {chapter_folder}')
            except Exception as e:
                print(f'Error processing {filename} in {chapter_folder}: {e}')
    else:
        print(f'Folder not found: {chapter_folder}')

# # Loop through the specified range of chapter numbers
# for chapter_number in range(start_chapter, end_chapter + 1):
#     chapter_folder = f'chapter-{chapter_number}'
#     chapter_path = os.path.join(main_folder_path, chapter_folder)
    
#     # Check if the chapter folder exists
#     if os.path.isdir(chapter_path):
#         print(f'Processing folder: {chapter_folder}')
        
#         # Loop through all files in the chapter folder
#         for filename in os.listdir(chapter_path):
#             file_path = os.path.join(chapter_path, filename)
            
#             # Check if the file is an image
#             try:
#                 with Image.open(file_path) as img:
#                     # Check the height of the image
#                     if img.height < 200:
#                         os.remove(file_path)  # Remove the image
#                         print(f'Removed: {filename} from {chapter_folder}')
#             except Exception as e:
#                 print(f'Error processing {filename} in {chapter_folder}: {e}')
#     else:
#         print(f'Folder not found: {chapter_folder}')



# import os
# from PIL import Image

# # Specify the folder containing the images
# folder_path = './test_output'

# # Loop through all files in the folder
# for filename in os.listdir(folder_path):
#     file_path = os.path.join(folder_path, filename)
    
#     # Check if the file is an image
#     try:
#         with Image.open(file_path) as img:
#             # Check the height of the image
#             if img.height < 200:
#                 os.remove(file_path)  # Remove the image
#                 print(f'Removed: {filename}')
#     except Exception as e:
#         print(f'Error processing {filename}: {e}')
