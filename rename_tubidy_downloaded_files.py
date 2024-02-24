import os
import shutil
import pathlib
import re


def search_files(path):
    files = []
    
    for file in os.listdir(path):
        files.append(os.path.join(path, file))
    
    return files


while True:
    path = input("\n > Enter Path of Files: ") 
    path = pathlib.Path(path)
    files = search_files(path)
    
    for file in files:
        old_name = str(os.path.basename(file))
        new_name = old_name
        
        if "_" in old_name:
            new_name = re.sub("_", " ", old_name)
            
        if re.search("(aac\s*\d{5,10})", new_name):
            search = re.search("(aac\s*\d{5,10})", new_name)
            
            new_name = re.sub(str(search), "", new_name)
            
        new_name = new_name.title()
         
        print(f"=> {old_name} > {new_name}")
        
    print("")
            
		
	

	    