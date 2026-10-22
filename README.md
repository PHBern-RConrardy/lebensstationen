# Lebensstationen

Interaktive Wegkarte und Zeitstrahl zu beruflichen und akademischen Stationen.

Die statische Website liegt in `dist/` und kann lokal direkt geöffnet oder mit einem einfachen Webserver gestartet werden.

Veröffentlichte Website: https://phbern-rconrardy.github.io/lebensstationen/

`dist/lebensstationen-standalone.html` ist eine einzelne offline nutzbare
HTML-Datei. Skripte, Styles und Kartendaten sind eingebettet. Die identische
Download-Datei liegt unter `docs/lebensstationen-standalone.html`.

Nach Änderungen an `dist/` neu erzeugen:

```sh
python3 scripts/build_standalone.py
```

Die dafür benötigten Bibliotheken und Schweizer Kartendaten liegen unter
`vendor/`; die Lizenztexte der Bibliotheken sind dort beigefügt. Kartengrundlage
Schweiz: swisstopo, TopoJSON-Aufbereitung durch swiss-maps (BSD).
