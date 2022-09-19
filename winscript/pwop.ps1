$defpath = [Environment]::GetFolderPath('Desktop')
cd $defpath
Copy-Item -Path powerlog.txt -Destination $home/powerlog.txt
