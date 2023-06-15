class adas:
    def __init__(self,row) -> None:
        splitted = row.split(';')
        self.ora = int(splitted[0])
        self.perc = int(splitted[1])
        self.adasdb = splitted[2]
        self.nev = splitted[3]

        self.kezdes = self.ora * 60 + self.perc