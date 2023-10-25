from os import getlogin, listdir, path

def cprint(data, silent=False):
	if silent:
		pass
	else:
		print(data)

def getPlayerLocation(silent=False):

	rbx_folder_path = f"C://Users/{getlogin()}/AppData/Local/Roblox/Versions"
	rbx_folder_items = listdir(rbx_folder_path)

	for rbx_folder_item in rbx_folder_items:
		if rbx_folder_item.startswith("version") == False:
			cprint(f"IGNORE: {rbx_folder_item} is not a folder, ignoring", silent)
			rbx_folder_items.remove(rbx_folder_item)
	cprint(f"FOUND: Found potential client locations: {rbx_folder_items}", silent)

	for version_folder in rbx_folder_items:
		version_folder_items = listdir(f"{rbx_folder_path}/{version_folder}")
		for version_folder_item in version_folder_items:
			if version_folder_item == "RobloxPlayerLauncher.exe":
				cprint(f"FOUND: Roblox Player has been found in folder: {rbx_folder_path}/{version_folder}", silent)
				player_path_txt = open("rbx_player.txt", "w")
				player_path_txt.write(f"{rbx_folder_path}/{version_folder}/RobloxPlayerLauncher.exe")
				player_path_txt.close()
				cprint("Roblox Player path has been saved to 'rbx_player.txt'.", silent)

def replaceRbxAssets():
	if path.isfile("rbx_player.txt"):
		player_path_txt = open("rbx_player.txt", "r+")

		if listdir(player_path_txt.read()):
			pass
		else:
			print("'rbx_player is invalid'. Saving the Roblox Player location.")
			getPlayerLocation(silent=True)
	else:
		correct_option = False
		while correct_option == False:
			option2 = str(input("""
			yes: Save the Roblox Player location to 'rbx_player.txt' and try again
			no: Exit the operation

			You have not saved the Roblox Player location to 'rbx_player.txt'.
			Do you want to run that operation and try again? """))

			if option2 == "yes":
				correct_option = True
				getPlayerLocation()
			elif option2 == "no":
				correct_option = True
			else:
				print("That operation is invalid. Try again.")

while True:
	option = int(input("""
	0. Exit the Roblox Client Modifier program
	1. Find the Roblox Player path and save it to a file named 'rbx_path.txt'
	2. Replace Roblox Player assets with the assets contained in the 'rbx_client' folder
	Enter the number for the operation you want to execute: """))

	if option == 0:
		exit()
	elif option == 1:
		getPlayerLocation()
	elif option == 2:
		replaceRbxAssets()
	else:
		print("That operation is invalid. Try again.")