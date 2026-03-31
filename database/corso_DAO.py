# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
from model.corso import Corso


class Corso_DAO():
    @staticmethod
    def getAllCorsi():
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = "select * from corso"

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Corso(codins=row["codins"], crediti=row["crediti"], nome=row["nome"], pd=row["pd"]))

        cursor.close()
        cnx.close()
        return res

    @classmethod
    def getCorsi(cls, matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = f'''select * from iscrizione i, corso c where matricola = {matricola} and c.codins = i.codins'''

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Corso(codins=row["codins"], crediti=row["crediti"], nome=row["nome"], pd=row["pd"]))

        cursor.close()
        cnx.close()
        return res

    @classmethod
    def iscrivi(cls, matricola, corso):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = f'''insert into iscrizione(matricola, codins) values ({matricola}, "{corso}")'''

        cursor.execute(query)
        cnx.commit()
        if cursor:
            cursor.close()
            cnx.close()
            return True

        cursor.close()
        cnx.close()
        return False
