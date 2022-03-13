$src = ".\OfflineList\datas\laqieer - Fire Emblem - Game Boy Advance.xml"
$link = "https://github.com/laqieer/FE-ROM-Hack-Database"
python3 Scripts\Convert.py "$src" _data\ROMs.csv --encoding=UTF-8
python3 Scripts\Convert.py "$src" Excel\ROMs.csv --encoding=UTF-8-SIG
rm -fo DATs/*
SabreTools ud -out=DATs -ot=all -rme -de='Fire Emblem ROM hacks' -c='Game Boy Advance' -hp="$link" -u="$link" -co="$link" -au=laqieer -em='laqieer@126.com' "$src"