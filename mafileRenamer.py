import os
import json


def rename_files(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            with open(filepath, 'r') as file:

                data = json.load(file)

                if 'account_name' in data:

                    new_filename = data['account_name'] + '.maFile'

                    new_filepath = os.path.join(directory, new_filename)

                    file.close()
                    os.rename(filepath, new_filepath)
                    print(f'{filename} renamed to {new_filename}')
                else:
                    print(f'Error in {filename}')


directory_path = 'mafiles'
rename_files(directory_path)
