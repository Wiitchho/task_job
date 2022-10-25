# Zkomprimování souborů .log

Script na zkomprimování logu ve složce -->
/var/log Program by měl ušetřit místo přepsáním do formátu .gzip. Poté vymaže uložené logy ve formátu .log a ponechá
pouze logy ve formátu .gz

## Instalace cron:

Program se bude spouštět automaticky pomoci crontabu každý 1. den v měsíci.

Otevřeme si terminál a pomoci příkazu 'crontab -e' se dostaneme do editoru. pomoci písmene 'i' začneme insert nastavením
crontabu:

    0 0 1 * * python3 /path/to/gzip_task.py

Poté zadáme 'esc' tím vyskočíme z insert, odsadíme a napíšeme ':wq' pro ukončení editoru


