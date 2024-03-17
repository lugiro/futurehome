#!/bin/bash

# ON OFF STIKKONTAKT

# Sett inn IP-adresse for Futurehome HUB og bruk API bruker og passord
# Sett inn riktig topic og channel nr (her 10_0)
# val lik true  gir stikk ON
# val lik false gir stikk OFF

mosquitto_sub -h IP_adresse_FuturehomeHUB  -p 1884 \
  -u min_API_bruker -P mitt_API_passord -C 1 \
  -t pt:j1/mt:cmd/rt:dev/rn:zw/ad:1/sv:out_bin_switch/ad:10_0 \
  -m '{
    "serv": "out_bin_switch",
    "type": "cmd.binary.set",
    "val_t": "bool",
    "val": true,
    "props": {},
    "tags": null
  }'
