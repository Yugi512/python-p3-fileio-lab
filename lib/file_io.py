def write_file(file_name, file_content):
    
    with open(f"{file_name}.txt",mode="w") as files:
        files.write(file_content)


def append_file(file_name, append_content):
    with open(f"{file_name}.txt",mode="a") as files:
        files.write(append_content)


def read_file(file_name):
    with open(f"{file_name}.txt",mode="r") as files:
       return files.read()

