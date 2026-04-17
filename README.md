# Python Batch Renamer (Pip)
---

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
- `--target` || `--phrase`: (Required) Target prhase for removal. Example: `-tg changeThis`
- `--new`: (Required) Value replacing target phrase. Example: `-nw changeTo`.
  - To replace with nothing, type \"blank\".
  - To replace with space, type \"space\".
- `--file`: (Optional) Defines if Batch-Renamer should target a specific file type containing the target phrase instead of all files containing the the target phrase. Example: `-f mp4`.
  - To batch rename folders/directories, type: `-f dir` or `-f folder`.

---
### Test Settings:
python reincrementor.py -t 1 -st 5 -f txt -d 3 -p pre -sf suf -sp _ -n 1

---
### Program Installation:
Program functions using `pip`'s install tool
- Creating executable: run `pip install .` in `./Python-Batch-Renamer-Pip`
