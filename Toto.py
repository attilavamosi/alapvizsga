class Totó:
    def __init__(self,row) -> None:
        splitted = row.split()
        self.év = splitted[0]
        self.hét = int(splitted[1])
        self.forduló = int(splitted[2])
        self.t13p1 = int(splitted[3])
        self.ny13p0 = int(splitted[4])
        self.eredménye = splitted[5]