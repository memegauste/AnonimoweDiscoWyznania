![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)

# AnonimoweDiscoWyznania

## English

### An open-source discord bot for designations

##### What it is?
An discord.py bot requested by Slenderman. 

##### Dependencies (not required when using docker-compose)
* python3 (tested on 3.12.1)
* discord.py 2.3.2

##### How to write your own config?
Write your own config.json file:
```json
{
  "token": "EXAMPLE TOKEN HERE",
  "designation_id": "DESIGNATION CHANNEL ID FROM YOUR SERVER"
}
```

Configuration of field "designation_id" is NOT required (it's for serving response from private messages).

You can also set "cmd_prefix" field for changing prefix for additional commands (by default '!').

## Polski

### Otwartoźródłowy bot do platformy discord do wyznań

##### Co to jest?
Otwartoźródłowy bot do platformy discord naśladujący AnonimoweMirkoWyznania (znane z wykopu).

Prośba o wykonanie została przekazana do mnie od Slendermana.

##### Zależności (nie wymagane przy użyciu docker-compose)
* python3 (przetestowane na 3.12.1)
* discord.py 2.3.2

##### Jak napisać swój własny config?
Stwórz plik config.json i zamieść następujący słownik:
```json
{
  "token": "TOKEN BOTA TUTAJ",
  "designation_id": "KANAŁ WYZNAN Z TWOJEGO SERWERA"
}
```

Konfiguracja pola "designation_id" nie jest wymagana (służy tylko do obsługi prywatnych wiadomości).

Możesz także ustawić pole "cmd_prefix" dla zmiany prefixa dodatkowych komend (domyślnie '!').