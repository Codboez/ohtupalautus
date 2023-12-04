class Summa:
    def __init__(self, laskin, get_syote) -> None:
        self._laskin = laskin
        self._get_syote = get_syote

    def suorita(self):
        syote = self._get_syote()
        self._laskin.plus(syote)

class Erotus:
    def __init__(self, laskin, get_syote) -> None:
        self._laskin = laskin
        self._get_syote = get_syote

    def suorita(self):
        syote = self._get_syote()
        self._laskin.miinus(syote)

class Nollaus:
    def __init__(self, laskin) -> None:
        self._laskin = laskin

    def suorita(self):
        self._laskin.nollaa()

class Kumoa:
    def __init__(self, laskin) -> None:
        self._laskin = laskin

    def suorita(self):
        self._laskin.kumoa()