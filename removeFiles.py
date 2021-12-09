import time
import os
import shutil

path = "/Users/mayashah/Desktop/Coding/Python/Project 99/Tester"

seconds = time.time()-3600

def get_file_or_folder_age(path):
    ctime = os.stat(path).st_ctime
    return ctime

def remove_file(path):
    if not os.remove(path):
        print("Removed successfully", path)
    else:
        print("Unable to delete", path)

def remove_folder(path):
    if not shutil.rmtree(path):
        print("Removed Successfully", path)
    else:
        print("Unable to delete", path)


def main():
    deletedFolderCount = 0
    deletedFilesCount = 0

    if os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            if seconds >= get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                deletedFolderCount = deletedFolderCount+1
                break
            else:
                for i in folders:
                    folderPath = os.path.join(root_folder, i)
                    if seconds >= get_file_or_folder_age(folderPath):
                        remove_folder(folderPath)
                        deletedFolderCount = deletedFolderCount+1
                for i in files:
                    filePath = os.path.join(root_folder, i)
                    if seconds >= get_file_or_folder_age(filePath):
                        remove_folder(filePath)
                        deletedFilesCount = deletedFilesCount+1
        else:
            if seconds >= os.get_file_or_folder_age(path):
                os.remove_file(path)
                deletedFilesCount = deletedFilesCount+1
    else:
        print('The given path does not exist')

    print('Total folders deleted: ', deletedFolderCount)
    print('Total files deleted: ', deletedFilesCount)
    

main()

