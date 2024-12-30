import os
from PIL import Image
import glob
import re
from datetime import datetime

# Helper function to extract numbers from the image filenames for sorting
def extract_number(filename):
    numbers = re.findall(r'\d+', filename)
    return int(numbers[0]) if numbers else 0

# Function to split images in each chapter folder and save all in one folder
def split_images_in_one_folder(parent_folder, output_folder, start_chapter, end_chapter, images_per_scene=7):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Loop through each chapter folder
    for chapter_num in range(start_chapter, end_chapter + 1):
        # Define the path for the current chapter folder inside the parent folder
        chapter_folder_path = os.path.join(parent_folder, f'chapter-{chapter_num}')
        
        # Check if the folder exists
        if not os.path.exists(chapter_folder_path):
            print(f"Folder {chapter_folder_path} does not exist. Skipping...")
            continue
        
        # Get all image files in the chapter folder (adjust the extension as needed)
        image_files = glob.glob(f'{chapter_folder_path}/*.jpg')  # Assumes images are .jpg, adjust if necessary
        
        # Sort the image files numerically by their filenames
        image_files.sort(key=lambda x: extract_number(os.path.basename(x)))
        
        # Get the current timestamp in the format YYYYMMDD_HHMMSS
        current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Process each image in the folder, including an index for image numbering
        for image_index, image_file in enumerate(image_files, start=1):
            # Load the image
            image = Image.open(image_file)
            width, height = image.size
            
            # Calculate the height of each scene
            scene_height = height // images_per_scene
            
            # Split the image into scenes
            for i in range(images_per_scene):
                # Crop the scene from the image
                scene = image.crop((0, i * scene_height, width, (i + 1) * scene_height))
                
                # Generate a new name for the scene image including the chapter, image number, scene number, and timestamp
                scene_name = f'chapter-{chapter_num}_image_{image_index}_scene_{i+1}_{current_time}.jpg'
                
                # Save the scene into the output folder
                scene.save(os.path.join(output_folder, scene_name))
            
            print(f"Processed {image_file} into {images_per_scene} scenes.")

# Set the path to the parent folder where your chapter folders are located
parent_folder = './i-cant-wait-to-eat-you/'  # Replace with the actual path to your folder containing chapter folders

# Set the path to the output folder where all images will be saved
output_folder = os.path.join(parent_folder, 'all_images')  # All images will be saved in this folder

# Set the start and end chapter numbers
start_chapter = 3  # Adjust based on the first chapter
end_chapter = 60  # Adjust based on the last chapter

# Call the function to split images and save all in one folder
split_images_in_one_folder(parent_folder, output_folder, start_chapter, end_chapter, images_per_scene=7)

print("Processing complete! All images saved to:", output_folder)


# import os
# from PIL import Image
# import glob
# import re
# from datetime import datetime

# # Helper function to extract numbers from the image filenames for sorting
# def extract_number(filename):
#     numbers = re.findall(r'\d+', filename)
#     return int(numbers[0]) if numbers else 0

# # Function to split images in each chapter folder and save all in one folder
# def split_images_in_one_folder(parent_folder, output_folder, start_chapter, end_chapter, images_per_scene=7):
#     # Create the output folder if it doesn't exist
#     os.makedirs(output_folder, exist_ok=True)
    
#     # Get the current timestamp in the format YYYYMMDD_HHMMSS
#     current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    
#     # Loop through each chapter folder
#     for chapter_num in range(start_chapter, end_chapter + 1):
#         # Define the path for the current chapter folder inside the parent folder
#         chapter_folder_path = os.path.join(parent_folder, f'chapter-{chapter_num}')
        
#         # Check if the folder exists
#         if not os.path.exists(chapter_folder_path):
#             print(f"Folder {chapter_folder_path} does not exist. Skipping...")
#             continue
        
#         # Get all image files in the chapter folder (adjust the extension as needed)
#         image_files = glob.glob(f'{chapter_folder_path}/*.jpg')  # Assumes images are .jpg, you can adjust as needed
        
#         # Sort the image files numerically by their filenames
#         image_files.sort(key=extract_number)
        
#         # Process each image in the folder, including an index for image numbering
#         for image_index, image_file in enumerate(image_files, start=1):
#             # Load the image
#             image = Image.open(image_file)
#             width, height = image.size
            
#             # Calculate the height of each scene
#             scene_height = height // images_per_scene
            
