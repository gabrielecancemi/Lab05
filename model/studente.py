from dataclasses import dataclass


@dataclass
class Studente:
    matricola: int
    cognome: int
    nome: str
    CDS: int

    def __hash__(self):
        return hash(self.matricola)

    def __eq__(self, other: "Studente"):
        return self.matricola == other.matricola

    def __str__(self):
        return f"{self.nome}, {self.cognome} ({self.matricola})"
