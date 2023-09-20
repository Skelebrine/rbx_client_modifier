from os import getlogin, listdir

option = int(input("""
1. Find the Roblox Player path and save it to a file named 'rbx_path.txt'
2. Replace Roblox Player assets with the assets contained in the 'rbx_client' folder
Enter the number for the operation you want to execute: """))

if option == 1:
    rbx_folder_path = f"C://Users/{getlogin()}/AppData/Local/Roblox/Versions"
    rbx_folder_items = listdir(rbx_folder_path)

    for rbx_folder_item in rbx_folder_items:
        if rbx_folder_item.startswith("version") == False:
            print(f"IGNORE: {rbx_folder_item} is not a folder, ignoring")
            rbx_folder_items.remove(rbx_folder_item)
    print(f"FOUND: Found potential client locations: {rbx_folder_items}")

    for version_folder in rbx_folder_items:
        version_folder_items = listdir(f"{rbx_folder_path}/{version_folder}")
        for version_folder_item in version_folder_items:
            if version_folder_item == "RobloxPlayerLauncher.exe":
                print(f"FOUND: Roblox Player has been found in folder: {rbx_folder_path}/{version_folder}")
                player_path_txt = open("rbx_player.txt", "w")
                player_path_txt.write(f"{rbx_folder_path}/{version_folder}/RobloxPlayerLauncher.exe")
                player_path_txt.close()
                print("Roblox Player path has been saved to 'rbx_player.txt'.")
elif option == 2:
    pass
