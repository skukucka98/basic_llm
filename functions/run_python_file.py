import os
import subprocess

def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        process = subprocess.run(["python3", target_file], timeout=30, capture_output=True)
        if not process:
            return "No output produced"
        output = f'STDOUT: {process.stdout}\nSTDERR: {process.stderr}\n'
        if process.returncode != 0:
            output += f'Process exited with code {process.returncode}\n'
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"