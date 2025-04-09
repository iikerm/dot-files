bold_code = "\033[1m"
uline_code = "\033[4m"
end_style_code = "\033[0m"

def formatAsError(text: str):
    text = "\033[91m" + text + end_style_code
    return text

def formatAsSuccess(text: str):
    text = "\033[92m" + text + end_style_code
    return text