import os
import hashlib
from projects import PROJECTS, PROJECTS_DEMO
from utils import delete_dir, create_dir, git_clone, is_file_valid
from file_hash import FileHash
from project_file_save import ProjectFileSave


md5_hash = hashlib.md5()

EXCLUDE_DIRS = ['.vscode', 'node_modules', 'log', '.git', 'dist', '.idea', '.nvmrc', '.DS_Store', '__pycache__', 'coverage', '.nyc_output']
EXCLUDE_FILES = ['.gitignore', '.cfignore', 'package-lock.json', '.directory', 'README.md', '.nyc_output']
EXCLUDE_EXTENSION = ['.jpg', '.png', '.jpeg', '.md', '.swap', '.opts', '.log', '.svg', '.pdf', '.otf', '.ttf', '.eot',
                     '.woff2', '.woff', '.gif', '.psd', '.xls', '.xlsx']
CLONE_DIR = './repositories'
OUTPUT_DIR = './output/'


delete_dir(dir_path=CLONE_DIR)
delete_dir(dir_path=OUTPUT_DIR)
create_dir(dir_path=CLONE_DIR)
create_dir(dir_path=OUTPUT_DIR)

for project in PROJECTS:
    project_base_dirs = []
    project_base_files = []
    project_exclude_files = EXCLUDE_FILES + project["exclude_extension"]
    project_exclude_extension = EXCLUDE_EXTENSION + project["exclude_extension"]

    clone_repository_dir = os.path.join(CLONE_DIR, project["name"])
    git_clone(CLONE_DIR, project["repository"])
    for item in os.listdir(clone_repository_dir):
        item_path = os.path.join(clone_repository_dir, item)
        if os.path.isdir(item_path):
            if item not in EXCLUDE_DIRS:
                project_base_dirs.append(item_path)

        if os.path.isfile(item_path):
            if is_file_valid(item, project_exclude_files, project_exclude_extension):
                project_base_files.append(item_path)

    for base_dir in project_base_dirs:
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                if is_file_valid(file, project_exclude_files, project_exclude_extension):
                    project_base_files.append(os.path.join(root, file))
    project_output = ''
    for file in project_base_files:
        file_hash = str(FileHash(file_path=file))
        project_output = ''.join([project_output, file_hash, "\n"])

    ProjectFileSave(project, project_output).save()
