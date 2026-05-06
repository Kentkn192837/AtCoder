param(
    [string]$dirPath
)

mkdir $dirPath
Copy-Item .\template $dirPath\main.py
new-item -Path $dirPath\1.txt -ItemType File
