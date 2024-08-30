import json
from fire import Fire
import scraper
import asyncio
from font_utils import get_metadata, subset_font
from unicode import unicodes
from css import fontface
from pathlib import Path

def dest_file(src, format):
    return Path(src).with_suffix(f".subset.{format}").name

def css_font_style(style):
    return "italic" if style == "Italic" else "normal"

def font_key(font):
    return (font["name"], font["style"])

def merge_metadata(local_font, web_font):
    return local_font | web_font | {"unicodes": unicodes(web_font["characters"])}

def generage_css(root, out, fonts, format):
    root_path = Path(root)        
    fontfaces = [
        fontface(**font | {"src": f'./{(root_path / out / dest_file(font["src"], format)).as_posix()}'})
        for font in fonts
    ]
    css = "\n\n".join(fontfaces)
    (Path(out) / "fonts-subset.css").write_text(css)
    return css

class Cli:
    """
    Optimize webfont loading. Create minimal subset of fonts on your web page for two-stage font loading.
    """
    @staticmethod
    def unicodes(url, output=None):
        """
        Find the characters of each font on the webpage.

        :param url: Page url.
        :param output: Output file.
        :returns: Characters and unicodes groupped by font name and font style.
        """
        async def func(url, output):   
            characters = await scraper.scrape(url)
            ret = [{"unicodes": unicodes(node["characters"])} | node for node in characters]
            if output:
                Path(output).parent.mkdir(parents=True, exist_ok=True)
                with open(output, "w") as f:
                    json.dump(ret, f)
            return json.dumps(ret, indent=2)
        
        return asyncio.run(func(url, output))

    @staticmethod
    def subset(path, url, format = "woff2", css = True, output = "", root = "./assets"):
        """ 
        Create minimal subset of fonts.
        
        :param path: Path of local fonts.
        :param url: Page url.
        :param format: Font format for subsetting.
        :param css: Whether to generate fontface for the subset fonts.
        :param output: Output directory.
        :param root: Asset root for generating fontface.
        """
        async def func(path, url, format, css, output, root):
            web_fonts = await scraper.scrape(url)
            local_fonts = [get_metadata(font) for font in Path().glob(path)]
            local_fonts_dict = {(font["name"], css_font_style(font["style"])): font for font in local_fonts}
            fonts = [merge_metadata(local_fonts_dict[font_key(font)], font)for font in web_fonts if font_key(font) in local_fonts_dict]
            Path(output).mkdir(parents=True, exist_ok=True)
            for font in fonts:
                subset_font(font["src"], format, font["unicodes"], (Path(output) / dest_file(font["src"], format)).as_posix())
            if css:
                return generage_css(root, output, fonts, format)
            
        return asyncio.run(func(path, url, format, css, output, root))

if __name__ == "__main__":
    Fire(component=Cli)
