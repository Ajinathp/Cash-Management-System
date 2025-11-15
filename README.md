<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Project Info</title>
    <style>
        .bold-black {
            color: black;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <p class="bold-black">Cash Management System – Wholesale Banking Project</p>
    <p class="bold-black">Author: Ajinath Phalk</p>
</body>
</html>


--Simple code for Copying files from one locstion to another location--
# Define source and destination folders
$source = "D:\CMS"
$destination = "E:\Backup"

# Copy all files and subfolders recursively
Copy-Item -Path $source\* -Destination $destination -Recurse -Force

Write-Host "Files copied successfully from $source to $destination"