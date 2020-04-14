<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">GPA - Digital Kitchen Herbs</h3>

---

<p align="center"> Sammlung von nützlichen Skripten, mit denen Kräuter über einen Raspberry Pi überwacht werden können
    <br> 
</p>

## Über
Gekaufte Küchenkräuter sind häufig sehr schwer lange am Leben zu erhalten. 
In diesem Guided Project soll eine Lösung entwickelt werden, mitwelcher diese länger halten.

Dafür sollen mit verschiedenen Sensoren die Kräuter überwacht werden und darauf aufbauend Empfehlungen gegeben werden.
Die Dafür nötigen Skripte befinden sich in diesem Repository.

## Installation

### Voraussetzungen
- Ohne IoT-Kit (grob):
    - [Python (3)](https://www.python.org/) installieren 
    - GroovePi+ installieren: [Seeedstudio-Wiki](http://wiki.seeedstudio.com/GrovePi_Plus/#setup-the-software-on-the-raspberry-pi).
    - Dann Schritte von Mit Iot-Kit
- Mit IoT-Kit:
    ```bash
    pip install requests
    ```
- Dieses Repo klonen. Am besten in
    ```bash
    /home/moxdlab/
    ```
    sodass folgende Struktur entsteht: 
    ```bash
    /home/moxdlab/digital-kitchen-herbs/..
     ```
- Sollte das Repo an eine andere Stelle geklont werden, so müssen die Pfade in den verschiedenen Skripten, welche auf den ``Tel_Helper`` oder den ``Conf_Helper`` angepasst werden.  
(TODO: Zu relativen Pfaden ändern)

### Nötige Anpassung

Um nun die Skripte ausführen zu können, müssen folgende Datein erstellt werden:

1. ``thingsboard-access.json`` im ``tel_helper-Ordner``
In diese Datei muss der Thingsboard-Token eingefügt werden.
    ```json
    {
    "token": "IHR_TOKEN"
    }
    ```
    
2. ``conf.json`` im ``conf_helper-Ordner``
In diese Datei wird die Konfiguration festgehalten. 
Darunter zum Beispiel der Pin / Port an dem ein Sensor angeschlossen ist oder auch in welchem Intervall die Sensoren ausgelesen werden.
   ```json
   {
     "Parameter1": "Wert",
     "Paramter2": 123456789
   }
    ```
    
Im zu wünschenden Skript kann einfach nach der Methode ``getValue`` gesucht werden, um die nötigen Parameter zu finden. 
Bei fehlen eines Parameters  erscheint eine Ausgabe.

## Ausführung und Verwendung
- Jedes Skript sollte immer nur ein Sensor oder eine Komponente ansprechen. 
- Die Skripte sind nach Sensor sortiert.
- Es können natürlich mehrere Skripte gleichzeitig ausgeführt werden.
- Dabei sollte jedoch beachtet werden
    - Zwei Skripte sollten nicht den gleichen Sensor gleichzeitig ansprechen.
    - Ein Sensor sollte immer vor der Ausführung des Skriptes eingesteckt werden.
- Skripte werden wie folgt ausgeführt:
    - In den jeweiligen Ordner navigieren
    ````bash
    cd /vollständiger/pfad/..
    ````
    - Skript starten
    ```bash
    python skript-name.py
    ```
    
   
## Verweise
- [Literaturverzeichnis](https://github.com/Bettlaken/K_H_Literature)

```
Readme-Template: https://github.com/kylelobo/The-Documentation-Compendium/blob/master/en/README_TEMPLATES/Standard.md#deployment
```
