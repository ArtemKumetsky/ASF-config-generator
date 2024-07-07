import json
import os
import shutil

# create variables
global log_data, pass_data
logpass_path = 'logpass.txt'
mafiles_folder = 'mafiles'
master_id = PRINT YOUR MASTER STEAMID64 HERE
template = {
    "Enabled": True,
    "SteamLogin": "",
    "SteamPassword": "",
    "AcceptGifts": True,
    "SteamUserPermissions": {
        f"{master_id}": 3
    },
    "FarmingPreferences": 128
}

# create folder for result
output_dir = "config"
os.makedirs(output_dir, exist_ok=True)
# create || clear report file
with open("report.txt", "w") as report_file:
    pass


# create jsons
def create_jsons(login, password):
    user_json = template.copy()
    user_json["SteamLogin"] = login
    user_json["SteamPassword"] = password

    file_name = f"{login}.json"
    file_path = os.path.join(output_dir, file_name)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(user_json, f, ensure_ascii=False, indent=4)

    print(f"Created {file_path}")


def check_mafiles(login, mafiles_folder, output_dir):
    mafile_path = os.path.join(mafiles_folder, f"{login}.mafile")
    if not os.path.exists(mafile_path):
        print(f"File {mafile_path} not found.")
        with open("report.txt", "a+") as report_file:
            report_file.write(f"{login}.mafile not found\n")
    else:
        shutil.move(mafile_path, output_dir)


# get separate logins and passwords from logpass.txt
def split_acc_data(logpass_path):
    global log_data, pass_data
    with open(logpass_path, 'r') as infile:
        log_data = []
        pass_data = []

        for line in infile:
            login, password = line.strip().split(':')
            create_jsons(login, password)
            check_mafiles(login, mafiles_folder, output_dir)


split_acc_data(logpass_path)

print("All files have been created.")
