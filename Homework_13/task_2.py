# Implement writer for proxy pattern from the lesson

import os


class FileWriter:
    def write_file(self, filename, content):
        with open(filename, 'w') as file:
            file.write(content)
        print(f"File '{filename}' has been written.")


class FileWriterProxy:
    def __init__(self):
        self.file_writer = FileWriter()

    def write_file(self, filename, content):
        if self.is_allowed(filename):
            self.file_writer.write_file(filename, content)
        else:
            print("Sorry, you are not allowed to write this file.")

    def is_allowed(self, filename):
        extension = os.path.splitext(filename)[1]
        return extension.lower() == ".txt"


if __name__ == '__main__':
    proxy = FileWriterProxy()
    proxy.write_file("example.txt", "This is some content.")
    proxy.write_file("example.jpg", "This won't be written.")
