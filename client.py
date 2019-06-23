from league import League
from config import read_entry
from gui import Gui

PL = League('Premier League')

for team in PL.table:
    print(len(str(team)))