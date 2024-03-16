# futurehome
Innholdet viser en enkel måte for å hente data fra Futurehome HUB med MQTT for overføring til Raspberry Pi  

Du trenger:<br>
Futurehome HUB 2<br>
Raspberri Pi 3B<br>
Mac/PC<br><br>

Installer Futurehome og legg til en enhet. I dette eksempelet er det benyttet en stikkontakt med kWh måling fra xxx
I app gå til Verktøy>husholdning>HUB-INSTILLINGE>LOKALT API OPPSETT
Opprett bruker og passor og trykk lagre (bruke videre min_bruker og mitt_passord)

For dette oppsettet benyttes ssh mot Raspberry Pi fra Mac (evt. kan PC benytes)<br>
Installer MQTT Explorer på Mac/PC<br> 

Installer følgende på Raspberry Pi:<br>
Mosquitto, mosquitto_pub og mosquitto_sub<br>

