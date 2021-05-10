import os
import shutil
import git


def delete_dir(dir_path):
    try:
        shutil.rmtree(dir_path)
    except OSError as e:
        print("Error: %s : %s" % (dir_path, e.strerror))
    else:
        print("Successfully delete the directory %s " % dir_path)


def create_dir(dir_path):
    try:
        os.mkdir(dir_path)
    except OSError:
        print("Creation of the directory %s failed" % dir_path)
    else:
        print("Successfully created the directory %s " % dir_path)


def git_clone(clone_dir, repostiry):
    git.Git(clone_dir).clone(repostiry)
    print("Successfully clone the repository %s " % repostiry)


def is_file_valid(file_name, exclude_files, exclude_extension):
    return not (file_name in exclude_files or file_name.lower().endswith(tuple(exclude_extension)))
