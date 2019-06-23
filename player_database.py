import csv



class Database:

    def __init__(self):
        self.fieldnames = ['ID', 'Name', 'Rating', 'SkillMoves', 'WeakFoot', 'Pace', 'Shooting', 'Passing', 'Dribbling',
                           'Defending', 'Physicality', 'Position', 'WR_Off', 'WR_Def', 'Height', 'Club', 'Country', 'League',
                           'Age', 'Shape', 'Shapepoints']
        self.file = 'player_database.csv'

    def read(self, playerid, value=False):
        with open(self.file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['ID'] == str(playerid):
                    if value:
                        return row[value]
                    else:
                        return row

    def all_from_category(self, category, value):
        with open(self.file) as file:
            reader = csv.DictReader(file)
            ret = list()
            for row in reader:
                if row[category] == value:
                    ret.append(row)
        return ret


__database = Database()


def read_player_value(playerid, value):
    try:
        return __database.read(playerid, value)
    except KeyError:
        return None


def read_player(playerid):
    try:
        return __database.read(playerid)
    except KeyError:
        return None


def all_from_club(club):
    return __database.all_from_category('Club', club)


def __new_entry(random=True):
    if random:
        pass


if __name__ == '__main__':
    print(read_player_value(2860, 'Shape'))
