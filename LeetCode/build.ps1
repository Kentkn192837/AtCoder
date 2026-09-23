param(
    [string]$dirPath
)

mkdir ${dirPath}
Copy-Item ".\template" "${dirPath}\main.py"
new-item -Path "${dirPath}\1.txt" -ItemType File
new-item -Path "${dirPath}\2.txt" -ItemType File
new-item -Path "${dirPath}\3.txt" -ItemType File
