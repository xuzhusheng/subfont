import asyncio
from playwright.async_api import async_playwright
from itertools import groupby

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

    def key_func(node):
        return (node[0].split(",")[0].replace('"', ""), node[1])
    
    def text_node(key, group):
        text = "".join([item[2] for item in group])
        return {
            "name": key[0],
            "style": key[1],
            "characters": "".join(sorted(set(text))),
        }

    return [text_node(k,g) for k, g in groupby(sorted(textNodes, key=key_func), key=key_func)]

if __name__ == "__main__":
    URL = "http://localhost:5173"
    print(asyncio.run(scrape(URL)))
