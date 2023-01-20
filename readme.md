**Problembeschreibung/Motivation**


  Warum dieses Projekt?


-  Der Promillerechner soll einem ermöglichen den ungefähren Promillewert, den man gerade hat oder vielleicht zu einem vorherigen Moment gehabt hat aufzeigen.

Welches Problem löst das Projekt?

- Der Promillerechner hilft bei der Einschätzung des eigenen Alkoholpegels, hilft also dabei nicht ausversehen betrunken Auto zu fahren. Dies ist ebenfalls für Fahrradfahrer und Scooterfahrer von Nutzen. Er soll also gewissermassen die Verkehrssicherheit steigern.

Was macht das Projekt?
- Die App nimmt Daten zum Alkoholkonsum und dem Körperbau des Users entgegen, und berechnet damit den Blutalkoholpegel. Basierend darauf weren Berechnungen ausgegeben. Der User erhält Informationen zur Fahrtüchtigkeit, der Stärke des kommenden Katers und einige Tipps zur behandlung des Katers.



**Betrieb**

  Welche zusätzliche Pakete müssen bei Bedarf installiert werden? (Muss im Normalfall nicht beachtet werden. Python muss nicht erwähnt werden, da das bei einem Python Projekt impliziert ist.)
 - Die Pakete random, flask, flask request, sowie flask render template müssen importiert werden, ansonsten keine Abhängigkeiten.


  Was muss man bei der Ausführung beachten? Was muss eventuell davor noch gemacht werden?
 - Die App ist mit durchschnittswerten gecodet, also gibt es keine Garantie, dass der gezeigte Promillewert akkurat ist.


  Welche Datei muss ausgeführt werden?
 - Die Datei main.py beinhaltet die Hauptfunktion, welche den Blutalkoholgehalt berechnet. Um den Rechner aufzurufen, muss der localhost unter 127.0.0.1:5000/rechner aufgerufen werden.


**Benutzung**
- Die App funktioniert mit einem Formular, welches Körperlicher Werte sowie den Alkoholkonsum des Users aufnimmt, und diese an die Hauptfunktion weiterleitet, welche Berechnungen vornimmt, und dem User Handlungsempfehlungen sowie Statistiken zu seinem Blutalkoholwert zeigt.


 Welche Optionen oder auch Spezialitäten existieren?
- Der Promillerechner unterscheidet die Geschlechter und wählt jeweils den passenden Alkoholabbauwert, ebenfalls wird das Körpergewicht berücksichtigt.

**Architektur**
- Die Web App zeigt dem Nutzer ein Formular, welches den Input aufnimmt, und per request an die Hauptfunktion "calculate_bac()" in der Python-Datei main.py sendet. Diese nimmt Berechnungen vor, und gibt die berechneten Werte mit derselben GET und POST-Methode weiter an die HTML-Seite "feedback.html", wenn die Inputs des Nutzers komplett eingegeben wurden, lädt die App die Template "feedback.html" anstatt des Anfangsformulars, was dem Nutzer seine Resultate präsentiert.

**Ungelöste/unbearbeitete Probleme**

 Was wurde nicht gelöst?
- Es gelang nicht, eine genauere Berechnung für die Dauer bis zur Nüchternheit einzubauen.


 Verbesserungspotenzial:
- Es war geplant eine umfangreiche Funktion zur Ermittlung der Fahrtüchtigkeit des Users einzubauen, Codeüberbleibsel sind in der calculate_bac() noch anzufinden, konnten jedoch nicht erfolgreich in die html-Dateien eingebaut werden.