#             # Split the image into scenes
#             for i in range(images_per_scene):
#                 # Crop the scene from the image
#                 scene = image.crop((0, i * scene_height, width, (i + 1) * scene_height))
                
#                 # Generate a new name for the scene image including the chapter, image number, scene number, and timestamp
#                 original_image_name = os.path.basename(image_file).split('.')[0]  # Get the base image name without extension
#                 scene_name = f'chapter-{chapter_num}_image_{image_index}_scene_{i+1}_{current_time}.jpg'
                
#                 # Save the scene into the output folder
#                 scene.save(os.path.join(output_folder, scene_name))
            
#             print(f"Processed {image_file} into {images_per_scene} scenes.")

# # Set the path to the parent folder where your chapter folders are located
# parent_folder = './i-cant-wait-to-eat-you/'   # Replace with the actual path to your folder containing chapter folders

# # Set the path to the output folder where all images will be saved
# output_folder = os.path.join(parent_folder, 'all_images')  # All images will be saved in this folder

# # Set the start and end chapter numbers
# start_chapter = 1  # Adjust based on the first chapter
# end_chapter = 6    # Adjust based on the last chapter

# # Call the function to split images and save all in one folder
# split_images_in_one_folder(parent_folder, output_folder, start_chapter, end_chapter, images_per_scene=7)

# print("Processing complete! All images saved to:", output_folder)

# import os
# from PIL import Image
# import glob
# import re

# # Helper function to extract numbers from the image filenames for sorting
# def extract_number(filename):
#     numbers = re.findall(r'\d+', filename)
#     return int(numbers[0]) if numbers else 0

# # Function to split images in each chapter folder and save all in one folder
# def split_images_in_one_folder(parent_folder, output_folder, start_chapter, end_chapter, images_per_scene=7):
#     # Create the output folder if it doesn't exist
#     os.makedirs(output_folder, exist_ok=True)
    
#     # Loop through each chapter folder
#     for chapter_num in range(start_chapter, end_chapter + 1):
#         # Define the path for the current chapter folder inside the parent folder
#         chapter_folder_path = os.path.join(parent_folder, f'chapter-{chapter_num}')
        
#         # Check if the folder exists
#         if not os.path.exists(chapter_folder_path):
#             print(f"Folder {chapter_folder_path} does not exist. Skipping...")
#             continue
        
#         # Get all image files in the chapter folder (adjust the extension as needed)
#         image_files = glob.glob(f'{chapter_folder_path}/*.jpg')  # Assumes images are .jpg, you can adjust as needed
        
#         # Sort the image files numerically by their filenames
#         image_files.sort(key=extract_number)
        
#         # Process each image in the folder, including an index for image numbering
#         for image_index, image_file in enumerate(image_files, start=1):
#             # Load the image
#             image = Image.open(image_file)
#             width, height = image.size
            
#             # Calculate the height of each scene
#             scene_height = height // images_per_scene
            
#             # Split the image into scenes
#             for i in range(images_per_scene):
#                 # Crop the scene from the image
#                 scene = image.crop((0, i * scene_height, width, (i + 1) * scene_height))
                
#                 # Generate a new name for the scene image including the chapter, image number, and scene number
#                 original_image_name = os.path.basename(image_file).split('.')[0]  # Get the base image name without extension
#                 scene_name = f'chapter-{chapter_num}_image_{image_index}_scene_{i+1}.jpg'
                
#                 # Save the scene into the output folder
#                 scene.save(os.path.join(output_folder, scene_name))
            
#             print(f"Processed {image_file} into {images_per_scene} scenes.")

# # Set the path to the parent folder where your chapter folders are located
# parent_folder = './i-cant-wait-to-eat-you/'   # Replace with the actual path to your folder containing chapter folders

# # Set the path to the output folder where all images will be saved
# output_folder = os.path.join(parent_folder, 'all_images')  # All images will be saved in this folder

# # Set the start and end chapter numbers
# start_chapter = 1  # Adjust based on the first chapter
# end_chapter = 2    # Adjust based on the last chapter

# # Call the function to split images and save all in one folder
# split_images_in_one_folder(parent_folder, output_folder, start_chapter, end_chapter, images_per_scene=7)

# print("Processing complete! All images saved to:", output_folder)


# import os
# from PIL import Image
# import glob

# # Function to split images in each chapter folder and save all in one folder
# def split_images_in_one_folder(parent_folder, output_folder, start_chapter, end_chapter, images_per_scene=7):
#     # Create the output folder if it doesn't exist
#     os.makedirs(output_folder, exist_ok=True)
    
