## Allgemeines

Dies ist das Repo, welches die FSFW-Homepage (https://fsfw-dresden.de) mit Hilfe von [Pelican](http://docs.getpelican.com/),
einem Generator für statische Webseiten baut.

Es enthält je ein Git-Submodul für das Theme und den eigentlichen Inhalt.

Nach dem Klonen sollten man deshalb ggf. 

 `git submodule update --init`

aufrufen, um diese Repos in die entsprechenden Unterverzeichnisse zu klonen.
Siehe auch `.gitmodules` und <https://git-scm.com/book/en/v2/Git-Tools-Submodules>.


## Kurz-Doku des Bau-Prozesses

Relevante Kommandos:
* `make html` -> befüllt das `output`-Verzeichnis
* `make devserver`
 * gut für Vorschau: aktualisiert die erzeugten HTML-Dateien automatisch bei Änderungen
* `make publish`
 * (verwendet Konfig-Datei `publishconf.py`)
 * Dadurch können z.B. unterschiedliche CSS-URLs für Vorschau und Produktion verwendet werden

### Weiter Infos:
Siehe [Pelican-Doku](http://docs.getpelican.com/).
