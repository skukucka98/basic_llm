import os

def get_files_info(working_directory, directory=None):
    abs_working_dir = os.path.abspath(working_directory)
    dir_path = abs_working_dir
    if directory:
        dir_path = os.path.abspath(os.path.join(working_directory, directory))
    
    if not dir_path.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(dir_path):
        return f'Error: "{directory}" is not a directory'
    
    dir_contents = os.listdir(dir_path)
    try:
        files_info = []
        for content in dir_contents:
            path = os.path.abspath(os.path.join(dir_path, content))
            file_size = os.path.getsize(path)
            is_dir = os.path.isdir(path)
            files_info.append(f"- {content}: file_size={file_size} bytes, is_dir={is_dir}")
        
        return "\n".join(files_info)
    
    except Exception as e:
        return f"Error: {e}"