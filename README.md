<p style="font-size: 16px;">Cash-Management-System</p>
<br>
Cash Management System – Wholesale Banking Project
<br>
Author : Ajinath Phalke
<br>

------------------------------------------------------------------------------------------

Simple code for Copying files from one locstion to another location
Define source and destination folders
$source = "D:\CMS"
$destination = "E:\Backup"

Copy all files and subfolders recursively
Copy-Item -Path $source\* -Destination $destination -Recurse -Force

Write-Host "Files copied successfully from $source to $destination"