param(
    [string]$dirPath
)

mkdir ${dirPath}
Copy-Item ".\template" "${dirPath}\main.py"
Copy-Item ".\template.run.ps1" "${dirPath}\run.ps1"
new-item -Path "${dirPath}\1.txt" -ItemType File
new-item -Path "${dirPath}\2.txt" -ItemType File
new-item -Path "${dirPath}\3.txt" -ItemType File
