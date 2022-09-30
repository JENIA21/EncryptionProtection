import json


class DecodeClass:
    def __init__(self, name):
        self.name = name

    split_func = lambda lst, sz: [lst[i:i + sz] for i in range(0, len(lst), sz)]

    @staticmethod
    def convert_base(num, to_base=16, from_base=10):
        if isinstance(num, str):
            n = int(num, from_base)
        else:
            n = int(num)
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if n < to_base:
            return alphabet[n]
        else:
            return DecodeClass.convert_base(n // to_base, to_base) + alphabet[n % to_base]

    def decode(self):
        out_text = []
        with open('dic_file.txt', 'r') as fr:
            lst = json.load(fr)
        with open(self.name, "rb") as file:
            data = file.read()
            data = data[4096:]
            dic_value = []
            for value in data:
                dic_value.append(value)
            data_text = DecodeClass.split_func(dic_value, 16)
        for values in data_text:
            for value in lst:
                if values == value[0]:
                    out_text.append(value[1])
        with open(self.name, "wb") as file:
            for one_data in out_text:
                res = DecodeClass.convert_base(one_data)
                if res != 0:
                    if len(res) % 2 == 0:
                        file.write(bytes.fromhex(res))
                    else:
                        res = '0' + res
                        file.write(bytes.fromhex(res))
                else:
                    file.write(bytes(0))
