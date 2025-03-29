# Studie-Budie

Studie-Budie is een Python-applicatie die gebruik maakt van de `tkinter` GUI-bibliotheek. Het biedt verschillende functionaliteiten, waaronder een overschrijfoefening en een weerstanden-simulatie.

## Inhoud

- [Installatie](#installatie)
- [Gebruik](#gebruik)
  - [Overschrijven](#overschrijven)
  - [Weerstanden](#weerstanden)
- [Bestandsstructuur](#bestandsstructuur)
- [Auteurs](#auteurs)

---

## Installatie

1. Zorg ervoor dat Python 3.x is geïnstalleerd op je systeem.
2. Installeer de vereiste pakketten met de volgende opdracht:
   ```bash
   pip install -r requirements.txt
   ```
   **Opmerking:** De vereiste pakketten zijn `tkinter`, `psutil`, en `colorama`.

3. Start de applicatie door het volgende commando uit te voeren:
   ```bash
   python main.py
   ```

---

## Gebruik

### Overschrijven

De overschrijven-functionaliteit biedt een oefening waarbij je woorden moet invoeren en controleren of ze correct zijn. 

- **Startpagina:** Klik op "Home" in het menu om naar de startpagina te gaan.
- **Overschrijven:** Selecteer "overschrijven" in het menu om de oefening te starten.
  - Voer een woord in en druk op Enter om te controleren of het correct is.
  - Klik op "V" om een nieuw woord in te stellen.
  - Klik op "new Log" om een nieuw logbestand te maken.

### Weerstanden

De weerstanden-functionaliteit biedt een simulatie voor het berekenen van weerstanden in serie en parallel.

- **Weerstanden tekenen:** Klik op de canvas om een nieuwe weerstand te plaatsen.
- **Plus/Min-pool:** Klik op "plus" of "min" om een pool te plaatsen.
- **Binding:** Gebruik de rechtermuisknop of de "binden"-optie om weerstanden te verbinden.
- **Berekeningen:**
  - Klik op "serie" om de totale weerstand in serie te berekenen.
  - Klik op "parralel" om de totale weerstand in parallel te berekenen.

---

## Bestandsstructuur

Hier is een overzicht van de belangrijkste bestanden en hun functies:

- **`main.py`**: Startpunt van de applicatie.
- **`app.py`**: Bevat de `Window`-klasse en de hoofdfunctionaliteiten van de GUI.
- **`overschrijven_app.py`**: Logica voor de overschrijven-functionaliteit.
- **`weerstanden.py`**: Logica voor de weerstanden-simulatie.
- **`coordinaten_ui_weerstanden.py`**: Coördinaten en UI-instellingen voor de weerstanden-functionaliteit.
- **`settings.py`**: Instellingen en configuraties.
- **`Debug.py`**: Debug-opties voor ontwikkelaars.

---

## Auteurs

Deze applicatie is gemaakt door **Casper Vanbeselaere**.

---

Veel plezier met het gebruik van Studie-Budie!