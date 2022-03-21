[CmdLetbinding()]
param (
[decimal]$Number,
[string]$ROM
)

Import-Module .\crc32.psm1

$Basename = [System.IO.Path]::GetFileNameWithoutExtension($ROM)
$Directory = [System.IO.Path]::GetDirectoryName($ROM)
$ImgPath = "..\OfflineList\imgs\laqieer - Fire Emblem - Game Boy Advance\"
if($Number -gt 500){
   $ImgPath += "501-1000\"
}else {
   $ImgPath += "1-500\"
}

Get-Item $ROM
get-crc32 $ROM
Compress-Archive -Force -LiteralPath $ROM -DestinationPath ..\FE-ROM-Hack-Repo\ROMs\$Basename.zip
Remove-Item $ROM

get-crc32 $Directory\$Basename-0.png
get-crc32 $Directory\$Basename-1.png
Move-Item $Directory\$Basename-0.png $ImgPath"$Number"a.png
Move-Item $Directory\$Basename-1.png $ImgPath"$Number"b.png
