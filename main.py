import json
from fire import Fire
import scraper
import asyncio
import utils

class Cli:
    """
    :param output: The path of output file
    :param pretty: Pretty print the result to std output
    """
    def __init__(self, *, output = None) -> None:
        self.__output = output

    def scrape(self, url):
        """Scrape the text of web page.

        :param url: Page url
        :returns: Text groupped by font name and font style
        """
        ret = asyncio.run(scraper.scrape(url))
        if self.__output:
            with open(self.__output, "w") as f:
                json.dump(ret, f)
        return json.dumps(ret, indent=2)

    def unicode(self, file = None, text = ""):
        """
        Convert the input text and file to unicode range
        :param text: Input text
        :param file: The path of input file
        :returns: Unicode range
        """
        content = ""
        if file:
            with open(file) as f:
                content = "".join(f.readlines())

        ret = utils.string_to_unicode_ranges(text + content)
        return ret

if __name__ == "__main__":
    Fire(component=Cli)
