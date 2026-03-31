import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def cercaIscritti(self, e):
        corso = self._view.ddInCorso.value
        if corso is None:
            self._view.create_alert("Inserire il corso")
            return
        studenti = self._model.getStudentiCorso(corso)
        for s in studenti:
            self._view.txtResult.controls.append(ft.Text(f"{s}"))
        self._view.update_page()

    def cercaStudente(self, e):
        matricola = self._view.txtInMatricola.value
        if matricola == "":
            self._view.create_alert("Inserire la matricola")
            return
        studente = self._model.getStudente(matricola)
        if studente is None:
            self._view.create_alert("Studente NON esistente")
            return
        else:
            self._view.txtNome.value = studente.nome
            self._view.txtCognome.value = studente.cognome

        self._view.update_page()

    def cercaCorsi(self, e):
        matricola = self._view.txtInMatricola.value
        if matricola == "":
            self._view.create_alert("Inserire la matricola")
            return
        studente = self._model.getStudente(matricola)
        if studente is None:
            self._view.create_alert("Studente NON esistente")
            return
        else:
            corsi = self._model.cercaCorsi(matricola)
            if corsi is None:
                self._view.create_alert("Studente iscritto a nessun corso")
                return
            else:
                for c in corsi:
                    self._view.txtResult.controls.append(ft.Text(f"{c}"))

        self._view.update_page()

    def iscrivi(self, e):
        corso = self._view.ddInCorso.value
        if corso is None:
            self._view.create_alert("Inserire il corso")
            return
        matricola = self._view.txtInMatricola.value
        if matricola == "":
            self._view.create_alert("Inserire la matricola")
            return

        studente = self._model.getStudente(matricola)
        if studente is None:
            self._view.create_alert("Studente NON esistente")
            return
        else:
            res = self._model.iscrivi(matricola, corso)
            if res:
                self._view.txtResult.controls.append(ft.Text(f"CREATO"))
                self._view.update_page()

            else:
                self._view.create_alert("ERRORE")

    def refil_corso(self):
        for c in self._model.getAllCorsi():
            self._view.ddInCorso.options.append(ft.dropdown.Option(key=c.codins, text=c))