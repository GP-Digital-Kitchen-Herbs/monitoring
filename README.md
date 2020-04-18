<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://github.com/Bettlaken/K_H_Pictures/blob/master/undraw_Gardening.svg" alt="Project logo"></a>
</p>

<h3 align="center">GPA - Digital Kitchen Herbs</h3>

---

<p align="center">
    Script zum Senden der Monitoring Daten an das Thingsboard Portal
    <br> 
</p>

## Über
Gekaufte Küchenkräuter sind häufig schwer lange am Leben zu erhalten. 
In diesem Guided Project soll eine Lösung entwickelt werden, welche sich diesem Problem annimmt..

Dafür sollen mit verschiedenen Sensoren die Kräuter überwacht werden und darauf aufbauend Empfehlungen gegeben werden.
Die dafür nötigen Skripte befinden sich in diesem Repository.

## Installation

- Ohne IoT-Kit (grob):
    - [Python (3)](https://www.python.org/) installieren 
    - GroovePi+ installieren: [Seeedstudio-Wiki](http://wiki.seeedstudio.com/GrovePi_Plus/#setup-the-software-on-the-raspberry-pi).
    - Dann Schritte von Mit Iot-Kit
- Mit IoT-Kit:
    ```bash
    pip3 install requests
    ```
- Dieses Repo klonen.
- Die Konfigurationsdatei generieren:
    ```bash
    python3 generate_config.py
    ```
    Dieser Schritt generiert die Datei `conf.json` und füllt sie mit den nötigen Werten. Beim erneuten Generieren werden alle bisherigen Werte überschrieben. Wenn ein Sensor deaktiviert werden soll, kann die Konfigurationsdatei neu generiert werden oder die entsprechende Zeile aus der `conf.json` entfernen.
- Danach kann das Monitoring gestartet werden:
    ```bash
    python3 start.py
    ```
    Das Skript sendet die Sensorwerte der aktivierten Sensoren im definierten Interval an das Thingsboard Portal.
- Mit folgendem Aufruf kann das Monitoring im Hintergrund gestartet werden, sodass es auch nach dem Trennen der SSH Session aktiv bleibt:
    ```bash
    screen -dmS monitoring python3 start.py
    ```
- Um die Session zu stoppen muss zunächst wieder zu dieser verbunden werden:
    1. 'screen -r monitoring'
    2. Die Session beenden mit `Strg+A`, danach `k` und zuletzt `y`
   
## Verweise
- [Literaturverzeichnis](https://github.com/Bettlaken/K_H_Literature)
- Bild von: https://undraw.co/
