#!/bin/bash

# SJEKKER kWh FRA STIKKONTAKT

# Sett inn IP-adresse for Futurehome HUB og bruk API bruker og passord
# -C mottar ett telegram og avslutter
# Deretter gaar program i loop og venter paa nytt telegram
# Sett inn riktig topic og channel nr (her 10_0)
# Det kan ta ca 30 sekunder foer foerste telegram kommer

while true; do
  mosquitto_sub -h IP_adresse_FuturehomeHUB  -p 1884 \
  -u min_API_bruker -P mitt_API_passord -C 1 \
  -t pt:j1/mt:evt/rt:dev/rn:zw/ad:1/sv:meter_elec/ad:10_0 > stikk_kWh.txt

  mv stikk_kWh.txt ny_stikk_kWh.txt   #Flytter siste telegram til ny fil
  cat ny_stikk_kWh.txt                #Viser alle telgrammer
  python3 konverter_json_format.py    #Sorter ut tid og kWh-verdi fra det siste telegrammet
done
