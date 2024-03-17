#importer json
import json

#Hent telegram fra fil
with open("ny_stikk_kWh.txt") as file:
    jdata = file.read().replace('\n',' ')
print(jdata)

#Konverter tekst til objekt
json_object = json.loads(jdata)

#Hent verdier i objekt
tid = json_object["ctime"]
kwh_verdi = json_object["val"]

print("Tid:",tid)
print("kWh-verdi:", kwh_verdi)
