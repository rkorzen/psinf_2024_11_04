import wx


class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        # Tworzymy panel główny
        panel = wx.Panel(self)

        # Utworzenie widżetów
        a_label = wx.StaticText(panel, label="a", pos=(10, 10))
        self.a = wx.TextCtrl(panel, pos=(30, 10), size=(100, -1))

        b_label = wx.StaticText(panel, label="b", pos=(10, 40))
        self.b = wx.TextCtrl(panel, pos=(30, 40), size=(100, -1))

        self.button = wx.Button(panel, label="Dodaj", pos=(10, 70))
        self.button.Bind(wx.EVT_BUTTON, self.dodaj)  # Powiązanie przycisku z funkcją dodaj

        self.wynik_label = wx.StaticText(panel, label="-", pos=(10, 100))

    def dodaj(self, event):
        try:
            # Pobieranie wartości i dodawanie
            a_value = int(self.a.GetValue())
            b_value = int(self.b.GetValue())
            wynik = a_value + b_value

            # Aktualizacja etykiety wynikowej
            self.wynik_label.SetLabel(str(wynik))
        except ValueError:
            self.wynik_label.SetLabel("Błąd: podaj liczby")


# Główna pętla aplikacji
app = wx.App(False)
frame = MyFrame(None, title="Dodawanie", size=(200, 200))
frame.Show()
app.MainLoop()

print("print po")
