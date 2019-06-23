import csv
import json
from club import _Club
from match import Match
from config import read_entry


class DeleteDoubles:
    def __init__(self):

        names = {}

        doubles = []

        c = 0

        fieldnames = ['ID', 'Name', 'Rating', 'SkillMoves', 'WeakFoot', 'Pace', 'Shooting', 'Passing', 'Dribbling',
                      'Defending', 'Physicality', 'Position', 'WR_Off', 'WR_Def', 'Height', 'Club', 'Country', 'League',
                      'Age']

        realrows = list()

        with open('player_database.csv') as file:
            rows = csv.DictReader(file)

            for row in rows:
                realrows.append(row)
                name = row['Name']
                if name not in names:
                    add = {name: row['ID']}
                    names.update(add)
                else:
                    c += 1
                    doubles.append(str(row['ID']))
                    print(row['ID'] + row['Name'])
                    print(names[row['Name']])

            print(c)
            print(doubles)

            c2 = 0

            doubles2 = list()

            for double in doubles:
                for row in realrows:
                    if row['ID'] == double:
                        name = row['Name']
                        height = row['Height']
                        age = row['Age']
                for row in realrows:
                    if row['ID'] != double and name == row['Name'] and height == row['Height'] and age == row['Age']:
                        doubles2.append(double)
                        c2 += 1

            print(doubles2)
            print(c2)

            idnrs = []

        with open('player_database.csv', 'w') as file2:
            writer = csv.DictWriter(file2, fieldnames)
            writer.writeheader()
            for row in realrows:
                if row['ID'] not in doubles2:
                    writer.writerow({'ID': row['ID'], 'Name': row['Name'], 'Rating': row['Rating'],
                                     'SkillMoves': row['SkillsMoves'], 'WeakFoot': row['WeakFoot'], 'Pace': row['Pace'],
                                     'Shooting': row['Shooting'], 'Passing': row['Passing'],  #
                                     'Dribbling': row['Dribbling'], 'Defending': row['Defending'],
                                     'Physicality': row['Phyiscality'], 'Position': row['Position'],
                                     'WR_Off': row['WR_Off'], 'WR_Def': row['WR_Def'],
                                     'Height': row['Height'], 'Club': row['Club'], 'Country': row['Country'],
                                     'League': row['League'], 'Age': row['Age'].split(' ')[0]})


class GetLeagues:

    @staticmethod
    def leagues():
        clubs = list()

        with open('player_database.csv') as file:
            rows = csv.DictReader(file)
            for row in rows:
                if (row['Club'], row['League']) not in clubs:
                    clubs.append((row['Club'], row['League']))

        leagues = list()

        for key in clubs:
            leagues.append(key[0])

        print(leagues)

        leagues = dict()

        for club in clubs:
            if club[1] not in leagues:
                new = {club[1]: [club[0]]}
                leagues.update(new)
            else:
                leagues[club[1]].append(club[0])

        for key in leagues:
            print(key)
            for team in leagues[key]:
                print('    ' + team)

        return leagues


class AddShape:

    def __init__(self):
        all = list()

        with open('player_database.csv') as file:
            rows = csv.reader(file)
            for row in rows:
                all.append(row)

        header = all[0]
        header.append('Shape')
        header.append('Shapepoints')

        del all[0]

        for player in all:
            player.append(0)
            player.append(0)

        with open('player_database.csv', 'w') as file2:
            writer = csv.writer(file2)
            writer.writerow(header)
            for pl in all:
                writer.writerow(pl)


class BuildClubDatabase:

    def __init__(self):
        clubs = {}
        fieldnames = ['Name', 'League', 'Rating', 'Coach', 'Money']

        with open('player_database.csv') as file:
            rows = csv.DictReader(file)

            for row in rows:
                name = row['Club']
                if name not in clubs:
                    add = {name: row['League']}
                    clubs.update(add)
        with open('club_database.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames)
            writer.writeheader()
            for club in clubs:
                print(club)
                writer.writerow({'Name': club, 'League': clubs[club], 'Rating': 100, 'Coach': 0, 'Money': 0})


class Matchtable:

    @staticmethod
    def create_fixtures(teams):
        n = len(teams)
        matchs = []
        fixtures = []
        return_matchs = []
        for fixture in range(1, n):
            for i in range(int(n / 2)):
                matchs.append((teams[i], teams[n - 1 - i]))
                return_matchs.append((teams[n - 1 - i], teams[i]))
            teams.insert(1, teams.pop())
            fixtures.insert(int(len(fixtures) / 2), matchs)
            fixtures.append(return_matchs)
            matchs = []
            return_matchs = []

        for fixture in fixtures:
            print(fixture)


class PrintTeams:

    def __init__(self, league):
        clubs = read_entry('clubnames', 'Leagues', league)
        for club in clubs:
            c = _Club(club)
            print(c.name,  c.team_rating)


class RandomResults:

    def __init__(self, league):
        with open('leagues/' + league + '/results.dat') as file:
            results = json.load(file)
        for fixture in results:
            for match in fixture:
                t = list()
                for team in match:
                    t.append(team)
                m = Match(_Club(t[0]), _Club(t[1])).ergebnis()
                match[t[0]] = m[t[0]]
                match[t[1]] = m[t[1]]
                print(match)
        with open('leagues/' + league + '/results.dat', 'w') as file:
            json.dump(results, file)


if __name__ == '__main__':
    PrintTeams('Premier League')
