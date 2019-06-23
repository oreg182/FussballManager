from tkinter import *
from league import League


class Gui:

    def __init__(self):
        self.root = Tk()
        self.tableframe = Frame()
        self.__tableframe(PL)
        self.tableframe.pack()
        self.root.mainloop()

    def __tableframe(self, league: League):
        table = league.table

        rows = [Label(self.tableframe, text='| Mannschaft                | Sp.| S  | U  | N  | T   | GT  | Dif. | Pkt.|', font=('Liberation mono', 10))]
        for team in table:
            rows.append(Label(self.tableframe, text=str(team), font=('Liberation mono', 10)))
        for x, r in enumerate(rows):
            r.grid(row=x, sticky=W)
        for place in league.aufsteiger:
            rows[place].configure(background='lightgreen')
        for place in league.absteiger:
            rows[place].configure(background='#ff3333')
        for place in league.cl_plaetze:
            rows[place].configure(background='#1a53ff')
        for place in league.cl_quali_plaetze:
            rows[place].configure(background='lightblue')
        for place in league.el_plaetze:
            rows[place].configure(background='orange')


if __name__ == '__main__':
    from league import League
    PL = League('Premier League')
    g = Gui()
