from sys import maxsize

class Group:

    def __init__(self, name = None, header = None, footer = None, id = None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    # переопределенная стандартная функция представления
    def __repr__(self):
        return '%s %s' % (self.id, self.name)

    # переопределенная стандартная функция сравнения
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    # функция получения id записи, если None - возвращается мах возможное число
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize