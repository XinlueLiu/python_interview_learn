import shutil
src = "/Volumes/Macintosh HD - Data/Users/xinlueliu/saved_files/python/file.py"
dest = "/Volumes/Macintosh HD - Data/Users/xinlueliu/saved_files/python/file_backup.py"
#copy file from src to dest. copy copies permission bits, while copyfile only copies the data
#copy2 will preserve the metadata. e.g. timestamps, and permission
shutil.copy2(src,dest)
#copymode will only copy the permission
#copystate will copy the permission and metadata
#copyfileobj copies the content of fsrc to fdst
#copytree copies entire directory recursively
src = "/Volumes/Macintosh HD - Data/Users/xinlueliu/saved_files/python"
dest = "/Volumes/Macintosh HD - Data/Users/xinlueliu/saved_files/python/tmp"
#shutil.copytree(src,dest)
#will remote entire directory
shutil.rmtree(dest)