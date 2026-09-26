param(
    [string]$dirPath,
    [string]$methodName
)

if (!(Test-Path $dirPath)) {
    mkdir ${dirPath}
}

$content = Get-Content ".\template"
$content = $content -replace "XXXXXXXXXXXXXXX", ${methodName}
Set-Content "${dirPath}\main.py" ${content}
Copy-Item ".\template.run.ps1" "${dirPath}\run.ps1"
new-item -Path "${dirPath}\1.txt" -ItemType File
new-item -Path "${dirPath}\2.txt" -ItemType File
new-item -Path "${dirPath}\3.txt" -ItemType File
