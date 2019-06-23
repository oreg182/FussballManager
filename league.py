import json
from random import shuffle
from operator import attrgetter
from club import _Club
from config import read_entry


class League:

    def __init__(self, name):
        self.name = name
        self.club_names = read_entry('clubnames', 'Leagues', name)

        self.clubs = list()
        for club in self.club_names:
            self.clubs.append(_Club(club))

        self.fixture = self.__load_fixture()

        self.next_matchday = self.load_matchday(read_entry('next_matchday', 'Leagues', self.name))

        self.all_results = self.load_results()

        self.table = self.calc_table()

        self.aufsteiger = read_entry("aufsteiger", 'Leagues', name)
        self.absteiger = read_entry("absteiger", 'Leagues', name)
        self.cl_plaetze = read_entry("cl", 'Leagues', name)
        self.cl_quali_plaetze = read_entry("clq", 'Leagues', name)
        self.el_plaetze = read_entry("el", 'Leagues', name)

    def __create_fixture(self):
        n = len(self.club_names)
        teams = self.club_names
        matchs = []
        fixtures = []
        for _ in range(1, n):
            for i in range(int(n / 2)):
                matchs.append((teams[i], teams[n - 1 - i]))
            teams.insert(1, teams.pop())
            fixtures.insert(int(len(fixtures) / 2), matchs)
            matchs = []
        shuffle(fixtures)
        newfixtures = list()
        for fixture1 in fixtures:
            newfixture = []
            for match in fixture1:
                newmatch = (match[1], match[0])
                newfixture.append(newmatch)
            newfixtures.append(newfixture)
        for fixture1 in newfixtures:
            fixtures.append(fixture1)
        with open('leagues/' + self.name + '/fixture.dat', 'w') as file:
            json.dump(fixtures, file)
        results = list()
        for fixture in fixtures:
            newfixture = list()
            for match in fixture:
                newmatch = {match[0]: None, match[1]: None}
                newfixture.append(newmatch)
            results.append(newfixture)
        with open('leagues/' + self.name + '/results.dat', 'w') as file:
            json.dump(results, file)
        return fixtures

    def __load_fixture(self):
        with open('leagues/' + self.name + '/fixture.dat') as file:
            return json.load(file)

    def load_matchday(self, matchday):
        return self.fixture[int(matchday)]

    def load_results(self, matchday='all'):
        with open('leagues/' + self.name + '/results.dat') as file:
            if matchday == 'all':
                return json.load(file)

    def calc_table(self):
        return Table(self.club_names, self.all_results).calc()

    def __repr__(self):
        return 'Object League <' + self.name + '>'


class _TableTeam:
    def __init__(self, name):
        self.name = name
        self.punkte = 0
        self.spiele = 0
        self.siege = 0
        self.unentschieden = 0
        self.niederlagen = 0
        self.tore = 0
        self.gegentore = 0
        self.tordifferenz = 0

    def get_difference(self):
        self.tordifferenz = self.tore - self.gegentore

    def __repr__(self):
        return '| {:25}'.format(self.name[:25]) + ' | {:1} | '.format(str(self.spiele)) + '{:2} | '.format(str(self.siege)) + '{:2} | '.format(str(self.unentschieden))+ '{:2} | '.format(str(self.niederlagen))+ '{:3} | '.format(str(self.tore))+ '{:3} | '.format(str(self.gegentore))+ '{:4} | '.format(str(self.tordifferenz))+ '{:3} | '.format(str(self.punkte))


class Table:

    def __init__(self, names, all_results):
        """format: {teamname: [spiele, siege, unentschieden, niederlagen, tore, gegentore, punkte], ...}"""
        table = {}
        for team in names:
            add = {team: _TableTeam(team)}
            table.update(add)
        for fixture in all_results:
            for match in fixture:

                teams = list()
                for team in match:
                    teams.append(team)

                if match[teams[0]] is None or match[teams[1]] is None:
                    continue

                table[teams[0]].spiele += 1  # spiele für beide teams += 1
                table[teams[1]].spiele += 1

                if match[teams[0]] > match[teams[1]]:
                    table[teams[0]].siege += 1  # siege team 1 += 1
                    table[teams[1]].niederlagen += 1  # niederlagen team 2 += 1
                    table[teams[0]].punkte += 3  # punkte für sieg erhöhen

                elif match[teams[0]] < match[teams[1]]:
                    table[teams[1]].siege += 1  # siege team 1 += 1
                    table[teams[0]].niederlagen += 1  # niederlagen team 2 += 1
                    table[teams[1]].punkte += 3  # punkte für sieg erhöhen

                elif match[teams[0]] == match[teams[1]]:
                    table[teams[0]].unentschieden += 1  # unentschieden beide += 1
                    table[teams[1]].unentschieden += 1
                    table[teams[0]].punkte += 1  # punkte erhöhen
                    table[teams[1]].punkte += 1

                table[teams[0]].tore += match[teams[0]]  # tore & gegentore für heimteam
                table[teams[0]].gegentore += match[teams[1]]

                table[teams[1]].tore += match[teams[1]]  # tore & gegentore für auswaertsteam
                table[teams[1]].gegentore += match[teams[0]]
        for team in table:
            table[team].get_difference()

        table = sorted(table.values(), key=attrgetter('punkte', 'tordifferenz', 'tore'), reverse=True)

        self.table = table

    def calc(self):
        return self.table
