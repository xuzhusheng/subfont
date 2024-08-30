# Subfont
Optimize webfont loading. Create minimal subset of fonts on your web page for two-stage font loading.

---
## Prerequisite
Need to install browser for playwright as below:
```
playwright install
```

## Usage

```
python main.py -h
INFO: Showing help with the command 'main.py -- --help'.

NAME
    main.py - Optimize webfont loading. Create minimal subset of fonts on your web page for two-stage font loading.

SYNOPSIS
    main.py COMMAND | -

DESCRIPTION
    Optimize webfont loading. Create minimal subset of fonts on your web page for two-stage font loading.

COMMANDS
    COMMAND is one of the following:

     subset
       Create minimal subset of fonts.

     unicodes
       Find the characters of each font on the web page.
```
### Find the characters of each font on your webpage.
```
python main.py unicodes -h
INFO: Showing help with the command 'main.py unicodes -- --help'.

NAME
    main.py unicodes - Find the characters of each font on the web page.

SYNOPSIS
    main.py unicodes URL <flags>

DESCRIPTION
    Find the characters of each font on the web page.

POSITIONAL ARGUMENTS
    URL
        Page url.

FLAGS
    -o, --output=OUTPUT
        Type: Optional[]
        Default: None
        Output file.

NOTES
    You can also use flags syntax for POSITIONAL ARGUMENTS
```
Examples:
```
python main.py unicodes -o output.json https://xuzhusheng.github.io/
```
Save output to outpus.json and print on screen as below:
```
[
  {
    "unicodes": "U+20,U+58,U+5A,U+65,U+67-68,U+6E,U+73,U+75",
    "name": "Monsieur La Doulaise",
    "style": "normal",
    "characters": " XZeghnsu"
  },
  {
    "unicodes": "U+A,U+20,U+4D,U+58,U+5A,U+61-62,U+64-65,U+67-68,U+6E,U+73,U+75,U+79",
    "name": "Open Sans",
    "style": "normal",
    "characters": "\n MXZabdeghnsuy"
  },
  {
    "unicodes": "U+20,U+42-43,U+48,U+4D,U+52,U+61,U+63,U+65,U+67,U+6C-6F,U+73-75",
    "name": "Playfair Display",
    "style": "normal",
    "characters": " BCHMRaceglmnostu"
  }
]
```

### Create minimal subset of fonts for your webpage
```
python main.py subset -h
INFO: Showing help with the command 'main.py subset -- --help'.

NAME
    main.py subset - Create minimal subset of fonts.

SYNOPSIS
    main.py subset PATH URL <flags>

DESCRIPTION
    Create minimal subset of fonts.

POSITIONAL ARGUMENTS
    PATH
        Path of local fonts.
    URL
        Page url.

FLAGS
    -f, --format=FORMAT
        Default: 'woff2'
        Font format for subsetting.
    -c, --css=CSS
        Default: True
        Whether to generate fontface for the subset fonts.
    -o, --output=OUTPUT
        Default: ''
        Output directory.
    -r, --root=ROOT
        Default: './assets'
        Asset root for generating fontface.

NOTES
    You can also use flags syntax for POSITIONAL ARGUMENTS
```
Examples:
```
python main.py subset "fonts/*.woff2" https://xuzhusheng.github.io -o "fonts/subset" 
```
Create subset fonts in the output folder "fonts/subset" and generated css as below:
```
@font-face {
  font-family: 'Monsieur La Doulaise';
  font-style: normal;
  font-display: swap;
  src: url(./assets/fonts/subset/MonsieurLaDoulaise-Regular.subset.woff2) format('woff2');
  unicode-range: U+20,U+58,U+5A,U+65,U+67-68,U+6E,U+73,U+75;
}

@font-face {
  font-family: 'Open Sans';
  font-style: normal;
  font-weight: 300 800;
  font-stretch: 100%;
  font-display: swap;
  src: url(./assets/fonts/subset/OpenSans-VariableFont_wdth,wght.subset.woff2) format('woff2');
  unicode-range: U+A,U+20,U+4D,U+58,U+5A,U+61-62,U+64-65,U+67-68,U+6E,U+73,U+75,U+79;
}

@font-face {
  font-family: 'Playfair Display';
  font-style: normal;
  font-weight: 400 900;
  font-display: swap;
  src: url(./assets/fonts/subset/PlayfairDisplay-VariableFont_wght.subset.woff2) format('woff2');
  unicode-range: U+20,U+42-43,U+48,U+4D,U+52,U+61,U+63,U+65,U+67,U+6C-6F,U+73-75;
}
```
