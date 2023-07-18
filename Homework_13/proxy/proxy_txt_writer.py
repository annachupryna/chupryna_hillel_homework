from Homework_13.proxy.txt_reader import TxtReader
from Homework_13.proxy.txt_writer import TxtWriter


class TxtProxyWriter(TxtWriter, TxtReader):
    def __init__(self, file_name):
        super().__init__(file_name)
        self.__text = ''
        self.__writer = TxtWriter(file_name)
        self.__reader = TxtReader(file_name)

    def write_file(self, text):
        if text in self.__text:
            return self.__text
        else:
            self.__writer.write_file(text + '\n')
            bla = self.__reader.read_file()
            self.__text = bla
            return self.__text


if __name__ == '__main__':
    txt_proxy_writer = TxtProxyWriter('test.txt')
    data_1 = txt_proxy_writer.write_file('test1')
    data_2 = txt_proxy_writer.write_file('test2')
    data_3 = txt_proxy_writer.write_file('test1')
