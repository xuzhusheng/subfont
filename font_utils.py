from fontTools import ttLib
import sys
from fontTools.subset import main as font_subset
from pathlib import Path


def get_metadata(font_path):
    font = ttLib.TTFont(font_path)
    names = ttLib.TTFont(font_path)["name"]
    meta = {
        "name": names.getDebugName(1),
        "style": names.getDebugName(2),
        "src": font_path.as_posix(),
    }
    
    try:
        meta = meta | {k:(v[0], v[-1]) for k, v in font["fvar"].getAxes().items()}
    except:
        ...
        
    return meta


def subset_font(font, format, unicodes, output):
    sys.argv = [
        None,
        font,
        f"--flavor={format}",
        f"--unicodes={unicodes}",
        f"--output-file={output}",
        "--ignore-missing-glyphs",
    ]
    font_subset() 
