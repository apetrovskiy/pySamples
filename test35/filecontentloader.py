class FileContentLoader:
    def __init__(self, file_path):
        self.file = open(file_path, 'r')

    def __del__(self):
        self.file.close()

    def load_all(self):
        return self.file.readlines()
