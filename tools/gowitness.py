import subprocess
from pathlib import Path
import os

def check_folder(folder_path, name):
    is_there = False
    files = [files for path, dirs, files in os.walk(folder_path)][0]
    for file_name in files:
        if name == file_name:
            is_there = True
    return is_there
            

def go_witness(url, path, type = 'png'):
    """insert just path object \n
        type: png or pdf """
    
    Path(path).mkdir(parents=True, exist_ok=True)
    exe_path = str(Path(__file__)).replace('py','exe')
    arguments = ['--disable-db', '--screenshot-path', path, 'single', 'https://' + url]
    
    if type == "pdf":
        arguments.append(f'--{type}')

    for time in range(10):
        if check_folder(path,f'https-{url}.{type}'):
            break
        subprocess.call([exe_path, *arguments])

    if check_folder(path,f'https-{url}.{type}'):
        return f'{path}\\https-{url}.{type}'
    return None


















