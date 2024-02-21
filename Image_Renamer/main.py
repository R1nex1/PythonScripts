import os
import re

def main():
    rename_images_in_folder('Your file path here.')

def rename_images_in_folder(folder_path):
    try:
        file_counter = {}
        for filename in os.listdir(folder_path):
            if os.path.isfile(os.path.join(folder_path, filename)):
                # Use regex to remove the UUID and anything after it, including the underscore before it
                base_filename = re.sub(r'_\w{8}-\w{4}-\w{4}-\w{4}-\w{12}.*', '', filename)
                
                # Split and remove the username (first part) and everything after "--stylize" (including "--stylize")
                parts = base_filename.split('_')
                if "--stylize" in parts:
                    parts = parts[1:parts.index("--stylize")]
                else:
                    parts = parts[1:]
                
                new_filename = '_'.join(parts)
                
                # Add counter if filename already exists
                counter = file_counter.get(new_filename, 0) + 1
                file_counter[new_filename] = counter
                new_filename_with_counter = f"{new_filename}_{str(counter).zfill(2)}"
                
                file_extension = os.path.splitext(filename)[1]
                new_file_path = os.path.join(folder_path, f"{new_filename_with_counter}{file_extension}")
                
                os.rename(os.path.join(folder_path, filename), new_file_path)
                print(f"Renamed {filename} to {new_filename_with_counter}{file_extension}")
    except FileNotFoundError as e:
        print(f"Error: {e}. File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()