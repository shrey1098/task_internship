from os import stat
from pwd import getpwuid
import csv
import os.path, time


# Function takes directory path and output file name (without .csv extension) as parameters
def file_metadata(dir_path: str, output_file: str):
    arr = os.listdir(dir_path)
    output = output_file + ".csv"
    with open(output, 'a') as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Filename', 'Filetype', 'Size(in Bytes)', 'Author', 'Last Modified',
                         'Created', 'Last Accessed'])

    for file in arr:
        filename, file_extension = os.path.splitext(file)
        size = os.path.getsize(dir_path + "/" + file)
        author = getpwuid(stat(dir_path + "/" + file).st_uid).pw_name
        modify_date = time.ctime(os.path.getmtime(dir_path + "/" + file))
        create_date = time.ctime(os.path.getctime(dir_path + "/" + file))
        access_date = time.ctime(os.path.getatime(dir_path + "/" + file))

        with open(output, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(
                [filename, file_extension, size, author, modify_date, create_date, access_date])

    return output


