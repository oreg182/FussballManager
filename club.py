from player import Player
from club_database import read_club_value, read_club
from player_database import all_from_club


class _ClubAI:

    def __init__(self):
        self.player = []

    def set_first_elvn(self):
        team = self.player[:11]
        return team


class _Club(_ClubAI):

    def __init__(self, name, load='ALL'):
        if load == 'ALL':
            super().__init__()
            self.name = name
            self.data = read_club(name)
            self.league = self.data['League']
            self.coach = self.data['Coach']
            self.money = self.data['Money']

            self.player = []
            for p in all_from_club(name):
                self.player.append(Player(p))

            self.first_elvn = self.set_first_elvn()

            self.team_rating = self.get_team_rating()

    def get_team_rating(self):
        c = 0
        for player in self.first_elvn:
            c += player.rating
        c /= 11
        return int(round(c, 0))

    def __repr__(self):
        return 'Object Club ' + self.name


if __name__ == '__main__':
    print(_Club('Manchester United').team_rating)
