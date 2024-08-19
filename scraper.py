import asyncio
from playwright.async_api import async_playwright
from itertools import product
import re
from utils import string_to_unicode_ranges

JS_GET_TEXT_NODE = """
root => {
    const walker = document.createTreeWalker(
        root, 
        NodeFilter.SHOW_TEXT, 
    );

    let node;
    const textNodes = []

    while(node = walker.nextNode()) {
        const style = getComputedStyle(node.parentElement);
        textNodes.push([style.fontFamily, style.fontStyle, node.nodeValue])
    }
    
    return textNodes;
}
"""

async def scrape(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        await page.evaluate("document.fonts.ready")  # wait for  loading completed
        textNodes = await page.locator("body").evaluate(JS_GET_TEXT_NODE)

    for node in textNodes:
        node[0] = node[0].split(",")[0].replace('"', "")


    fonts = set([node[0] for node in textNodes])
    styles = set([node[1] for node in textNodes])

    ret = []
    for font, style in product(fonts, styles):
        characters = set(
            "".join([node[2] for node in textNodes if node[0] == font and node[1] == style])
        )
        text = re.sub("[\n ]", "", "".join(sorted(characters)))
        text and ret.append(
            {
                "font": font,
                "style": style,
                "text": text,
                "unicode": string_to_unicode_ranges(text),
            }
        )
    return ret

if __name__ == "__main__":
    URL = "http://localhost:5173"
    print(asyncio.run(scrape(URL)))
