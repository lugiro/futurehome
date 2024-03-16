# futurehome
Innholdet her viser en enkel måte for å motta/sende data fra/til Futurehome HUB med MQTT for overføring til Raspberry Pi  

Du trenger:<br>
Futurehome HUB 2<br>
Raspberry Pi 3B<br>
Mac/PC<br><br>

Installer Futurehome.<br> 
I app gå til Verktøy>husholdning>HUB-INSTILLINGE>LOKALT API OPPSETT<br>
Opprett bruker og passord og trykk lagre (benytter her min_bruker og mitt_passord)<br>

Legg til en enhet i Futurehome.<br>
I dette eksempelet er det benyttet en stikkontakt med kWh måling fra Cleverio, On/Off Receiver, med Zwave. <br>
I app gå til Verktøy/enheter/<br>
Klikk på enhet som er lagt til og deretter klikk på systemdata.<br>
Finn channel, i dette tilfellet er channel 10_0<br>

Bruk et passende nettverksprogram for å finne IP-adresse for FuturehomeHUB, IP-adr blir automatisk tilordnet og kan endre seg.<br>
Typiske nettverk vil være 192.168.1.x eller 10.0.0.x<br>

Installer MQTT Explorer på Mac/PC<br>
Logg inn på MQTT Explorer med min_bruker og mitt_passord og benytte port 1884.<br>
I venstre vindu i Explorer vises alle enheter og deres data, finn kWh-måling for ad:10_0 og klikk på linjen.<br>
På høyre side oppe klikk på første symbol til høyre for Topic (Copy to clipboard).<br>
Aktuell topic for kWh-måling er da funnet, benyttes etter -t under<br>

Bygg så opp følgende CLI-kommand (som senere skal benyttes i Raspberry Pi):<br>
mosquitto_sub -h IP_adr_FuturehomeHUB -p 1884 -u min_bruker -P mitt_passord -t pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:meter_elec/ad:10_0<br>

Benytt ssh mot Raspberry Pi fra Mac (evt. PC)<br>
Installer følgende på Raspberry Pi:<br>
Mosquitto, mosquitto_pub og mosquitto_sub<br>
Kjør så CLI-kommandi vist over fra Raspberry Pi<br>
mosquitto_sub står så å lytter på port 1884 og innkommende telgram med FIMP-format vises, bl.a. kWh-verdi fra stikkontakt.<br>
FIMP-format er beskrevet her 



