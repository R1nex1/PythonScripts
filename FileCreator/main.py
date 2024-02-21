import os

def main():
    base_dir = "Your directory location here"
    start_folder = "Start folder name here"
    end_folder = "End folder name here"
    file_names = ["example.html", "example.css", "examle.js"]
    
    file_creator(base_dir, start_folder, end_folder, file_names)

def file_creator(base_dir, start_folder, end_folder, file_names):
    folder_name_prefix = start_folder.rstrip('0123456789')
    start_number = int(''.join(filter(str.isdigit, start_folder)))
    end_number = int(''.join(filter(str.isdigit, end_folder)))

    for i in range(start_number, end_number + 1):
        folder_name = f"{folder_name_prefix}{i}"
        folder_path = os.path.join(base_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        for file_name in file_names:
            with open(os.path.join(folder_path, file_name), 'w') as file:
                pass

if __name__ == "__main__":
    main()