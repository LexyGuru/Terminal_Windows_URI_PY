$defpath = [Environment]::GetFolderPath('Desktop')
cd $defpath
powercfg /list > $home/powerlog.txt