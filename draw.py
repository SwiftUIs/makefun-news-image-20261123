#!/usr/bin/env python3
"""Compose the 23 November 2026 newspaper front page (1024x1024 PNG).

All artwork is flat editorial illustration generated without text; every
word on the page is drawn here with real fonts, so nothing is garbled.
Run: python3 draw.py  ->  writes entry.png next to this file.
"""

from PIL import Image, ImageDraw, ImageFont
import os

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (18, 18, 18)
RED = (178, 34, 34)
GREY = (90, 90, 86)
RULE = (18, 18, 18)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning a list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, x, y, text, fnt, max_w, fill=INK, leading=6):
    lines = wrap(draw, text, fnt, max_w)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + leading
    return y


def cover(img, w, h):
    """Centre-crop an image to exactly w x h."""
    iw, ih = img.size
    scale = max(w / iw, h / ih)
    nw, nh = int(iw * scale + 0.5), int(ih * scale + 0.5)
    img = img.resize((nw, nh), Image.LANCZOS)
    left = (nw - w) // 2
    top = (nh - h) // 2
    return img.crop((left, top, left + w, top + h))


def load(name):
    return Image.open(os.path.join(HERE, "assets", name)).convert("RGB")


def main():
    page = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(page)
    mx = 36  # side margin
    right = W - mx

    # ---- masthead -------------------------------------------------------
    d.rectangle([0, 0, W, 8], fill=INK)
    d.text((W // 2, 26), "THE WORLD IN ONE DAY",
           font=font(SERIF_B, 58), fill=INK, anchor="ma")
    d.rectangle([mx, 104, right, 107], fill=RULE)
    d.rectangle([mx, 111, right, 112], fill=RULE)
    d.text((W // 2, 118), "MONDAY 23 NOVEMBER 2026",
           font=font(SANS_B, 30), fill=RED, anchor="ma")
    d.text((W // 2, 156), "Six stories from around the world, in one page",
           font=font(SERIF, 20), fill=GREY, anchor="ma")
    d.rectangle([mx, 188, right, 191], fill=RULE)

    # ---- lead story: COP31 ----------------------------------------------
    y0 = 206
    cop = cover(load("media-generation-cop31-antalya-0-3a71573c-5a93-4400-bbd9-5457a9543e90.webp"), 560, 262)
    page.paste(cop, (mx, y0))
    tx = mx + 584
    d.text((tx, y0 + 2), "CLIMATE  •  ANTALYA, TURKEY",
           font=font(SANS_B, 17), fill=RED)
    y = draw_wrapped(d, tx, y0 + 34, "COP31 ENDS WITH NO DEAL",
                     font(SERIF_B, 40), right - tx, leading=4)
    y = draw_wrapped(d, tx, y + 8,
                     "The EU and about 130 countries reject a draft text that leaves out fossil fuels. The summit closes without an agreement.",
                     font(SANS, 19), right - tx, leading=5)
    d.rectangle([mx, 486, right, 489], fill=RULE)

    # ---- row 2: Kyiv and markets -----------------------------------------
    y1 = 500
    col_w = (right - mx - 24) // 2
    # Kyiv, left
    kyiv = cover(load("media-generation-kyiv-mourning-0-dbbd90c0-3e9e-4922-a51f-34f9f9e578b5.webp"), col_w, 136)
    page.paste(kyiv, (mx, y1))
    d.text((mx, y1 + 143), "WAR IN UKRAINE  •  KYIV REGION",
           font=font(SANS_B, 15), fill=RED)
    y = draw_wrapped(d, mx, y1 + 168, "STRIKE ON DYMER KILLS AT LEAST 10",
                     font(SERIF_B, 27), col_w, leading=2)
    draw_wrapped(d, mx, y + 4,
                 "A Russian strike north of Kyiv kills at least 10 people. The region marks 23 November a day of mourning.",
                 font(SANS, 17), col_w, leading=4)
    # Markets, right
    x2 = mx + col_w + 24
    mkt = cover(load("media-generation-market-selloff-0-ac7b5dc3-5273-4a18-aae8-c07cd7df1c44.webp"), col_w, 136)
    page.paste(mkt, (x2, y1))
    d.text((x2, y1 + 143), "MARKETS  •  TOKYO AND NEW YORK",
           font=font(SANS_B, 15), fill=RED)
    y = draw_wrapped(d, x2, y1 + 168, "AI SELL-OFF SHAKES MARKETS",
                     font(SERIF_B, 27), col_w, leading=2)
    draw_wrapped(d, x2, y + 4,
                 "Shares in AI companies slide sharply. Japan's Nikkei falls 5.06%; the S&P 500 drops 3.7%.",
                 font(SANS, 17), col_w, leading=4)
    d.rectangle([mx, 782, right, 785], fill=RULE)

    # ---- row 3: three short stories ---------------------------------------
    y2 = 800
    third = (right - mx - 48) // 3
    stories = [
        ("US POLITICS", "DEMOCRATS WIN THE HOUSE, 258 SEATS",
         "Democrats clinch 258 House seats, their largest majority since 1992."),
        ("MEXICO", "MEXICO CAPTURES 'EL CHAPO ISIDRO'",
         "Mexican forces capture the FBI's most-wanted fugitive in Sinaloa."),
        ("SPORT  •  MOTOGP", "MÁRQUEZ TAKES EIGHTH TITLE",
         "Marc Márquez wins his eighth MotoGP title."),
    ]
    # MotoGP picture sits above the third panel's text
    moto = cover(load("media-generation-motogp-marquez-0-5577bb8b-58f6-4f59-bfd2-31b9f3a402e1.webp"), third, 76)
    badges = ["258", "FBI", None]
    for i, (kicker, head, cap) in enumerate(stories):
        x = mx + i * (third + 24)
        if i == 2:
            page.paste(moto, (x, y2))
            ty = y2 + 84
        else:
            d.rectangle([x, y2, x + third, y2 + 76], fill=(30, 58, 95) if i == 0 else (120, 30, 30))
            d.text((x + third // 2, y2 + 38), badges[i], font=font(SANS_B, 40),
                   fill=(255, 255, 255), anchor="mm")
            ty = y2 + 84
        d.text((x, ty), kicker, font=font(SANS_B, 14), fill=RED)
        y = draw_wrapped(d, x, ty + 22, head, font(SERIF_B, 20), third, leading=2)
        draw_wrapped(d, x, y + 4, cap, font(SANS, 14), third, leading=3)

    # ---- footer ------------------------------------------------------------
    d.rectangle([mx, 996, right, 999], fill=RULE)
    d.text((W // 2, 1004), "Every story above happened or was first reported on Monday 23 November 2026.",
           font=font(SERIF, 13), fill=GREY, anchor="ma")

    page.save(os.path.join(HERE, "entry.png"), "PNG", optimize=True)
    print("wrote entry.png", page.size)


if __name__ == "__main__":
    main()
