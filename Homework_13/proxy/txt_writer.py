from Homework_13.proxy.abstract_writer import Writer


class TxtWriter(Writer):
    def __init__(self, file_name):
        self.file_name = file_name

    def write_file(self, text):
        with open(self.file_name, 'a') as file:
            file.write(text)
        return file
