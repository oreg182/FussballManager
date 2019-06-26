from Server.player_database import read_player

fieldnames = ['ID', 'Name', 'Rating', 'SkillMoves', 'WeakFoot', 'Pace', 'Shooting', 'Passing', 'Dribbling',
              'Defending', 'Physicality', 'Position', 'WR_Off', 'WR_Def', 'Height', 'Club', 'Country', 'League',
              'Age']


class Player:

    def __init__(self, data, load='all'):
        if load == 'all':
            self.data = data
            self.name = data['Name']
            self.ID = data['ID']
            self.rating = int(data['Rating'])
            self.skillmoves = data['SkillMoves']
            self.weakfoot = data['WeakFoot']
            self.pace = data['Pace']
            self.defending = data['Defending']
            self.shooting = data['Shooting']
            self.passing = data['Passing']
            self.dribbling = data['Dribbling']
            self.physicality = data['Physicality']
            self.position = data['Position']
            self.wr_off = data['WR_Off']
            self.wr_def = data['WR_Def']
            self.height = data['Height']
            self.club = data['Club']
            self.country = data['Country']
            self.league = data['League']
            self.shape = data['Shape']
            self.shapepoints = data['Shapepoints']

    def saison_update(self):
        """alter erhöhen; formpunkte in verbesserung umwandeln"""
        pass

    def __repr__(self):
        return str(self.data)


if __name__ == '__main__':
    print(Player(read_player(54)))
