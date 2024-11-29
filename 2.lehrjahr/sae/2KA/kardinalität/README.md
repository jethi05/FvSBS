# Kardinalität
# Kardinalität in Datenbanken

Die **Kardinalität** beschreibt die Art der Beziehung zwischen Tabellen in einer Datenbank und gibt an, wie viele Datensätze einer Tabelle mit Datensätzen einer anderen Tabelle verknüpft werden können.

## Typen der Kardinalität

### 1. Eins-zu-Eins (1:1)
Jeder Datensatz in Tabelle A ist mit höchstens einem Datensatz in Tabelle B verknüpft und umgekehrt.

- **Beispiel**: Eine Person hat genau einen Personalausweis.
- **Anwendung**: Wird verwendet, wenn Informationen in zwei Tabellen aufgeteilt werden sollen, z. B. aus Sicherheitsgründen.

**Darstellung**:
![Bild](https://help.tableau.com/current/pro/desktop/de-de/Img/1-1.png)
---

### 2. Eins-zu-Viele (1:N)
Ein Datensatz in Tabelle A kann mit mehreren Datensätzen in Tabelle B verknüpft sein, aber jeder Datensatz in Tabelle B gehört nur zu einem Datensatz in Tabelle A.

- **Beispiel**: Ein Kunde kann mehrere Bestellungen haben, aber jede Bestellung gehört genau einem Kunden.
- **Anwendung**: Häufigstes Muster in relationalen Datenbanken, z. B. bei hierarchischen Beziehungen.

**Darstellung**:

---

### 3. Viele-zu-Viele (M:N)
Ein Datensatz in Tabelle A kann mit mehreren Datensätzen in Tabelle B verknüpft sein, und ein Datensatz in Tabelle B kann ebenfalls mit mehreren Datensätzen in Tabelle A verknüpft sein.

- **Beispiel**: Studenten können mehrere Kurse belegen, und ein Kurs kann von mehreren Studenten belegt werden.
- **Anwendung**: Erfordert oft eine **Zwischentabelle** (Join-Tabelle), die die Beziehungen speichert.

**Darstellung**:


---

## Technische Umsetzung

Die Kardinalität wird oft durch **Fremdschlüssel** und Tabellenstrukturen dargestellt:

- **1:1**: Beide Tabellen enthalten eindeutige Schlüssel, und ein Fremdschlüssel verknüpft sie.
- **1:N**: Die Tabelle auf der "Viele"-Seite enthält einen Fremdschlüssel, der auf die "Eins"-Tabelle verweist.
- **M:N**: Eine Zwischentabelle wird erstellt, die die Primärschlüssel beider Tabellen als Fremdschlüssel enthält.

---

## Praktische Bedeutung

- Kardinalität hilft, Datenbankanfragen zu optimieren und Abhängigkeiten zwischen Tabellen zu definieren.
- Ein falsches Verständnis der Kardinalität kann zu inkorrektem Datenmodell führen, was die Datenintegrität gefährdet.

