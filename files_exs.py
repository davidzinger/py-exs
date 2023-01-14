import os
import hashlib


def hashing(file_path):

    with open(file_path, 'rb') as opened_file:
        content = opened_file.read()
        sha256 = hashlib.sha256()
        sha256.update(content)
        opened_file.close()
        return '{}: {}'.format(sha256.name, sha256.hexdigest())


def check_name(file1, file2):
    if file1[:-3] == file2[:-3] and file2.endswith("sha256"):
        return False
    else:
        return True


def main(dir_path):

    for file1 in os.listdir(dir_path):

        if file1.endswith("exe"):

            for file2 in os.listdir(dir_path):

                if check_name(file1, file2):
                    sha256 = hashing(dir_path + '\\' + file1)
                    new_file_name = file1[:-3] + "sha256"
                    f = open(dir_path + '\\' + new_file_name, "w")
                    f.write(sha256)
                    f.close()

#before running create test floder
main(r"C:\Users\david\OneDrive\Desktop\test")





