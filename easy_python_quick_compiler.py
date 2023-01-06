import os
import shutil


def remove_folder(folder_name):
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)


def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)


def dot_py_to_dot_exe(string):
    return f'{string.split(".")[0]}.exe'


def file_path_to_file(string):
    return string.split("\\").pop()


def delete_ends_with(directory,string_endswith):
    files = os.listdir(directory)
    for file2 in files:
        if file2.endswith(f".{string_endswith}"):
            os.remove(file2)


def remote_compile(file):
    command = f'pyinstaller --noconfirm --onefile --console  "{file}"'
    print(f'running command:\n{command}')
    os.system(command)
    with open(dot_py_to_dot_exe(f'dist/{file_path_to_file(file)}'), 'rb') as f:
        binary = f.read()

    remove_folder('dist')
    remove_folder('build')
    delete_ends_with(os.getcwd(), 'spec')
    return binary


def local_compile(file):
    dir = f'"{os.getcwd()}\\{file}"'
    command = f'pyinstaller --noconfirm --onefile --console  {dir}'
    print(f'running command:\n{command}')
    os.system(command)
    with open(dot_py_to_dot_exe(f'dist/{file}'), 'rb') as f:
        binary = f.read()

    remove_folder('dist')
    remove_folder('build')
    return binary


file = input('Enter file path of file to compile, or only file name if file is in the same directory as me:\n')
if '\\' in file:
    with open(dot_py_to_dot_exe(file), 'wb') as f:
        f.write(remote_compile(file))

    print(f'Compiled file was saved to {dot_py_to_dot_exe(file)}')

else:
    with open(dot_py_to_dot_exe(file), 'wb') as f:
        f.write(local_compile(file))

    print(f'Compiled file was saved to {os.getcwd()}\\{dot_py_to_dot_exe(file)}')
