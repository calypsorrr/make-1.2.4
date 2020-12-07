#!/bin/bash
Sudo apt-get update # downloads de informatie voor alle pakjes.
Echo “update compleet”
Echo “verwijderen van ongebruikte file’s en pakjes”
Sudo apt-get autoremove # verwijderen alle pakjes die niet meer gebruikt worden door het systeem.
Sudo apt-get autoclean # ruimt alle files op dat niet meer gedownload kunnen worden en verwijderd die geen dat het systeem niet meer nodig heeft.
Echo “opkuisen compleet”
Echo “maken van kapotte pakjes 
PROGRAM=${1?Error: no name given}
Sudo dpkg-reconfigure -f PROGRAM # reconfigureren van een al geinstalleerd pakketje(phpmyadmin). (-f readline = hoe het reconfigureren gedaan moet worden)
Sudo dpkg-reconfigre -p critical phpmyadmin # hiermee is de setting naar critical verplaatst, dit wilt zeggen dat het systeem alleen iets zegt als het misschien stuk zou gaan. 
Sudo apt-get install -f # installeert alle pakjes opnieuw die gebroken waren en installeert pakjes die het systeem nodig zou hebben. (-f =  attempt to correct a system with broken dependencies in place.)
Echo “Gebroken pakjes gemaakt”
Echo “opnieuw aan het updaten”
Sudo apt-get update # downloads de informatie voor alle pakjes.
Echo “update finished”
Echo “upgrading”
Sudo apt-get upgrade # installeert vrijgekomen upgrades voor alle pakjes. 
Echo “finished”
exit
