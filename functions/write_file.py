import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    try:
        if not os.path.exists(os.path.dirname(target_file)):
            os.makedirs(target_file)
        with open(target_file, "w") as f:
            f.write(content)
    except Exception as e:
        return f"Error: {e}"
        
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'