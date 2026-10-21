import os

img = []
vid = []
doc = []
songs = []
codes = [] 
archive = []
others = []


images = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"]
videos = [".mp4", ".avi", ".mkv", ".mov"]
docs = [".pdf", ".docx", ".txt", ".pptx", ".xlsx"]
music = [".mp3", ".wav", ".aac"]
python = [".py"]
archives = [".zip", ".rar", ".7z"]

                                                                                                                           
Categories = [images, videos, docs, music, python, archives]
Categories_name = ["images", "videos", "docs", "music", "python", "archives"]
mini_category = [img, vid, doc, songs, codes, archive]


def read_files(path) :
    for item in os.listdir() :
        for category in Categories :
            for type in category :   
                if (item.lower().endswith(type)) :
                    sort_extension(type, item, path)
    sort_category(path)
                    

def sort_extension(x, y, path) :
    if x in images :
        img.append(y)
        
    elif x in videos :
        vid.append(y)
        
    elif x in docs :
        doc.append(y)
        
    elif x in music :
        songs.append(y)

    elif x in python :
        codes.append(y)
        
    elif x in archives :
        archive.append(y)        


def  sort_category(path) :
    for folder_name, file_list in zip(Categories_name, mini_category):
        move_file(folder_name, file_list, path)

    move_others(path)

    print_summery()

    for file_list in mini_category:
        file_list.clear()
    
    others.clear()
    

def move_file(directory_name ,items , path) :
    path1 = "C:\\Users\Admin\\Desktop\\organized file\\"
    if os.path.isdir(path1) :

        os.chdir(path1)
        if not os.path.exists(directory_name)  :
            os.mkdir(directory_name)
        


        for unit in items : 
            x = 1
            source = os.path.join(path,unit)
            destination = os.path.join(path1,directory_name,unit)
            while True :
                if os.path.exists(destination) :
                    x += 1
                    initial_block = unit.rfind(".")
                    result = unit[:initial_block] + " " + "(" + str(x) + ")" + unit[initial_block :]
                    destination1 = os.path.join(path1,directory_name,result)
                    destination = destination1
                else :
                    os.rename(source, destination)
                    break          
                                      

def print_summery() :
    total = 0
    destination ="C:\\Users\Admin\\Desktop\\organized file\\"

    print("============================================================================================================================================")
    print(f"saved location :   {destination}")
    print("============================================================================================================================================")

    for items in mini_category :
        total += len(items)
    print(f"total files :{total}")
    print(" ")
    for name, item in zip(Categories_name, mini_category) :
        print(f"{len(item)} files are transferred to {name}")


def move_others(path) :

    for items in os.listdir() :
        path2 = os.path.join(path,items)
        if os.path.isfile(path2) :
            others.append(items)  
    move_file("others",others,path)


def file_organizer() :
    while True :
        name = "FILE ORGANIZER"
        print("============================================================================================================================================")
        print(name.rjust(76))
        print("============================================================================================================================================")
        print("1. Organize Folder \n2. View Supported Categories \n3. Exit")
        choice = input("enter your choice :")
        if choice == "1" :
            path = input("enter your folder's path :")
            tf1 = os.path.isdir(path)
            if tf1 :
                os.chdir(path)
                read_files(path)
            else :
                print("PATH NOT FOUND !! \nTRY AGAIN")
        elif choice == "2" :
            path = input("enter your folder's path :")
            tf1 = os.path.isdir(path)
            if tf1 :
                os.chdir(path)
                print(os.listdir())
        elif choice == "3" :
            break

file_organizer()