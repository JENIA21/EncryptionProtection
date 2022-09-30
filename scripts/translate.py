import json


class TranslateClass:
    def __init__(self, name):
        self.name = name

    split_func = lambda lst, sz: [lst[i:i + sz] for i in range(0, len(lst), sz)]

    def translate(self):
        with open(self.name, "rb") as file:
            data = file.read()
            dic_value = []
            dic = data[:4096]
            out_data = []
            for value in dic:
                dic_value.append(value)
            count = TranslateClass.split_func(dic_value, 16)
            for numb in range(0, 256):
                print(count[numb], '------>', numb)
                out_data.append((count[numb], numb))
        with open('dic_file.txt', 'w') as fw:
            json.dump(out_data, fw)
