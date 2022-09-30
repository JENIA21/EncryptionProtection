import hashlib
from Crypto.Cipher import AES


class EncodeClass:
    def __init__(self, name, key):
        self.name = name
        self.key = hashlib.sha256(key.encode()).digest()

    split_func = lambda lst, sz: [lst[i:i + sz] for i in range(0, len(lst), sz)]

    def encode(self, ):
        with open(self.name, "rb") as file_inp:
            data = file_inp.read()
            out_data = []
            count = EncodeClass.split_func(data, 16)
            cipher = AES.new(self.key, AES.MODE_ECB)
            for i in count:
                out_data.append(cipher.encrypt(bytes(i)))
            with open(self.name, "wb") as file_out:
                for one_data in out_data:
                    file_out.write(one_data)
