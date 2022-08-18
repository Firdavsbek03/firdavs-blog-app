with open("requirements.txt") as file_name:
    data=file_name.readlines()
with open("requirements.txt", "w") as file_name:
    for module in data:
        file_name.write(f"{module.split('=')[0]}\n")