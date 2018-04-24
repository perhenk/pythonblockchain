
# Enkel blokkkjede

En proof of consept blokkkjede basert på
[Hackernoons](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46)
guide for hvordan bygge en blokkjede.


## Krav
Koden kjører på Python3.
Følgende avhengigheter kan installeres med pip:

> [sudo] pip install flask

For å starte applikasjonen:

> python3 app.py

Filene som slutter på .sh er skallscript [for Linux / Unix] som snakker med RestAPI som er
implementert i Flask. app.py inneholder web-grensesnittet mens blockchain.py implementerer
selve blokk-kjeden. 
