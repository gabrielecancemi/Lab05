from database.corso_DAO import Corso_DAO
from database.studente_DAO import Studente_DAO


class Model:
    def __init__(self):
        pass

    def getAllCorsi(self):
        return Corso_DAO.getAllCorsi()

    def getStudente(self, matricola):
        return Studente_DAO.getStudente(matricola)

    def getStudentiCorso(self, corso):
        return Studente_DAO.getStudentiCorso(corso)

    def cercaCorsi(self, matricola):
        return Corso_DAO.getCorsi(matricola)

    def iscrivi(self, matricola, corso):
        return Corso_DAO.iscrivi(matricola, corso)

