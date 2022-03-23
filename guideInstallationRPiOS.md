# GUIDE D'INSTALLATION DU LOGICIEL MAISON POUR AKAI MPD218

## Pré-requis : 

## -Une carte micro SD vierge (car les données stockées dessus seront effacées en installant Raspberry Pi OS)
## -un Ordinateur <span style="color: orange">FIXE</span> avec un port micro SD ou SD
## - un adaptateur microSD->SD si vous n'avez pas de port micro SD sur votre ordinateur
## - un Raspberry Pi 4
## - votre AKAI MPD218
## - des écouteurs ou une enceinte dotée d'une prise jack 3.5 mm 

<br/>

## 1) 
### Inserez la carte SD dans le port de votre ordinateur
<br/>

## 2) 
### Telechargez raspberry Pi OS sur votre PC (https://www.raspberrypi.com/software/operating-systems/)
![telechargementOS](telechargementOS.png)
### <span style="color: orange">Installez bien la version Legacy with Desktop </span>pour bien avoir Raspberry Pi OS 10 et pas 11
<br/>

## 3) 
### Telechargez BalenaEtcher (https://www.balena.io/etcher/)
![balena](balena.png)
<br/>

## 4) 
### Lancez BalenaEtcher et cliquez sur "Flash from file"
![balena1](balena1.png)
<br/>

## 5) 
### Cherchez le zip de Raspberry Pi OS et ouvrez le 
<br/>

## 6) 
### Cliquez sur "Select Target" et selectionnez la carte SD
![balena2](balena2.png)
<br/>

## 7) 
### cliquez sur "flash" et attendez (ça peut durer une dizaine de minutes)
### <span style="color: orange">Si le flash échoue </span>, votre carte n'est peut être pas vide, formatez la et réessayer
![balena3](balena3.png)
<br/>

## 8)
### <span style="color: orange">Une fois le flash terminé </span>, retirez la carte SD et inserez la microSD dans le Raspberry
<br/>

## 9)
### Branchez votre Rasberry :  le clavier et la souris, le HDMI à l'écran de votre PC fixe, et l'alimentation sur le secteur.
### <span style="color: orange">/!\ Si votre écran ne s'allume pas</span>, verifier le port de votre HDMI sur votre PC (IN et pas OUT) et essayez avec l'autre port microHDMI de votre Raspberry
![Cables](photoCables.jpg)
<br/>

## 10)
### Ne mettez pas de mot de passe, connectez vous au Wifi (Si la Wifi ne fonctionne pas, un partage de connexion fera l'affaire)
<br/>

## 11)
### Cliquez sur next à l'écran "update software"
<br/>

## 12)
### Cliquez sur restart pour redemarrer votre Raspberry après les mises à jour
![restart](restart.png)
<br/>

## 13)
### <span style="color: red">L'installation de raspberry PI OS est terminée</span> , maintenant, il vous faut recuperer le dossier contenant le logiciel necéssaire à la mise en route de l'AKAI. Pour cela, soit vous l'avez sur votre Drive ou une clé USB, soit il vous faut le récuperer sur notre GitLab commun (https://forge.iut-larochelle.fr)
![gitlab](gitlab.png)
<br/>


## 14)
### faites un clic droit sur l'icone de son en haut à droite et sélectionnez "AV Jack"
![Son](sonPanneau.png)
<br/>


## 15)
### Une fois le zip téléchargé, l'extraire sur le bureau
<br/>

## 17)
### branchez l'AKAI et le jack(ou enceintes) sur le Raspberry

## 16)
### Allez dans PTS-Sampler-2020-2021 puis faites un clic droit sur le dossier Sampler et sélectionnez <span style="color: orange">"ouvrir dans un terminal"</span>
<br/>

## 17)
### executez la commande ` sudo ./install.sh`
<br/>

## Le terminal va maintenant installer toutes vos dépendances puis <span style="color: orange">votre Raspberry va redémarrer</span>. Si vous n'avez rien débranché, <span style="color: red">votre AKAI devrait être fonctionnel</span>. Pour une utilisation sans écran, débranchez votre souris, HDMI et clavier, puis débranchez et rebranchez votre cable d'alimentation, et attendez 30 secondes avant de tester votre AKAI.
<br/>

## Dans tout les cas d'utilisations, <span style="color: orange">le câble d'alimentation doit être branché en dernier</span>, pour effectuer des tests avec l'écran allumé, pas besoin de redémarrer votre Raspberry à chaque fois, lancer un terminal avec l'icone en haut à gauche aura le même effet sur le lancement du logiciel.

