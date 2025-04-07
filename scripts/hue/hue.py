import sys

scripts_path = "/home/.scripts" # Add your own path here
sys.path.append(scripts_path)   #So it can import things from .py files in .scripts dir
import stylelib as sts


if len(sys.argv) != 2:
    print(sts.formatAsError(" | Invalid options"))
    raise SystemExit

elif (not sys.argv[1].__contains__(",")) or sys.argv[1].__contains__("#"):
    # Waits for a hex color code with/without the '#'
    color = sys.argv[1].strip("#")

    alpha = None
    if len(color) != 3 and len(color) != 6:
        # Input was an invalid color
        print(sts.formatAsError(" | Non compatible color"))
        raise SystemExit

    rgb = []

    for i in range(0, 3):
        channel = ""
        for j in range(0, int(len(color)/3)):
            channel += color[int(i*len(color)/3 + j)]
        if len(channel) == 1:
            channel += channel
        rgb.append(int(channel, 16))
    
    rgb = str(rgb)
    rgb = rgb.strip("[").strip("]")
    print(rgb)

elif sys.argv[1].__contains__(",") and len(sys.argv[1].split(",")) == 3:
    # Waits for rgb
    color = sys.argv[1].split(",")
    h = ""
    for i in range(0, len(color)):
        color[i] = str(hex(int(color[i]))).strip("0x")
        h += color[i]

        if len(color[i]) == 1:
            h += color[i]
    
    print(h)

else:
    print(sts.formatAsError(" | Non compatible color"))
    raise SystemExit