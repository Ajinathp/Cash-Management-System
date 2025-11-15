# Cash-Management-System
Cash Management System – Wholesale Banking Project
<br>
Author : Ajinath Phalke
--Simple code for Copying files from one locstion to another location--
# Define source and destination folders
$source = "D:\CMS"
$destination = "E:\Backup"

# Copy all files and subfolders recursively
Copy-Item -Path $source\* -Destination $destination -Recurse -Force

Write-Host "Files copied successfully from $source to $destination"