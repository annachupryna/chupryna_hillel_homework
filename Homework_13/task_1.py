# Implement adapter patter from_txt_to_html

class FromDataAdapter:
    def __init__(self, file_path):
        self.file_path = file_path

    def convert_from_txt_to_html(self):
        with open(self.file_path) as file:
            lines = file.readlines()
        headers_txt = lines[0].replace('\n', '')
        user_data_txt = lines[1:]
        headers = headers_txt.split(',')
        data_user = [item.replace('\n', '').split(',') for item in user_data_txt]
        result = []

        for u_data in data_user:
            result.append(dict(zip(headers, u_data)))

        for dic in result:
            for key, value in dic.items():
                print(f'<{key}>{value}</{key}>')
            print('--------------')

        return result


if __name__ == '__main__':
    data = FromDataAdapter('lines.txt').convert_from_txt_to_html()
    print(data)
