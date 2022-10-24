#Zkomprimování souborů .log
Script na zkomprimování logu ve složce -->
/var/log
Program by měl ušetřit místo přepsáním do formátu .gzip.
Poté vymaže uložené logy ve formátu .log a ponechá pouze logy ve formátu .gz


##Použití
Program se bude spouštět automaticky pomoci crontabu každý 30. den v měsíci.
