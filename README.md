[![wakatime](https://wakatime.com/badge/user/b4602be3-3210-4922-b81d-ba8117864e8f/project/3ca7c904-d298-40bb-9d86-4007f864caad.svg)](https://wakatime.com/badge/user/b4602be3-3210-4922-b81d-ba8117864e8f/project/3ca7c904-d298-40bb-9d86-4007f864caad)
---
# Gauss'sches Eliminationsverfahren zur Lösung von Gleichungssystemen

Das Gauss'sche Eliminationsverfahren ist eine numerische Methode zur Lösung von Gleichungssystemen. Es ermöglicht die Lösung von Gleichungssystemen mit beliebig vielen Unbekannten, indem es die Koeffizientenmatrix des Systems durch eine oberdreieckige Matrix ersetzt. Anschließend kann das System durch Rückwärtssubstitution gelöst werden.

Dieses Programm implementiert das Gauss'sche Eliminationsverfahren in Python und ermöglicht es Benutzern, Gleichungssysteme mit beliebig vielen Unbekannten zu lösen. Es ist einfach zu bedienen und erfordert nur wenige Schritte, um ein Gleichungssystem zu lösen.

## Verwendung

Um dieses Programm zu verwenden, geben Sie einfach eine Matrix A und einen Vektor b ein, die das Gleichungssystem darstellen, das gelöst werden soll. Das Programm löst das Gleichungssystem und gibt den Lösungsvektor x zurück.

Um das Programm zu verwenden, müssen Sie Python auf Ihrem Computer installiert haben. Laden Sie dann die Datei `solve.py` herunter und speichern Sie sie in einem Verzeichnis auf Ihrem Computer. Öffnen Sie dann eine Eingabeaufforderung oder ein Terminalfenster, navigieren Sie zum Verzeichnis, in dem Sie `solve.py` gespeichert haben, und geben Sie den folgenden Befehl ein:

```sh
python solve.py -a "[[a11, a12, ..., a1n], [a21, a22, ..., a2n], ..., [an1, an2, ..., ann]]" -b "[b1, b2, ..., bn]"
```

Ersetzen Sie a11, a12, ..., ann durch die Koeffizienten des Gleichungssystems und b1, b2, ..., bn durch die Konstanten auf der rechten Seite des Gleichungssystems. Stellen Sie sicher, dass die Klammern und Kommas korrekt geschrieben sind.

## Beispiel

Angenommen, wir haben das folgende Gleichungssystem:

<ul>
<li style="list-style-type: none;">3x + 2y - z = 1</li>
<li  style="list-style-type: none;">2x - 2y + 4z = -2</li>
<li style="list-style-type: none;">-x + 0.5y - z = 0</li>
</ul>

Wir können dieses Gleichungssystem als eine Matrix A und einen Vektor b schreiben:

```python
A = [[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]]
b = [1, -2, 0]
```

Um dieses Gleichungssystem mit dem Gauss'schen Eliminationsverfahren zu lösen, geben wir den folgenden Befehl in der Eingabeaufforderung ein:

```zsh
python solve.py -a "[[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]]" -b "[1, -2, 0]"
```

Das Programm gibt den folgenden Lösungsvektor zurück:

```python
[ 1. -2. -2.]
```

Das bedeutet, dass die Lösung für das Gleichungssystem x = -0.06666667, y = 0.60000000 und z = 0.00000000 ist.
