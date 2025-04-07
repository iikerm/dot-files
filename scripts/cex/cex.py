# Clipboard command EXecution

import os
import sys

scripts_path = "/home/.scripts"     # Swap for your own path
sys.path.append(scripts_path)   # So it can import things from .py files in .scripts dir
import stylelib as sts


getIp = False
commandToExecute = ""

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print(sts.formatAsError(f" | Invalid syntax, please use {sys.argv[0]} <command>"))
    raise SystemExit
else:
    commandToExecute = sys.argv[1]
    if (sys.argv[1]) == "-i":
        commandToExecute = "ip addr | grep 'scope global'"
        getIp = True
    if sys.argv[1].__contains__("hue"):
        commandToExecute = commandToExecute.replace("hue", f"python3 {scripts_path}/hue/hue.py")
        print(commandToExecute)

if commandToExecute != "":
    result = os.popen(commandToExecute).read()

if getIp:
    result = ((result.replace("inet ", "")).split("/"))[0].strip()

if result == "":
    print(sts.formatAsError(f" | Command produced no output (") + commandToExecute + sts.formatAsError(")"))
    raise SystemExit
else:
    result = result.strip("\n")
    os.system(f"echo {result} | xclip -sel clip -r")
    if getIp:
        print(sts.formatAsSuccess(f" | Current IP copied to clipboard (") + result + sts.formatAsSuccess(")"))
    else:
        print(sts.formatAsSuccess(f" | Command output copied to clipboard (") + result + sts.formatAsSuccess(")"))
    
    raise SystemExit
