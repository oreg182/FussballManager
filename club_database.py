import csv


class Database:

    def __init__(self):
        self.fieldnames = ['Name', 'League', 'Rating', 'Coach', 'Money']
        self.file = 'club_database.csv'

    def read(self, name, value=False):
        with open(self.file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Name'] == str(name):
                    if value:
                        return row[value]
                    else:
                        return row


__database = Database()


def read_club_value(name, value):
    try:
        return __database.read(name, value)
    except KeyError:
        raise KeyError


def read_club(name):
    try:
        return __database.read(name)
    except KeyError:
        raise KeyError


# TODO schreibzugriff

if __name__ == '__main__':
    print(read_club('Juventus'))
