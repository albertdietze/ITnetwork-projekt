class Pojistena_osoba:
    """
    Třída pro pojištěnou osobu
    """

    def __init__(self, jmeno, prijmeni, vek, telefon):
        """
        Konstruktor pro vytvoření pojištěné osoby
        """
        self.jmeno = jmeno.capitalize()
        self.prijmeni = prijmeni.capitalize()
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}, věk: {self.vek}, telefonní číslo: {self.telefon}"
    """ 
    Textové vyjádření pojištěných osob
    """
