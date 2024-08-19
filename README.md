# web-font-utils
Scrape characters of fonts in your web page for two-stage font loading.

---
## Prerequisite
Need to install browser for playwright as below:
```
playwright install
```

## Usage

### Scrape your web page
```
python main.py scrape -h    
INFO: Showing help with the command 'main.py scrape -- --help'.

NAME
    main.py scrape - Scrape the text of web page.

SYNOPSIS
    main.py scrape URL

DESCRIPTION
    Scrape the text of web page.

POSITIONAL ARGUMENTS
    URL
        Page url

NOTES     
    You can also use flags syntax for POSITIONAL ARGUMENTS
```
Examples:
```
python main.py scrape -o output.json https://xuzhusheng.github.io/
```
Save output to outpus.json and print on screen as below:
```
[
  {
    "font": "Playfair Display",
    "style": "normal",
    "text": "BCHMRaceglmnostu",
    "unicode": "U+42-43,U+48,U+4D,U+52,U+61,U+63,U+65,U+67,U+6C-6F,U+73-75"
  },
  {
    "font": "Open Sans",
    "style": "normal",
    "text": "MXZabdeghnsuy",
    "unicode": "U+4D,U+58,U+5A,U+61-62,U+64-65,U+67-68,U+6E,U+73,U+75,U+79"
  },
  {
    "font": "Monsieur La Doulaise",
    "style": "normal",
    "text": "XZeghnsu",
    "unicode": "U+58,U+5A,U+65,U+67-68,U+6E,U+73,U+75"
  }
]
```

### Convert test to unicode range
```
python main.py unicode -h
INFO: Showing help with the command 'main.py unicode -- --help'.

NAME
    main.py unicode - Convert the input text and file to unicode range

SYNOPSIS
    main.py unicode <flags>

DESCRIPTION
    Convert the input text and file to unicode range

FLAGS
    -f, --file=FILE
        Type: Optional[]
        Default: None
        The path of input file
    -t, --text=TEXT
        Default: ''
        Input text
```
