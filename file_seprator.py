import os, shutil

#MINI PROJECT :: CONSOLE FILE SEPARATOR
#Input a path/directory and this project will seprate all videos,audios,images,documents easily.

folderpath=input("Enter Path :")

folders = {
'video_extension' : ('.mp4','.mkv','.MKV','.flv','.mpeg'),
'audio_extension' : ('.mp3','.m4a','.wav','.flac'),
'document_extension' : ('.doc','.pdf','.txt','.ppt'),
'images_extension' : ('.png','.jpg','.jpeg')
}


print("Looking & Seprating Files..")
def file_finder(folder_path,extension):
    files = []
    for file in os.listdir(folder_path):   # For each and every directory inside a directory you have to use os.walk(folder_path) method and other things will remains almost same.
        for ext in extension:
            if file.endswith(ext):
                files.append(file)
    return files

for extension_type,extension_tuple in folders.items():
          folder_name = extension_type.split('_')[0] + 'Files'
          folder_path= os.path.join(folderpath,folder_name)
          list_files = file_finder(folderpath,extension_tuple)
          if(not list_files):
              print(folder_name+" does not exists!")
          if not os.path.isdir(folder_path) and list_files:
            os.mkdir(folder_path)
          for item in list_files:
              item_path = os.path.join(folderpath,item)
              item_new_path = os.path.join(folder_path,item)
              shutil.move(item_path,item_new_path)
         

print("Done!!")


