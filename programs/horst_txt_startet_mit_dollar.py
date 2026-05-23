import pathlib
this_folder = pathlib.Path(".")
for file in this_folder.glob("*_de.txt"):
	#if this_folder.is_file():
	print(file)
	with open(file) as myfile:
		lines = myfile.readlines()
	#print(lines)
	new_lines = []
	found = False
	for line in lines:
		if line.strip().startswith("python3 "):
			print("replace!!!")
			correct = line.strip().replace("python3 ", "$ python3 ")
			print(correct)
			found = True
			new_lines.append(correct)
		else:
			new_lines.append(line)
	if found:
		with open(file, "w") as myfile:
			myfile.writelines(new_lines)	
		print("file changed")
	else:
		print("file skipped")
	#input("Enter")
		
	
