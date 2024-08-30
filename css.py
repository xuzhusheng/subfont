def fontface(
    name, style, src, unicodes, wght=None, wdth=None, format="woff2", **kwargs
):
    weight = f"font-weight: {wght[0]:.0f} {wght[1]:.0f};" if wght else ""
    stretch = f"font-stretch: 100%;" if wdth else ""
    css = f"""
@font-face {{
  font-family: '{name}';   
  font-style: {style};   
  {weight}
  {stretch}
  font-display: swap;
  src: url({src}) format('{format}');
  unicode-range: {unicodes};
}}
    """
    return "\n".join([l for l in css.splitlines() if l.strip()])
