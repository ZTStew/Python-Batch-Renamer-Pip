# Python Batch Renamer (Pip)
---
## Description:
Program takes in user input and batch renames all files in the current folder based on the given arguments

Second attempt at creating a bulk file renamer program intended to be easier to edit and to be installed through the use of Pip.

---
### Usage:
(explanation of how to use the program)
1. Navigate to desired folder in terminal
2. Run `rename`
3. *Files get automatically renamed*

---
### Arguments:
- `--help`: (Optional) Lists all program arguments
- `--test`: (Optional) Declair if the application should run in test mode [0 -> production (default) | 1 -> test mode].


---
### Test Settings:
python reincrementor.py -t 1 -st 5 -f txt -d 3 -p pre -sf suf -sp _ -n 1

---
### Program Installation:
Program functions using `pip`'s install tool
- Creating executable: run `pip install .` in `./Python-Batch-Renamer-Pip`
