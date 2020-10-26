# Install Chocolatey
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

# Install Python
choco install -y python --version=3.7.9

# Install db0mb3r
cmd /C "refreshenv && python -m pip install --upgrade pip db0mb3r"

# Create desktop shortcut
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$Home\Desktop\db0mb3r.lnk")
$Shortcut.TargetPath = "C:\Python37\Scripts\db0mb3r.exe"
$Shortcut.Save()

# Run db0mb3r
C:\Python37\Scripts\db0mb3r.exe
