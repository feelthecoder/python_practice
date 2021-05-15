import os, shutil

#MINI PROJECT :: CONSOLE FILE SEPARATOR
#Input a path/directory and this project will seprate all videos,audios,images,documents easily.

folderpath=input("Enter Path :")

print("1. Separate Only Same Directory Files\n2. Seprate Files from Sub-directories also\n")

choice = int(input("Enter Your Choice (1-2) : \n"))



folders = {
'video_extension' : ('.mp4','.mkv','.MKV','.flv','.mpeg'),
'audio_extension' : ('.mp3','.m4a','.wav','.flac'),
'document_extension' : ('.doc','.pdf','.txt','.ppt'),
'images_extension' : ('.png','.jpg','.jpeg')
}


print("Looking & Seprating Files..")

def file_finder2(folder_path,extension):
    files_path = []
    files = []
    for path,folder,file in os.walk(folder_path):   
        for i in file:
            for j in extension:
             if i.endswith(j):
                 files.append(i)
                 files_path.append(os.path.join(path,i))
    return files_path,files


def file_finder1(folder_path,extension):
    files = []
    for file in os.listdir(folder_path):   
        for ext in extension:
            if file.endswith(ext):
                files.append(file)
    return files

   



for extension_type,extension_tuple in folders.items():
          folder_name = extension_type.split('_')[0] + 'Files'
          folder_path= os.path.join(folderpath,folder_name)
          if choice==1:
                 list_files = file_finder1(folderpath,extension_tuple)
                 if(not list_files):
                        print(folder_name+" does not exists!")
                 if not os.path.isdir(folder_path) and list_files:
                        os.mkdir(folder_path)
                 for item in list_files:
                      item_path = os.path.join(folderpath,item)
                      item_new_path = os.path.join(folder_path,item)
                      shutil.move(item_path,item_new_path)
          elif choice==2:
                 list_files_dir,list_files = file_finder2(folderpath,extension_tuple)
                 if(not list_files):
                    print(folder_name+" does not exists!")
                 if not os.path.isdir(folder_path) and list_files:
                    os.mkdir(folder_path)
                 for item,dirs in zip(list_files,list_files_dir):
                           item_new_path = os.path.join(folder_path,item)
                           shutil.move(dirs,item_new_path)
          else:
              print("Wrong Choice!!")

          

print("Done!!")


