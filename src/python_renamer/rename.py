
import os

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



def rename_directories(arguments):
  print(arguments)

# # function removes "phrase_to_remove" from "phrase" and replaces it with "replace_with" and re-adds "file_type"
# def remove_phrase(phrase, phrase_to_remove, replace_with, file_type):
#   # cuts phrase based on phrase_to_remove
#   cut = phrase.split(phrase_to_remove)
#   out = ""

#   # loops through cut and reconstructs new phrase
#   val = 0
#   while val < len(cut):
#     # adds each index to out
#     out += cut[val]

#     val += 1
#     # prevents replace_with from being added to the end of the phrase
#     if val < len(cut):
#       out += replace_with

#   out = out.strip()

#   out += "." + file_type

#   return out


# # Itterates through all file_type files found in given directory
# for input_file in arg.input_files:
#   # Gitbash is unable to handle non-unicode symbols potentially crashing the program
#   try:
#     # removes file extension from input_file name
#     renamed_file = input_file.split("." + arg.file_type)[0]
#     # removes any trailing whitespaces
#     renamed_file = renamed_file.strip()
#     # removes file path from renamed_file
#     renamed_file = os.path.basename(renamed_file)

#     # checks if phrase_to_remove is found in file name 
#     if arg.phrase_to_remove in renamed_file:
#       # removes phrase
#       update_file = remove_phrase(renamed_file, arg.phrase_to_remove, arg.replace_with, arg.file_type)
#       # updates existing file with new name
#       os.rename(input_file, update_file)
#       print("Task completed: " + input_file + " -> " + update_file)

#   except:
#     errors.append(input_file)

# # Informs user there are errors that occured
# if len(errors) > 0:
#   print("ERRORS Detected: " + str(len(errors)))
