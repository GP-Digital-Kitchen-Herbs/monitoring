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

### Python und GrovePi

**INFORMATION**  
Python und GrovePi sind bereits auf den Raspberry Pi's des IoT-Kits vorinstalliert. Diese Schritte sind nur notwendig, wenn kein Raspberry Pi der TH-Köln verwendet wird. 

1. [Python 3](https://www.python.org/) installieren 
2. GroovePi+ installieren: [Seeedstudio-Wiki](http://wiki.seeedstudio.com/GrovePi_Plus/#setup-the-software-on-the-raspberry-pi).

### Monitoring
1. Dieses Repository klonen
    ```bash
    git clone https://github.com/GP-Digital-Kitchen-Herbs/monitoring
    ```
2. In das soeben geklonte Repository navigieren
    ```bash
    cd monitoring
    ```
3. Pakete installieren
    ```bash
    pip3 install -r requirements.txt
    ```

4. Die Konfigurationsdatei generieren:
    ```bash
    python3 generate_config.py
    ```
    Dieser Schritt generiert die Datei `conf.json` und füllt sie mit den nötigen Werten. Beim erneuten Generieren werden alle bisherigen Werte überschrieben. 
    Wenn ein Sensor deaktiviert werden soll, kann die Konfigurationsdatei neu generiert werden oder die entsprechende Zeile aus der `conf.json` entfernen. Bei Bedarf können Werte aus der bisherigen Konfiguration mittels des folgenden zusätzlichen Parameters in die neue Konfiguration übernommen werden: 
    ```bash 
    -k NAME_DES_SCHLÜSSELS [WEITERE SCHLÜSSEL]
    ```
   Andersherum können mittels des folgenden zusätzlichen Parameters nur bestimmte Schlüssel verändert werden:
   ```bash 
    -c NAME_DES_SCHLÜSSELS [WEITERE SCHLÜSSEL]
   ```

5. **Optional wenn der Ultrasonic-Ranger nicht verwendet wird**: Um den Ultrasonic-Ranger zu kalibieren muss folgender Befehl ausgeführt werden:
    ```bash 
    python3 generate_config.py -cu
    ```

6. Starten des Monitoring:
    ```bash
    python3 start.py
    ```
    Das Skript sendet die Sensorwerte der aktivierten Sensoren im definierten Interval an das Thingsboard Portal.

### Hinweise zum Starten der Skripte via SSH
Um das Monitoring im Hintergrund zu starten, sodass die Skripte nach der SSH Verbindung weiterhin laufen, kann eine Screen-Session gestartet werden.

#### Starten der Screen-Session
```bash
screen -dmS monitoring python3 start.py
```

#### Stoppen der Screen Session
1. Verbinden zur Screen Session
    ```bash
    screen -r monitoring
    ```
2. Beenden der Screen Session  
`Strg+A`, danach `k` und zuletzt `y`
   
## Verweise
- [Online Dokumentation](https://herbs-lit.jaykju.de/)
- [Literaturverzeichnis Repositrory](https://github.com/Bettlaken/K_H_Literature)
- Bild von: https://undraw.co/
