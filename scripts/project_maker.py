from convert_video_to_images import create_images
from create_vbs_writer import create_vbs_writer
import os
from colorama import Fore, Back, Style, init

def main():
    print("\n=========================================================================================n")
    # Initialization of color printing
    init()

    # Get the path of the video, then creates the images directory in the project folder
    video_name = input("\nPlease enter the right name for the video with format (ex: my_video.mp4):\n")
    video_path = "videos/" + video_name
    while not os.path.isfile(video_path):
        video_name = input("The file has not been found in the '/video' folder, please enter a valid name: ")
        video_path = "videos/" + video_name

    try:
        # Get rid of the extension ('.mp4' for example) and creates the project directory
        project_name = video_name.split('.')[0]
        os.mkdir(project_name)
    except:
        raise(ValueError(Fore.RED + "A folder has already been created for this video, please remove it and start again"))
    
    images_directory = f"{project_name}/images"
    os.mkdir(images_directory)

    print(Fore.GREEN + f"Successfully created the projet folder under the name of '{project_name}'")



    # Get the max number of images to create and create the images
    max_number_of_images = input(Style.RESET_ALL + "\nPlease enter the maximum number of images you want to create for the video (type 'm' to transform the full video):\n")
    while not (max_number_of_images == 'm' or max_number_of_images.isdigit()):
        max_number_of_images = input("Please enter a valid input: ")
    
    print("Currently creating all the images, this step can take a few minutes, please wait.")
    create_images(video_path, images_directory, max_number_of_images)
    print(Fore.GREEN + "Successfully created all the images" + Style.RESET_ALL)



    # Run the pyinstaller command to create the '.exe' file, then move the file to the right directory and rename it to the project name
    print("\nStart building the 'exe' file:")
    os.system("pyinstaller --onefile .\scripts\display_video.py")
    os.system(f"move .\dist\display_video.exe {project_name}")
    os.system(f"ren .\{project_name}\display_video.exe {project_name}.exe")
    os.system("rd /s /q build")
    os.system("rd /s /q dist")
    os.system("del display_video.spec")
    print(Fore.GREEN + "Successfully created the executable file")



    # Creation of the vbs writer file if wanted, then create the exe file for the writer
    want_vbs = input(Style.RESET_ALL + "\nDo you want to create a vbs file to display a message box that launch the '.exe' file when closed ? (y or n)\n")
    while not (want_vbs == 'y' or want_vbs == 'n'):
        want_vbs = input("Please enter a valid input ('y' for yes, 'n' for no):")
    
    if want_vbs == 'y':
        vbs_title = input("\nPlease enter the title you want to display for your message box:\n")
        vbs_content = input("Please enter the text you want to display for your message box:\n")
        want_loop = input(Style.RESET_ALL + "\nDo you want to make the vbs file to loop and get duplicated ? (y or n)\n")
        while not (want_loop == 'y' or want_loop == 'n'):
            want_loop = input("Please enter a valid input ('y' for yes, 'n' for no):")
        
        if want_loop == 'y':
            create_vbs_writer(project_name, vbs_title, vbs_content, True)
        else:
            create_vbs_writer(project_name, vbs_title, vbs_content, False)
        
        # Run the pyinstaller command to create the '.exe' file, then move the file to the right directory
        print("\nStart building the 'exe' file:")
        os.system("pyinstaller --onefile set_vbs.py")
        os.system(f"move .\dist\set_vbs.exe {project_name}")
        os.system("rd /s /q build")
        os.system("rd /s /q dist")
        os.system("del set_vbs.spec")
        os.system("del set_vbs.py")
        print(Fore.GREEN + "Successfully created the executable file")




    # End printing
    print(Style.RESET_ALL + f"""
=========================================================================================
The project has been correctly created
To launch your project, you can start the '{project_name}.exe' file or the 'set_vbs.exe' file if you wanted a '.vbs'
Note that if you want to copy paste the folder on another computer, the vbs file will automatically be recognized as a virus
It will then be destroyed by the target's computer
In that case, run the 'set_vbs.exe' when the folder is already on the target's computer
""")


# Launch main
main()
