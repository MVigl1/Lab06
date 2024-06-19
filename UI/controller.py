import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleTopVendite(self, e):
        anno = self._view.dd_anno
        brand = self._view.dd_brand
        retailer = self._view.dd_retailer

        if anno is None or anno == "":
            self._view.create_alert("Inserire l'anno")
            return
        if brand is None or brand == "":
            self._view.create_alert("Inserire il brand")
            return
        if retailer is None or retailer == "":
            self._view.create_alert("Inserire il retailer")
            return

        self._view.txt_result.controls.append(ft.Text(f"Top Vendite, {anno}!"))
        self._view.update_page()


    def handleAnalizzaVendite(self, e):
        anno = self._view.dd_anno
        brand = self._view.dd_brand
        retailer = self._view.dd_retailer

        if anno is None or anno == "":
            self._view.create_alert("Inserire l'anno")
            return
        if brand is None or brand == "":
            self._view.create_alert("Inserire il brand")
            return
        if retailer is None or retailer == "":
            self._view.create_alert("Inserire il retailer")
            return

        self._view.txt_result.controls.append(ft.Text(f"analizza vendite, {anno}!"))
        self._view.update_page()


    def populate_dd_anno(self):
        return self._model.populate_dd_anno()

