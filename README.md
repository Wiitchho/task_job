# Zkomprimování souborů .log

Script na zkomprimování logu ve složce
`/var/log` Program by měl ušetřit místo přepsáním do formátu .gzip. Poté vymaže uložené logy ve formátu `.log` a ponechá
pouze logy ve formátu `.gz`

## Instalace cron

Program se bude spouštět automaticky pomoci crontabu každý 1. den v měsíci.

Otevřeme si terminál a pomoci příkazu `crontab -e` se dostaneme do editoru. pomoci písmene `i` začneme insert nastavením
crontabu:

    0 0 1 * * python3 /path/to/gzip_task.py

Poté zadáme `esc` tím vyskočíme z insert, odsadíme a napíšeme `:wq` pro uložení a ukončení editoru.

## Instalace pytest

1. Otevřete svůj macOS terminal.
2. Napište „pip install pytest“ bez uvozovek a stiskněte Enter.
3. Pokud to nefunguje, zkuste `pip3 install pytest` nebo `python -m pip install pytest`.
4. Počkejte na úspěšné ukončení instalace.
5. Restartuj svůj terminál, jdi do adresáře, kde máš skript a pust `pytest`

## Použití
skript se spouští pomoci argumentu `python3 gzip_task.py /var/log`
Soubory po zazipování se smažou a zůstanou pouze .gzip soubory.

