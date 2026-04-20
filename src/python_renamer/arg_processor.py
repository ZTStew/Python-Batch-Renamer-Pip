
"""
Description:
  Function takes user provided arguments and parses them for problems or key codes
"""

def process_args(args):
  output = {}

  # targets program execution towards ./rename
  if args.test == 1:
    output["directory"] = ".\\rename"
  else:
    output["directory"] = ".\\"

  # handles target string parsing
  if args.target:
    if args.target.lower() == "space":
      output["target"] = " "
    else:
      output["target"] = args.target
  else:
    output["error"] = "ERROR: Required field [target] not found."

  # handles new string parsing
  if args.new:
    if "blank" in args.new.lower():
      output["new"] = ""
    elif "space" in args.new.lower():
      output["new"] = " "
    else:
      output["new"] = args.new
  else:
    output["error"] = "ERROR: Required field [new] not found."

  # handles file string parsing for file_types and directories
  if args.file:
    # check to handle directories being the program target
    if args.file.lower() == "dir" or args.file.lower() == "directory" or  args.file.lower() == "folder":
      output["file_type"] = "directory"
    # checks to handle file(s) being the program target
    else:
      output["file_type"] = args.file
      output["file_type"] = output["file_type"].strip(".")
  else:
    output["file_type"] = "*"

  return output
