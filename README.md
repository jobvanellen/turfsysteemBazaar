Turfsysteem studentenhuis "De Bazaar"
====================================
## Raspberry OS instellen
1. Zet Raspberry OS op een sd kaart met de raspberry imager
2. Gebruik headless setup om wifi en ssh in te stellen (op pc)
3. Zet de waveshare settings in config.txt om het scherm te kunnen gebruiken
4. Login met ssh (putty) en zet VNC aan via commando sudo raspi-config
5. Selecteer interfaces en zet VNC aan
6. Je kunt nu met VNC-viewer in het systeem komen

## Om het systeem op een raspberry pi te zetten:
1. Maak de folder /home/pi/Turfsysteem aan
2. Zet in deze folder, turfInterface.py, lijst.txt en de foto's in de juiste verhoudingen en gif format
3. Zorg de de namen van de foto's en de fotolocaties in lijst.txt overeenkomen
4. Installeer python3 -> sudo apt-get install python3
5. Instaleer guizero -> sudo pip3 install guizero
6. Installeer Pillow -> sudo pip3 install Pillow
7. run het turfsysteem -> python3 ~/Turfsysteem/turfInterface.py
