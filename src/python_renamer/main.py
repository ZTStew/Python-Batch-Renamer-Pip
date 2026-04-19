
"""
Description:
  Program takes user input to bulk rename files or folders in the given folder. Does not apply recursively

File:
  File takes user input and feeds it to the rest of the program
"""

import argparse, glob, os, sys
from arg_processor import process_args
from rename import rename_files, rename_directories


def main():
  # Default phrase
  target_phrase = "test"
  # Default new phrase
  new_phrase = ""
  # Default file type
  file_type = ""
  # Default directory location
  directory = ".\\"

  target_phrase_help_text = """
    (Required) Target prhase for removal. Example: `-tg changeThis`\n
    To replace with space, type \"space\".
  """
  new_value_help_text = """
    (Required) Value replacing target phrase. Example: `-nw changeTo`.\n
    To replace with nothing, type \"blank\".\n
    To replace with space, type \"space\".
  """
  file_type_help_text = """
    (Optional) Defines if Batch-Renamer should target a specific file type containing the target phrase 
    instead of all files containing the the target phrase. Example: `-f mp4`.\n
    To batch rename folders/directories instead, type: `-f dir` or `-f folder`.
  """

  args = argparse.ArgumentParser(description="Program searches given folder for video files and trims a specified number of seconds from the start or the end of the video. The file is then saved in a specified location.")
  # command line option running program in "test" mode
  args.add_argument(
    "-t",
    "--test",
    type=int,
    help="(Optional) Declair if the application should run in test mode [0 -> production (default) | 1 -> test mode]."
  )
  # command line option for setting the target string
  args.add_argument(
    "-tg",
    "--target",
    "-ph",
    "--phrase",
    type=str,
    help=target_phrase_help_text
  )
  # command line option for setting new string value
  args.add_argument(
    "-nw",
    "--new",
    type=str,
    help=new_value_help_text
  )
  # command line option for specifying file type restriction
  args.add_argument(
    "-f",
    "--file",
    type=str,
    help=file_type_help_text
  )
  # gets `args` from command line
  args = args.parse_args()

  # # processes `args` and returns dictionary
  arguments = process_args(args)

  # kills program if an error is found in user input
  try:
    if arguments["error"]:
      print(arguments["error"])
      sys.exit()
  except:
    pass

  # Collects all files in given directory with matching extension
  if arguments["file_type"] == "directory":
    print("directory specified")
  else:
    # collects list of all files with the desired extention in the specified directory
    target_files = glob.glob(arguments["directory"] + "\\*." + arguments["file_type"])

    # function to rename each file in `target_files`
    rename_files(arguments, target_files)


if __name__ == "__main__":
  main()
