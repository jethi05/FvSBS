Als Hitzetag (auch "Heißer Tag", "Tropentag") werden Tage bezeichnet, an denen eine Lufttemperatur von >= 30°C gemessen wird.

Die Datei hitzetage.txt enthält die Anzahl gemessener Hitzetage pro Jahr und Region. Orientierungshilfe: Die Datei hitzetage.ods enthält alle Daten die im Endprodukt der folgenden Aufgaben enthalten sind.

**Aufgaben**

A) Erweitere die Daten um die Spalte "Mittel" und speichere sie in einer neuen Datei. Gehe dazu wie folgt vor:

1. Schreibe die Funktion berechne_mittelwert(), die eine Liste mit Zahlenwerten als Strings erhält und den Mittelwert (auch: Durchschnitt, Mittel) dieser Werte als String zurückliefert. Prüfe die Funktion mit folgenden Werten:

   ```python
   print(berechne_mittelwert(["12", "8", "10"])) # --> "10.0"
   print(berechne_mittelwert(["1", "2"])) # --> "1.5"
   ```
2. Schreibe einen Programmteil, der den Inhalt der Datei hitzetage.txt liest und in eine neue Datei hitzetage_erweitert.txt schreibt.
3. Zerlege den Dateiinhalt so, dass du für jedes Jahr eine Liste mit den gemessenen Hitzetagen erhältst. Überprüfe dein Ergebnis mit dem Debugger und der Variablenansicht ("View", "Variables").  
   Benötigte Werkzeuge:

   ```python
   for 
   str.split()
   ```

   Berechne mit Hilfe der Funktion berechne_mittelwert() den Durchschnitt für jedes Jahr und hänge ihn ans Ende der jeweiligen Liste mit den gemessenen Hitzetagen.  
   Benötigte Werkzeuge: list.append()
4. Konvertiere die erweiterte Liste für jedes Jahr zu einem semikolongetrennten String. Sorge dafür, dass der String für jedes Jahr nach Ablauf der for-Schleife im Speicher ist.  
   Benötigte Werkzeuge: str.join()
5. Erweitere die Kopfzeile um die Spalte "Mittel" und füge die in den vorigen Aufgaben erweiterten Zeilen für jedes Jahr hinzu.  
   Benötigte Werkzeuge: str.join(), Konkatenation
6. Schreibe das Ergebnis in die Datei hitzetage_erweitert.txt
7. Speichere dein bisheriges Programm in die Datei hitzetage_a.py

B) Erweitere die Daten um die Fußzeile "Durchschnitt", die in jeder Spalte den Mittelwert für jede Region über alle Jahre enthält. Gehe dazu wie folgt vor:

1. Dupliziere die Datei hitzetage_a.py unter dem namen hitzetage_b.py und öffne sie mit der IDE (z.B. Thonny oder Spyder).
2. Gib alle Messwerte von "Brandenburg/Berlin" zeilenweise auf der Konsole aus. Durchlaufe und zerlege den Dateiinhalt von hitzetage.txt dazu so, dass du für jedes Jahr den Messwert von "Brandenburg/Berlin" isoliert an print() übergeben kannst.
3. Ändere das Programm aus der vorigen Aufgabe so ab, dass die Messwerte von "Brandenburg/Berlin" nicht mehr ausgegeben werden, sondern in eine neue Liste gespeichert werden.
4. Berechne den Durchschnitt für "Brandenburg/Berlin" mit Hilfe der Funktion berechne_mittelwert() aus Aufgabe A) und füge das Ergebnis in eine neue Liste mit dem Namen fusszeile_durchschnitt.
5. Berechne den jeweiligen Durchschnitt über alle Jahre für alle weiteren Regionen und füge ihn jeweils an die Liste fusszeile_durchschnitt.
6. Setze das Attribut "Durchschnitt" an den Beginn von fusszeile_durchschnitt und schreibe die neue Zeile als String ans Ende der Datei hitzetage_erweitert.txt

C) Der Mittelwert ist zwar präzise, doch kann er von Ausreißern verfälscht werden. Aus diesem Grund wird oft der robustere Median (Zentralwert) hinzugezogen um Datenreihen zu interpretieren. Erweitere die Ausgabedatei um die Zeile "Median" und die Spalte "Quartil". Gehe hierzu wie folgt vor:

1. Der Median steht in der Mitte einer sortierten Folge. Schreibe die Funktion berechne_median() die eine Liste von Zahlenwerten als Strings bekommt und den Median als String liefert \[Siehe Video: [Median erklärt](), auch am Ende dieses Texts\]. Prüfe die Funktion mit folgenden Testwerten:

   ```python
   berechne_median(["1", "2", "100"]) # --> "2"
   berechne_median(["100", "1", "2"]) # --> "2"
   berechne_median(["10", "1"]) # --> "5.5"
   berechne_median(["100", "200", "3", "50"]) # --> "75.0"
   ```

   Benötigte Werkzeuge:

   ```python
   for, int(str), list.append()
   list.sort() oder sorted(list)
   %, //, str(int)
   ```
2. Berechne den Median über alle Jahre für jede Spalte (jede Region und den Mittelwert).
3. Füge unten eine Zeile mit dem Median für jede Spalte an, setze an ihren Beginn das Wort "Median".
4. Der Wertebereich über dem Median heißt "oberes Quartil" und der Wertebereich unter dem Median heißt "unteres Quartil". Bestimme für jedes Jahr ob der **Mittelwert** im oberen Quartil oder im unteren Quartil liegt. Nimm als Referenzwert den Median der Mittelwerte aller Jahre (dieser steht in der Tabelle unten rechts).
5. Erweitere die Ausgabedatei um die Spalte "Quartil". Liegt der Wert für ein Jahr über dem Median der Mittelwerte aller Jahre, ist der Wert für das Jahr "oberes", liegt er darunter, ist der Wert für das Jahr "unteres". Wenn der Wert identisch mit dem Median ist, ist der Wert "Median".

<https://www.youtube.com/watch?v=-zOaiuB6RVs>