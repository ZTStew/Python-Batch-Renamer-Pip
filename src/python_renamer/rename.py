
import os

# renames specificly files in given `target_files` list
def rename_files(arguments, target_files):
  print("Target Phrase: " + arguments["target"])
  print("New Phrase: " + arguments["new"])
  print("File Type: " + arguments["file_type"])

  # loops through and seperates relavent variables from each file found
  for file_name in target_files:
    out = f"Renaming file: {file_name} --> "

    file = {}
    # tracker for if a 'file[]' has been renamed
    file['file_changed'] = False
    # removes path from `file_name`
    file['file_name'] = file_name.split("\\")[-1]
    file['file_name'] = file['file_name'].split("/")[-1]
    # tracks file extention for reassembly
    file['file_type'] = file_name.split(".")[-1]
    # removes file type from file['file_name']
    file['file_name'] = file['file_name'].split("." + file['file_type'])[0]
    # tracks path to file being looked at
    file['file_path'] = os.path.dirname(file_name)

    # seperates file based on `target` value
    file['file_parts'] = file['file_name'].split(arguments['target'])

    file['file_name'] = ""
    i = 0
    # reassembles file['file_name'] with user arguments
    while i < len(file['file_parts']):
      # re-adds non-targeted file name parts
      file['file_name'] += file['file_parts'][i]

      # prevents new argument from being added to the end of the file
      i += 1
      # adds 'new' to file['file_name']
      if i < len(file['file_parts']):
        file['file_name'] += arguments["new"]
        # flag for if the file has been changed
        file['file_changed'] = True

    # ensures program only continues on `file` if something has changed 
    if file['file_changed']:
      file['file_name'] = file['file_name'].strip()

      # manually sets no directory to correct value
      if file['file_path'] == ".":
        file_full_path = ".\\"
      else:
        file_full_path = file['file_path'] + "\\"

      file_full_path += file['file_name'] + "." + file['file_type']

      # reports name change to user
      print(out + file['file_name'] + "." + file['file_type'])
      os.rename(file_name, file_full_path)



# renames specificly directories in given `directories` list
def rename_directories(arguments, directory_location, directories):
  print("Target Phrase: " + arguments["target"])
  print("New Phrase: " + arguments["new"])
  print("File Type: " + arguments["file_type"])


  # looks for directories containing 'target'
  for directory in directories:
    # tracker for user feedback
    out = f"Renaming directory: {directory} --> "

    # checks if target phrase is in directory's name
    if arguments["target"] in directory:
      new_directory_name = ""
      # splits directroy name into 'parts'
      parts = directory.split(arguments["target"])

      part = 0
      while part < len(parts):
        # readds each part to 'new_directory_name'
        new_directory_name += parts[part]

        # order prevents 'new' from being added at the end of all opperations
        part += 1
        # adds "new" to directory name
        if part < len(parts):
          new_directory_name += arguments["new"]

      print(out + new_directory_name)
      os.rename(directory_location[0] + "\\" + directory, directory_location[0] + "\\" + new_directory_name)

