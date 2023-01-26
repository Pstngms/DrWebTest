import subprocess


def main():

    drivers_list = subprocess.check_output("driverquery").decode('866')

    with open("file.txt", "w+") as my_file:
        my_file.writelines(drivers_list)

    with open("file.txt") as my_file:
        for line in my_file.readlines():
            if line.startswith("Модуль") or line.startswith("=") or line.find('File System') != -1:
                print(line)


if __name__ == '__main__':
    main()
