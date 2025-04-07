# Copy command EXecution (CEX)
This script will copy the result of executing the command it receives by argument to the device's clipboard

## Recommendations
It is recommended to add an alias to your `.bashrc` file (or similar, I use zsh so mine is .zshrc) so that you dont have to call: 
`$ python3 <path_to_script>/cex.py <args>` every time.
To do this go to the `.bashrc` file and add an entry as follows:  
`alias cex=python3 <path_to_script>/cex.py `
> [!IMPORTANT]
> Note the space at the end of the entry so that it can receive arguments

## Usage
If you followed the steps above, the usage is very simple:  
Normal usage:
 - `$cex <command>`

Special cases:  
- `$cex -i`  
  This is a shorthand for copying the current IP address of the device.
  
- `$cex hue <color>`  
  This is a shorthand for working with the `hue.py` script that is found in this repository.

If the command was successfull, an output will be shown with what was copied to the clipboard.
