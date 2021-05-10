from datetime import datetime

OUTPUT_DIR = './output/'


class ProjectFileSave:
    def __init__(self, project, project_output):
        self.project = project
        self.output_dir = OUTPUT_DIR
        self.project_output = project_output

    def file_suffix(self):
        return datetime.now().strftime("%m%d%Y%H%M%S")

    def file_name(self):
        suffix = self.file_suffix()
        extension = "csv"
        return f'{self.output_dir}{self.project["name"]}_{suffix}.{extension}'

    def save_file(self):
        file_name = self.file_name()
        handler = open(file_name, 'w')
        handler.write(self.project_output)
        handler.close()

    def save(self):
        self.save_file()
