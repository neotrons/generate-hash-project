import hashlib

MD5_HASH = hashlib.md5()
CLONE_DIR = './repositories/'


class FileHash:
    def __init__(self, file_path):
        self.hash = MD5_HASH
        self.clone_dir = CLONE_DIR
        self.file = file_path
        self.digest = self.get_hash()

    def read_file(self):
        a_file = open(self.file, "rb")
        return a_file.read()

    def get_hash(self):
        content = self.read_file()
        self.hash.update(content)
        return self.hash.hexdigest()

    def line_file_hash(self):
        return f'{self.file.replace(self.clone_dir, "./")},{self.digest}'

    def __str__(self):
        return self.line_file_hash()
