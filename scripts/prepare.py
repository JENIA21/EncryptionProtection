class PrepareClass:
    def __init__(self, name):
        self.name = name

    def prepare(self):
        dic_sort = []
        write_data = []
        with open(self.name, "rb") as file:
            data = file.read()
            for t in data:
                data_i = t, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                write_data.append(data_i)
            for k in range(0, 256):
                sort = k, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                dic_sort.append(sort)
        with open(self.name, "wb") as file:
            for key in dic_sort:
                file.write(bytes(key))
            for one_data in write_data:
                file.write(bytes(one_data))
