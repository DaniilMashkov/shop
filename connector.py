import json
import os.path
import re

class Connector:
    """
    Класс коннектор к файлу, обязательно файл должен быть в json формате
    не забывать проверять целостность данных, что файл с данными не подвергся
    внешнего деградации
    """
    __data_file = None

    def __init__(self, df):
        self.__data_file = df
        self.__connect()

    def __connect(self):
        """
        Проверка на существование файла с данными и
        создание его при необходимости
        """
        if os.path.exists(self.__data_file):
            return 'file exists'
        else:
            with open (self.__data_file, 'w') as file:
                json.dump([], file)
                
                
    def insert(self, data):
        """
        Запись данных в файл с сохранением структуры и исходных данных
        """
        with open (self.__data_file, 'w') as file:
            try:
                json.dump(json.load(file).append(data), file)
            except:
                json.dump([data], file)


    def select(self, query):
        """
        Выбор данных из файла с применением фильтрации
        query содержит словарь, в котором ключ это поле для
        фильтрации, а значение это искомое значение, например:
        {'price': 1000}, должно отфильтровать данные по полю price
        и вернуть все строки, в которых цена 1000
        """
        with open (self.__data_file, 'r') as file:
            try:
                key = re.search(r"\w+", str(query))[0]

                lst = list(filter(lambda x: x[key]==query[key], json.load(file)))

                if not lst: print("Товар не найден")
                
                return lst

            except TypeError:
                return json.load(file)
        
                
    def delete(self, query):
        """
        Удаление записей из файла, которые соответствуют запрос,
        как в методе select
        """
        with open (self.__data_file, 'w+') as file:
            try:
                json.dump([x for x in json.load(file) if x['id'] != query['id']], file)
            except json.decoder.JSONDecodeError: 
                json.dump([], file)
            else:
                print('not found')     
            
            

if __name__ == '__main__':
    df = Connector('df.json')

    data_for_file = {'id': 1, 'title': 'tet'}

    df.insert(data_for_file)

    data_from_file = df.select({'id': 1})
    assert data_from_file == [data_for_file]

    # df.delete({'id': 1})
    # data_from_file = df.select({'id': 1})
    # assert data_from_file == []
