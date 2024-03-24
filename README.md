# Futurehome og Raspberry Pi
Her vises en enkel kommunikasjon mellom Futurehome HUB og Raspberry Pi<br>
Data mottas/sendes fra/til Futurehome HUB, med MQTT, fra/til Raspberry Pi  

***Du trenger***<br>
- Futurehome HUB 2<br>
- Raspberry Pi 3B<br>
- Mac/PC<br>

***Forutsetninger***<br>
- Kunnskap om Raspberry Pi og installasjon<br>
- Bruk av **ssh** (Secure Shell)
- Bruk av CLI (Command Line Interface)<br>
- Linux kommandoer<br>
- Litt forståelse av API (Application Programming Interface)<br>
- Litt forståelse av MQTT (Message Queuing Telemetry Transport)<br>

***Installer Futurehome***<br>
Installer Futurehome HUB og last ned Futurehome app på telefon<br>
I app gå til Verktøy>husholdning>HUB-INSTILLINGE>LOKALT API OPPSETT<br>
Opprett bruker og passord for API og trykk lagre<br>
Benytter videre her **min_API_bruker** og **mitt_API_passord**<br>

***Legg til en enhet i Futurehome***<br>
I dette eksempelet er det benyttet en stikkontakt med kWh-måling, fra Cleverio, On/Off Receiver, med Zwave. <br>
I app gå til Verktøy/enheter/<br>
Klikk på enhet som er lagt til og deretter klikk på systemdata.<br>
Finn channel, i dette tilfellet er channel 10_0<br>

***IP-adresse for Futurehome HUB***<br>
Bruk et passende nettverksprogram for å finne IP-adresse for FuturehomeHUB, IP-adr blir automatisk tilordnet og kan endre seg.<br>
Typiske nettverk vil være 192.168.1.x eller 10.0.0.x<br>

***Installer MQTT Explorer på Mac/PC***<br>
MQTT Explorer er et program som viser MQTT data, se http://mqtt-explorer.com<br>
Logg inn på MQTT Explorer med **min_API_bruker** og **mitt_API_passord** og benytt port 1884<br>
I venstre vindu i Explorer vises alle enheter og deres data, finn kWh-måling for ad:10_0 og klikk på linjen<br>
På høyre side oppe, klikk på første symbol til høyre for Topic (Copy to clipboard).<br>
Aktuell topic for kWh-måling er da funnet, benyttes etter -t i CLI-kommando under<br>

***CLI-kommando***<br>
Bygg så opp følgende CLI-kommando, som senere skal benyttes i filen **kwh_mosquitto_loop_V1.sh** i Raspberry Pi:<br>
**mosquitto_sub -h IP_adr_FuturehomeHUB -p 1884 -u min_API_bruker -P mitt_API_passord -t pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:meter_elec/ad:10_0**<br>
Kommando henter kWh-verdi fra stikkontakt<br>

***Mosquitto***<br>
Installer Mosquitto på Raspberry Pi (mosquitto_pub og mosquitto_sub)<br>
For hjelp google **install mosquitto on Raspberry Pi**<br>

***Henta data fra Futurehome HUB***<br>
Henter kWh-data fra stikkontakt<br>
Last ned scriptfil **kwh_mosquitto_loop_V1.sh** og endre nødvendige parametre<br>
Husk chmod +x kwh_mosquitto_loop_V1.sh<br>
Start script **./kwh_mosquitto_loop_V1.sh**<br>
mosquitto_sub står nå og lytter på port 1884 for innkommende telgram i FIMP-format, bl.a. tid og kWh-verdi fra stikkontakt.<br>

***Sende data til Futurehome HUB***<br>
Styrer stikkontakt ON/OFF<br>
Last ned scriptfil **on_off_mosquitto_V1.sh** og endre nødvendige parametre<br>
Husk chmod +x on_off_mosquitto_V1.sh<br>
Start script **./on_off_mosquitto_V1.sh**<br>
I scriptfil:<br> 
**val** lik **true**  gir stikkontakt ON<br>
**val** lik **false** gir stikkontakt OFF<br>

FIMP-format er beskrevet her: https://github.com/futurehomeno/fimp-api<br><br>

***Hvordan finne ip-adresse for Futurehome HUB***<br>
Koble opp en Raspberry Pi i samme lokale nettverk som Futurehome HUB står i.<br>
Programmet **fh_get_ip_adr_v01.py** kjøres fra Raspberry Pi i CLI.<br>

Dersom lokal ruter benytter DHCP for å bestemme ip-adresse for Futurehome HUB<br>
kan python program **fh_get_ip_adr_v01.py** benyttes både til å finne ip-adresse i utgangspunktet,<br>
og også for å finne ny ip-adresse dersom denne endres.<br>
I detter eksempelet benyttes ip segment 192.168.1.x<br>

Det må installes nmap pg netcat for å benytte programmet.<br><br>

OBS! Programvaren brukes på eget ansvar og utgiver tar ikke noe ansvar for eventuell skade som kan skje ved bruk av programvaren.



