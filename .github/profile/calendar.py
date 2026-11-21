"""Lay out the day columns from github-profile-3d-contrib v0.9.3 for the README."""

from pathlib import Path
import re
from xml.etree import ElementTree as ET

SVG = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG)


def prepare(source, destination):
    root = ET.parse(source).getroot()
    # Select the group by its day tiles. The upstream image also includes
    # unrelated radar, language, star and fork panels.
    days = next(group for group in root.findall(f"{{{SVG}}}g")
                if any(tile.get("class", "").startswith("cont-top-") for tile in group.iter()))
    period = next(text.text for text in root.iter(f"{{{SVG}}}text")
                  if re.fullmatch(r"\d{4}-\d{2}-\d{2} / \d{4}-\d{2}-\d{2}", text.text or ""))
    total = root.find(".//*[@class='fill-strong']").text
    plot = ET.Element(f"{{{SVG}}}svg", width="1280", height="420",
                      viewBox="0 0 1280 420", role="img", attrib={"aria-labelledby": "title"})
    ET.SubElement(plot, "title", id="title").text = f"{total} GitHub contributions, {period}"
    plot.append(root.find(f"{{{SVG}}}style"))
    ET.SubElement(plot, "rect", width="1280", height="420", attrib={"class": "fill-bg"})
    ET.SubElement(plot, "text", x="34", y="54", attrib={
        "class": "fill-strong", "style": "font: 32px Georgia, serif"
    }).text = f"{total} contributions"
    ET.SubElement(plot, "text", x="1246", y="54", attrib={
        "class": "fill-weak", "text-anchor": "end", "font-size": "21"
    }).text = period.replace(" / ", "  —  ")
    days.set("transform", "translate(25 47) skewY(-24)")
    plot.append(days)
    ET.ElementTree(plot).write(destination, encoding="utf-8")


if __name__ == "__main__":
    for mode in ("light", "dark"):
        name = f"calendar-{mode}.svg"
        prepare(Path("profile-3d-contrib") / name, Path("assets") / name)
