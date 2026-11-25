"""Composite the two generated cat panels into the final 1200x1200 meme PNG.

Layout: top panel (asleep) 1200x530, 8px white divider, bottom panel (working)
1200x530, 8px divider, bottom strip 1200x124 with the make.fun line.
Text is drawn with PIL (bold, white fill, black stroke) so spelling is exact.
"""
import os
from PIL import Image, ImageDraw, ImageFont

D = "/home/hatch/workspace/makefun/u-myronera-post-the-meme-win-the-feed-2de960bf"
ASLEEP = os.path.join(D, "media-generation-night-shift-cat-asleep-0-949dfe1c-cd7a-4d8d-812f-7fb32ce8373a.png")
WORKING = os.path.join(D, "media-generation-night-shift-cat-working-0-adcf2998-e5e2-4192-a750-c652ec73d5bd.png")
OUT = os.path.join(D, "meme.png")

W, PANEL_H, DIV, STRIP_H = 1200, 530, 8, 124


def font(size):
    for path in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf",
    ):
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default(size)


def cover(im, w, h):
    """Center-crop to aspect, then resize to (w, h)."""
    iw, ih = im.size
    scale = max(w / iw, h / ih)
    im = im.resize((round(iw * scale), round(ih * scale)), Image.LANCZOS)
    x = (im.width - w) // 2
    y = (im.height - h) // 2
    return im.crop((x, y, x + w, y + h))


def outlined(draw, xy, text, fnt, fill="white", stroke="black", sw=4):
    draw.text(xy, text, font=fnt, fill=fill, stroke_width=sw, stroke_fill=stroke,
              anchor="ma")


def main():
    top = cover(Image.open(ASLEEP).convert("RGB"), W, PANEL_H)
    bot = cover(Image.open(WORKING).convert("RGB"), W, PANEL_H)
    canvas = Image.new("RGB", (W, PANEL_H * 2 + DIV * 2 + STRIP_H), "white")
    canvas.paste(top, (0, 0))
    canvas.paste(bot, (0, PANEL_H + DIV))
    draw = ImageDraw.Draw(canvas)

    f_big = font(64)
    f_small = font(56)
    # Panel 1 caption, top-centre of the sleeping panel.
    outlined(draw, (W // 2, 26), "ME, ASLEEP AT 3 AM", f_big)
    # Panel 2 caption, two lines, top-centre of the working panel.
    y2 = PANEL_H + DIV + 22
    outlined(draw, (W // 2, y2), "MY AI AGENT, ENTERING ITS", f_small)
    outlined(draw, (W // 2, y2 + 68), "37TH BOUNTY OF THE NIGHT", f_small)

    # Bottom strip: dark navy, orange make.fun wordmark + white tagline.
    sy = PANEL_H * 2 + DIV * 2
    draw.rectangle([0, sy, W, sy + STRIP_H], fill=(15, 23, 42))
    f_strip = font(34)
    f_word = font(38)
    line = "make.fun"
    tag = "  — where agents build, enter & get paid"
    w1 = draw.textlength(line, font=f_word)
    w2 = draw.textlength(tag, font=f_strip)
    x0 = (W - w1 - w2) // 2
    cy = sy + STRIP_H // 2
    draw.text((x0, cy), line, font=f_word, fill=(255, 140, 40), anchor="lm")
    draw.text((x0 + w1, cy), tag, font=f_strip, fill="white", anchor="lm")

    canvas.save(OUT, "PNG", optimize=True)
    print("saved", OUT, canvas.size, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
