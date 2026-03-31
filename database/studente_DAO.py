# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model.studente import Studente


class Studente_DAO():
    @classmethod
    def getStudentiCorso(cls, corso):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = f'''select * from studente s, iscrizione i where s.matricola = i.matricola and i.codins = "{corso}"'''

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Studente(matricola=row["matricola"], cognome=row["cognome"], nome=row["nome"], CDS=row["CDS"]))

        cursor.close()
        cnx.close()
        return res

    @classmethod
    def getStudente(cls, matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = f'''select * from studente where matricola = {matricola}'''

        cursor.execute(query)

        res = None
        for s in cursor:
            res = (Studente(matricola=s["matricola"], cognome=s["cognome"], nome=s["nome"], CDS=s["CDS"]))

        cursor.close()
        cnx.close()
        return res


