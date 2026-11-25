#!/usr/bin/env python3
"""Build entry.png: a one-page newspaper summary of 24 Nov 2026 world news.

My own design: cream broadsheet, red masthead rule, one lead story,
a 3x2 grid of shorter stories, and a markets strip at the foot.
Deterministic: fixed fonts, fixed layout, no randomness, no network.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 48

INK = (26, 26, 26)
RED = (155, 28, 28)
PAPER = (246, 241, 231)
CARD = (255, 253, 247)
GREY = (96, 92, 84)
RULE = (196, 188, 172)
NAVY = (28, 32, 48)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap returning a list of lines that fit `width`."""
    lines, current = [], ""
    for word in text.split():
        trial = f"{current} {word}".strip()
        if draw.textlength(trial, font=fnt) <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def tracked(draw, xy, text, fnt, fill, tracking=3):
    """Draw text with extra letter spacing, returning the width used."""
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + tracking
    return x


def draw_card(draw, box, kicker, headline, body):
    x0, y0, x1, y1 = box
    draw.rounded_rectangle(box, radius=6, fill=CARD, outline=RULE, width=1)
    draw.rectangle([x0, y0 + 8, x0 + 6, y1 - 8], fill=RED)
    tx = x0 + 20
    tw = x1 - x0 - 40
    draw.text((tx, y0 + 12), kicker, font=font(SANS_BOLD, 19), fill=RED)
    y = y0 + 42
    for line in wrap(draw, headline, font(SERIF, 27), tw):
        draw.text((tx, y), line, font=font(SERIF, 27), fill=INK)
        y += 33
    y += 4
    for line in wrap(draw, body, font(SANS, 21), tw):
        draw.text((tx, y), line, font=font(SANS, 21), fill=GREY)
        y += 26


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead ----
    d.rectangle([MARGIN, 40, W - MARGIN, 44], fill=RED)
    tracked(d, (MARGIN, 58), "THE WORLD IN ONE PAGE",
            font(SANS_BOLD, 28), RED, tracking=4)
    d.text((MARGIN, 96), "24 November 2026",
           font=font(SERIF, 66), fill=INK)
    d.text((MARGIN, 178), "TUESDAY  •  WORLD NEWS SUMMARY",
           font=font(SANS_BOLD, 25), fill=GREY)
    d.line([MARGIN, 228, W - MARGIN, 228], fill=INK, width=3)

    # ---- lead story ----
    lx0, ly0, lx1, ly1 = MARGIN, 248, W - MARGIN, 428
    d.rounded_rectangle([lx0, ly0, lx1, ly1], radius=6, fill=CARD,
                        outline=INK, width=2)
    d.rectangle([lx0, ly0 + 10, lx0 + 8, ly1 - 10], fill=RED)
    tx = lx0 + 28
    d.text((tx, ly0 + 14), "LEAD  •  BUSINESS",
           font=font(SANS_BOLD, 23), fill=RED)
    d.text((tx, ly0 + 46), "Huang Is Back at Nvidia",
           font=font(SERIF, 48), fill=INK)
    deck = ("Jensen Huang is reinstated as chief executive — Nvidia shares "
            "jump about 30% and Wall Street rebounds.")
    y = ly0 + 106
    for line in wrap(d, deck, font(SANS, 25), lx1 - lx0 - 56):
        d.text((tx, y), line, font=font(SANS, 25), fill=GREY)
        y += 31

    # ---- 3x2 story grid ----
    stories = [
        ("UKRAINE", "Zaporizhzhia Hit Overnight",
         "Two killed and about 40 wounded, including children."),
        ("GAZA", "Six Killed in Gaza Strikes",
         "Israeli strikes kill at least six Palestinians, including two police officers."),
        ("IRAN", "Tehran Vows “All Tools”",
         "Iran says it will use “all tools” against the US naval blockade."),
        ("CLIMATE", "COP31 Collapses",
         "Climate talks end with no deal on fossil fuels."),
        ("NEPAL & ASIA", "Quake Shakes Nepal",
         "A 5.6-magnitude earthquake strikes near the China border."),
        ("ELSEWHERE", "Seoul’s $375,000 Bounty",
         "South Korea offers up to $375,000 to catch AI cheating in exams."),
    ]
    gx0, gy0 = MARGIN, 444
    gap = 14
    cw = (W - 2 * MARGIN - 2 * gap) // 3
    ch = 214
    for i, (kicker, headline, body) in enumerate(stories):
        col, row = i % 3, i // 3
        x0 = gx0 + col * (cw + gap)
        y0 = gy0 + row * (ch + gap)
        draw_card(d, (x0, y0, x0 + cw, y0 + ch), kicker, headline, body)

    # ---- markets strip ----
    my0, my1 = 902, 972
    d.rounded_rectangle([MARGIN, my0, W - MARGIN, my1], radius=8, fill=NAVY)
    line1 = "MARKETS      S&P 500  +4.7%      Nasdaq  +6.5%      Nikkei  +3.9%"
    line2 = "Gold  $3,620      Brent  $86.7"
    f1, f2 = font(SANS_BOLD, 26), font(SANS, 24)
    w1 = d.textlength(line1, font=f1)
    d.text(((W - w1) / 2, my0 + 8), line1, font=f1, fill=(255, 255, 255))
    w2 = d.textlength(line2, font=f2)
    d.text(((W - w2) / 2, my0 + 40), line2, font=f2, fill=(200, 204, 216))

    # ---- source line ----
    src = "Sources: Just Security Early Edition • The Global Eye • Horizon"
    w = d.textlength(src, font=font(SANS, 17))
    d.text(((W - w) / 2, 988), src, font=font(SANS, 17), fill=GREY)

    img.save("entry.png", format="PNG")
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