#     # Loop through each chapter folder
#     for chapter_num in range(start_chapter, end_chapter + 1):
#         # Define the path for the current chapter folder inside the parent folder
#         chapter_folder_path = os.path.join(parent_folder, f'chapter-{chapter_num}')
        
#         # Check if the folder exists
#         if not os.path.exists(chapter_folder_path):
#             print(f"Folder {chapter_folder_path} does not exist. Skipping...")
#             continue
        
#         # Get all image files in the chapter folder (adjust the extension as needed)
#         image_files = glob.glob(f'{chapter_folder_path}/*.jpg')  # Assumes images are .jpg, you can adjust as needed
        
#         # Process each image in the folder, including an index for image numbering
#         for image_index, image_file in enumerate(image_files, start=1):
#             # Load the image
#             image = Image.open(image_file)
#             width, height = image.size
            
#             # Calculate the height of each scene
#             scene_height = height // images_per_scene
            
#             # Split the image into scenes
#             for i in range(images_per_scene):
#                 # Crop the scene from the image
#                 scene = image.crop((0, i * scene_height, width, (i + 1) * scene_height))
                
#                 # Generate a new name for the scene image including the chapter, image number, and scene number
#                 # original_image_name = os.path.basename(image_file).split('.')[0]  # Get the base image name without extension
#                 scene_name = f'chapter-{chapter_num}_image_{image_index}_scene_{i+1}.jpg'
                
#                 # Save the scene into the output folder
#                 scene.save(os.path.join(output_folder, scene_name))
            
#             print(f"Processed {image_file} into {images_per_scene} scenes.")

# # Set the path to the parent folder where your chapter folders are located
# parent_folder = './i-cant-wait-to-eat-you/'  # Replace with the actual path to your folder containing chapter folders

# # Set the path to the output folder where all images will be saved
# output_folder = os.path.join(parent_folder, 'all_images')  # All images will be saved in this folder

# # Set the start and end chapter numbers
# start_chapter = 0  # Adjust based on the first chapter
# end_chapter = 2  # Adjust based on the last chapter

# # Call the function to split images and save all in one folder
# split_images_in_one_folder(parent_folder, output_folder, start_chapter, end_chapter, images_per_scene=7)

# print("Processing complete! All images saved to:", output_folder)



# import os
# from PIL import Image
# import glob

# # Function to split images in each chapter folder into scenes
# def split_images_in_folders(parent_folder, start_chapter, end_chapter, images_per_scene=7):
#     # Loop through each chapter folder
#     for chapter_num in range(start_chapter, end_chapter + 1):
#         # Define the path for the current chapter folder inside the parent folder
#         folder_path = os.path.join(parent_folder, f'chapter-{chapter_num}')
        
#         # Check if the folder exists
#         if not os.path.exists(folder_path):
#             print(f"Folder {folder_path} does not exist. Skipping...")
#             continue
        
#         # Get all image files in the chapter folder (adjust the extension as needed)
#         image_files = glob.glob(f'{folder_path}/*.jpg')  # Assumes images are .jpg, you can adjust as needed
        
#         # Process each image in the folder
#         for image_file in image_files:
#             # Load the image
#             image = Image.open(image_file)
#             width, height = image.size
            
#             # Calculate the height of each scene
#             scene_height = height // images_per_scene
            
#             # Split the image into scenes
#             for i in range(images_per_scene):
#                 # Crop the scene from the image
#                 scene = image.crop((0, i * scene_height, width, (i + 1) * scene_height))
                
#                 # Generate a new name for the scene image (original image name + scene number)
#                 original_image_name = os.path.basename(image_file).split('.')[0]  # Get the base image name without extension
#                 scene_name = f'{original_image_name}_scene_{i+1}.jpg'
                
#                 # Save the scene back into the same folder
#                 scene.save(os.path.join(folder_path, scene_name))
            
#             print(f"Processed {image_file} into {images_per_scene} scenes.")

# # Set the path to the parent folder where your chapter folders are located
# parent_folder = './i-cant-wait-to-eat-you/'  # Replace with the actual path to your folder containing chapter folders

# # Set the start and end chapter numbers
# start_chapter = 1  # Adjust based on the first chapter
# end_chapter = 6    # Adjust based on the last chapter

# # Call the function to split images
# split_images_in_folders(parent_folder, start_chapter, end_chapter, images_per_scene=7)

# print("Processing complete!")

