import math
import random
from club import _Club


class Match:

    def __init__(self, club1: _Club, club2: _Club, output='simple'):
        self.heimname = club1.name
        self.auswaertsname = club2.name  # TODO club rating zufällig verändern
        clubr1 = club1.team_rating + random.randint(-3, 3)
        clubr2 = club2.team_rating + random.randint(-3, 3)
        if output == 'simple':
            self.score = 0
            self.score2 = 0
            dif = clubr1 - clubr2
            events = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2]

            if dif > 0:
                for _ in range(dif):
                    for _ in range(30):
                        events.append(0)
                    events.append(1)
                for _ in range(int(dif/4)+random.randint(0, 1)):
                    events.append(2)

            elif dif < 0:
                dif = int(math.sqrt(dif ** 2))
                for _ in range(dif):
                    for _ in range(30):
                        events.append(0)
                    events.append(2)
                for _ in range(int(dif/4)+random.randint(0, 1)):
                    events.append(1)

            for minute in range(90):
                e = random.choice(events)
                if e == 1:
                    self.score += 1
                elif e == 2:
                    self.score2 += 1

    def ergebnis(self):
        return {self.heimname: self.score, self.auswaertsname: self.score2}

    def test1(self):
        return self.score

    def test2(self):
        return self.score2


if __name__ == '__main__':
    c1 = _Club('Manchester City')
    c2 = _Club('Real Madrid')

    print(c1.team_rating, c2.team_rating)

    s1 = 0
    s2 = 0

    s = 0
    u = 0
    n = 0

    c = 0

    for i in range(100000):
        m = Match(c1, c2)
        s1 = m.test1()
        s2 = m.test2()
        if s1 > s2:
            s += 1
        elif s1 == s2:
            u += 1
        else:
            n += 1

    print(s, u, n)
