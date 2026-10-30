"""Renders the README figures in assets/: hero.png, pipeline.png (schematic), training.png.

usage: python tools/render_figures.py      (Pillow only)
Inputs: assets/app-ui.png (from tools/capture_ui.py) and tools/training_log.json (epoch_loss and
epoch_categorical_accuracy read from IsaretDiliProjesi/Logs/train with tensorboard's EventAccumulator).
Fonts (OFL) are in tools/fonts/: Outfit and DM Mono. Colours come from the app's Qt stylesheet.
"""
import json, os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.path.join(ROOT, "tools", "fonts")
OUT = os.path.join(ROOT, "assets")

# The app: #121212 window, #2C2C2C fields, #4A148C / #6A1B9A / #8E24AA purple buttons.
BG, PANEL, FIELD, LINE = "#0F0D13", "#18151E", "#2C2C2C", "#2E2838"
PURPLE_DK, PURPLE, PURPLE_LT, LILAC = "#4A148C", "#6A1B9A", "#8E24AA", "#C99BF0"
TEXT, SUB, MUTED = "#F2EEF7", "#B3A9C2", "#7E748C"
# MediaPipe drawing colours used in isaret_dili_araclari.py (BGR there, RGB here).
LEFT_JOINT, LEFT_BONE = (76, 22, 121), (250, 44, 121)
RIGHT_JOINT, RIGHT_BONE = (66, 117, 245), (230, 66, 245)

def font(name, size, weight=None):
    f = ImageFont.truetype(os.path.join(FONTS, name), size)
    if weight:
        f.set_variation_by_axes([weight])
    return f

DISPLAY = lambda s: font("Outfit.ttf", s, 700)
SEMI = lambda s: font("Outfit.ttf", s, 600)
BODY = lambda s: font("Outfit.ttf", s, 400)
MONO = lambda s: font("DMMono-Regular.ttf", s)
MONO_M = lambda s: font("DMMono-Medium.ttf", s)

def wrap(d, text, f, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= width:
            cur = t
        else:
            lines.append(cur); cur = w
    return lines + [cur]

def glow(im, xy, r, rgb, alpha):
    layer = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).ellipse([xy[0] - r, xy[1] - r, xy[0] + r, xy[1] + r], fill=rgb + (alpha,))
    im.alpha_composite(layer.filter(ImageFilter.GaussianBlur(r // 2)))

def shadow(im, box, r, offset=16, blur=26, alpha=150):
    layer = Image.new("RGBA", im.size, (0, 0, 0, 0))
    x0, y0, x1, y1 = box
    ImageDraw.Draw(layer).rounded_rectangle([x0, y0 + offset, x1, y1 + offset], r, fill=(0, 0, 0, alpha))
    im.alpha_composite(layer.filter(ImageFilter.GaussianBlur(blur)))

def chip(d, xy, text, f, fill=PURPLE, color=TEXT, pad=(16, 8)):
    x, y = xy
    w = d.textlength(text, font=f)
    h = f.size + 2 * pad[1]
    d.rounded_rectangle([x, y, x + w + 2 * pad[0], y + h], 10, fill=fill)
    d.text((x + pad[0], y + pad[1] - 1), text, font=f, fill=color)
    return x + w + 2 * pad[0]

def caption(d, x, y, fig, title):
    nx = chip(d, (x, y), f"Fig. {fig}", MONO_M(17))
    d.text((nx + 16, y + 1), title, font=SEMI(26), fill=TEXT)

# A schematic open right hand in MediaPipe's 21-landmark layout (normalised 0..1).
HAND = [(.50, .95), (.36, .86), (.26, .74), (.19, .63), (.13, .53), (.38, .56), (.36, .39), (.35, .28), (.34, .18),
        (.50, .53), (.50, .34), (.50, .22), (.50, .11), (.62, .56), (.64, .39), (.65, .28), (.66, .19),
        (.73, .63), (.78, .51), (.81, .43), (.84, .35)]
BONES = [(0, 1), (1, 2), (2, 3), (3, 4), (0, 5), (5, 6), (6, 7), (7, 8), (5, 9), (9, 10), (10, 11), (11, 12),
         (9, 13), (13, 14), (14, 15), (15, 16), (13, 17), (0, 17), (17, 18), (18, 19), (19, 20)]

def draw_hand(d, box, joint, bone, mirror=False, scale=1.0):
    x0, y0, x1, y1 = box
    pt = lambda p: (x0 + ((1 - p[0]) if mirror else p[0]) * (x1 - x0), y0 + p[1] * (y1 - y0))
    for a, b in BONES:
        d.line([pt(HAND[a]), pt(HAND[b])], fill=bone, width=max(2, int(3 * scale)))
    for p in HAND:
        x, y = pt(p); r = 6 * scale
        d.ellipse([x - r, y - r, x + r, y + r], fill=joint, outline=TEXT, width=max(1, int(1.5 * scale)))

def window(im, box, title, shot):
    """Windows-style dark window frame around the real Qt screenshot."""
    x0, y0, x1, y1 = box
    shadow(im, box, 12)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle(box, 12, fill="#1C1A21", outline=LINE, width=2)
    d.text((x0 + 18, y0 + 9), title, font=BODY(17), fill=SUB)
    gx = x1 - 34
    d.line([(gx - 6, y0 + 13), (gx + 6, y0 + 25)], fill=SUB, width=2); d.line([(gx - 6, y0 + 25), (gx + 6, y0 + 13)], fill=SUB, width=2)
    d.rectangle([gx - 52, y0 + 13, gx - 40, y0 + 25], outline=SUB, width=2)
    d.line([(gx - 98, y0 + 19), (gx - 86, y0 + 19)], fill=SUB, width=2)
    bar = 38
    s = shot.resize((x1 - x0 - 4, y1 - y0 - bar - 2), Image.LANCZOS)
    mask = Image.new("L", s.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, -20, s.width, s.height], 10, fill=255)
    im.paste(s, (x0 + 2, y0 + bar), mask)

def card(im, box):
    shadow(im, box, 16, offset=12, blur=20, alpha=170)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle(box, 16, fill=PANEL, outline=LINE, width=2)
    return d

def hero():
    W, H = 1800, 860
    im = Image.new("RGBA", (W, H), BG)
    glow(im, (1350, 300), 460, (106, 27, 154), 110)
    glow(im, (300, 820), 300, (74, 20, 140), 90)
    d = ImageDraw.Draw(im)
    x, nx = 100, 100
    for t in ["MediaPipe", "LSTM", "PyQt5"]:
        nx = chip(d, (nx, 120), t, MONO_M(18), fill=PURPLE_DK if t != "MediaPipe" else PURPLE) + 10
    d.text((x - 4, 185), "Sign Language", font=DISPLAY(92), fill=TEXT)
    d.text((x - 4, 285), "Translator", font=DISPLAY(92), fill=LILAC)
    d.text((x, 410), "Teach it your own signs.", font=SEMI(38), fill=TEXT)
    y = 478
    for line in wrap(d, "A desktop app that tracks both hands with MediaPipe, reads 30-frame gesture "
                        "sequences with an LSTM network, and turns recognised signs into text and speech.", BODY(25), 560):
        d.text((x, y), line, font=BODY(25), fill=SUB); y += 37
    d.text((x, y + 30), "Digital Image Processing  ·  final project", font=MONO(17), fill=MUTED)
    d.text((x, y + 58), "Hüseyin Baran Işık", font=MONO(17), fill=MUTED)

    shot = Image.open(os.path.join(OUT, "app-ui.png")).convert("RGB")
    wx0, wx1, wy0 = 760, 1720, 110
    window(im, (wx0, wy0, wx1, wy0 + 38 + int((wx1 - wx0 - 4) * shot.height / shot.width) + 2), "İşaret dili çevirici", shot)

    # card 1: what the camera sees, as data
    d = card(im, (700, 470, 1110, 800))
    d.text((728, 494), "Per frame", font=MONO(16), fill=MUTED)
    draw_hand(d, (720, 520, 900, 760), LEFT_JOINT, LEFT_BONE, mirror=True, scale=0.75)
    draw_hand(d, (900, 520, 1080, 760), RIGHT_JOINT, RIGHT_BONE, scale=0.75)
    d.text((728, 762), "2 hands × 21 points × (x, y, z) = 126", font=MONO(15), fill=SUB)
    # card 2: the trigger
    d = card(im, (1150, 540, 1720, 740))
    d.text((1180, 566), "Blink to translate", font=SEMI(30), fill=TEXT)
    # Outfit has no "≥" glyph, so the rule is spelled out
    for i, line in enumerate(wrap(d, "When an eye blink is detected (eye aspect ratio below 0.34), the last 30 frames "
                                     "go to the LSTM. A word is accepted only at 65 % confidence or more.", BODY(21), 510)):
        d.text((1180, 616 + i * 31), line, font=BODY(21), fill=SUB)
    return im.convert("RGB")

def arrow(d, x0, x1, y):
    d.line([(x0, y), (x1 - 4, y)], fill=PURPLE_LT, width=3)
    d.polygon([(x1, y), (x1 - 12, y - 7), (x1 - 12, y + 7)], fill=PURPLE_LT)

def pipeline():
    W, H = 1800, 600
    im = Image.new("RGBA", (W, H), BG)
    glow(im, (W - 150, 80), 280, (106, 27, 154), 80)
    d = ImageDraw.Draw(im)
    caption(d, 70, 48, 2, "From a hand to a word (schematic)")
    top, h, w, gap = 140, 400, 230, 52
    xs = [70 + i * (w + gap) for i in range(6)]
    for x in xs:
        d.rounded_rectangle([x, top, x + w, top + h], 16, fill=PANEL, outline=LINE, width=2)
    for i in range(5):
        arrow(d, xs[i] + w + 8, xs[i + 1] - 8, top + h // 2)
    head = lambda x, t, s: (d.text((x + 20, top + 20), t, font=SEMI(24), fill=TEXT), d.text((x + 20, top + 54), s, font=MONO(15), fill=MUTED))
    # 1 camera frame
    head(xs[0], "Camera frame", "OpenCV, every 30 ms")
    d.rounded_rectangle([xs[0] + 20, top + 100, xs[0] + w - 20, top + 330], 10, fill="#000000")
    draw_hand(d, (xs[0] + 40, top + 115, xs[0] + w - 40, top + 320), RIGHT_JOINT, RIGHT_BONE, scale=0.8)
    # 2 landmarks
    head(xs[1], "Landmarks", "MediaPipe Holistic")
    for i, (lab, val) in enumerate([("left hand", "21 × 3"), ("right hand", "21 × 3"), ("no hand", "zeros"), ("one frame", "126")]):
        yy = top + 110 + i * 62
        d.rounded_rectangle([xs[1] + 20, yy, xs[1] + w - 20, yy + 48], 8, fill=FIELD)
        d.text((xs[1] + 34, yy + 12), lab, font=BODY(19), fill=SUB)
        d.text((xs[1] + w - 34 - d.textlength(val, font=MONO_M(18)), yy + 13), val, font=MONO_M(18), fill=LILAC)
    # 3 sequence
    head(xs[2], "Sequence", "last 30 frames")
    gx, gy, cell = xs[2] + 30, top + 105, 13
    for r in range(15):
        for c in range(13):
            shade = [PURPLE_DK, PURPLE, PURPLE_LT, "#3A2A4A"][(r * 7 + c * 3) % 4]
            d.rectangle([gx + c * cell, gy + r * cell, gx + c * cell + cell - 3, gy + r * cell + cell - 3], fill=shade)
    d.text((xs[2] + 20, top + 320), "30 × 126", font=MONO_M(24), fill=TEXT)
    # 4 LSTM
    head(xs[3], "LSTM network", "Keras, softmax output")
    for i, (lab, wdt) in enumerate([("LSTM 128", 1.0), ("LSTM 256", 1.0), ("LSTM 128", 1.0), ("Dense 64 · 32", .8), ("softmax", .6)]):
        yy = top + 105 + i * 50
        bw = int((w - 40) * wdt)
        d.rounded_rectangle([xs[3] + 20, yy, xs[3] + 20 + bw, yy + 38], 8, fill=PURPLE if i < 3 else PURPLE_DK)
        d.text((xs[3] + 34, yy + 8), lab, font=MONO_M(17), fill=TEXT)
    # 5 gate
    head(xs[4], "Accept?", "two checks")
    for i, (lab, val) in enumerate([("confidence", "≥ 0.65"), ("lead over #2", "≥ 0.10"), ("same as last word", "skip")]):
        yy = top + 110 + i * 70
        d.rounded_rectangle([xs[4] + 20, yy, xs[4] + w - 20, yy + 56], 8, fill=FIELD)
        d.text((xs[4] + 34, yy + 6), lab, font=BODY(17), fill=SUB)
        d.text((xs[4] + 34, yy + 28), val, font=MONO_M(18), fill=LILAC)
    # 6 output
    head(xs[5], "Text + speech", "gTTS, else pyttsx3")
    d.rounded_rectangle([xs[5] + 20, top + 110, xs[5] + w - 20, top + 220], 8, fill=FIELD)
    d.text((xs[5] + 34, top + 124), "raw words", font=BODY(17), fill=MUTED)
    d.text((xs[5] + 34, top + 154), "word word …", font=MONO_M(19), fill=TEXT)
    d.rounded_rectangle([xs[5] + 20, top + 236, xs[5] + w - 20, top + 346], 8, fill=FIELD)
    d.text((xs[5] + 34, top + 250), "AI ÇEVİRİ: local rules", font=BODY(17), fill=MUTED)
    d.text((xs[5] + 34, top + 280), "Sentence.", font=MONO_M(19), fill=TEXT)
    return im.convert("RGB")

def training():
    log = json.load(open(os.path.join(ROOT, "tools", "training_log.json"), encoding="utf-8"))
    loss, acc = log["epoch_loss"], log["epoch_categorical_accuracy"]
    import math
    W, H = 1500, 880
    im = Image.new("RGBA", (W, H), BG)
    glow(im, (W - 120, 60), 260, (106, 27, 154), 80)
    d = ImageDraw.Draw(im)
    caption(d, 70, 48, 3, "Training log: 3 signs, 100 epochs (training set)")
    n = len(loss)
    px0, px1 = 150, W - 100

    def panel(top, bottom, title, values, ticks, fmt, to_y, color, note):
        d.rounded_rectangle([70, top, W - 60, bottom], 16, fill=PANEL, outline=LINE, width=2)
        d.text((100, top + 18), title, font=SEMI(22), fill=TEXT)
        d.text((W - 90 - d.textlength(note, font=MONO(16)), top + 22), note, font=MONO(16), fill=SUB)
        py0, py1 = top + 70, bottom - 50
        for v in ticks:
            y = py1 - to_y(v) * (py1 - py0)
            d.line([(px0, y), (px1, y)], fill=LINE, width=1)
            d.text((px0 - 12 - d.textlength(fmt(v), font=MONO(15)), y - 10), fmt(v), font=MONO(15), fill=MUTED)
        for e in [1, 20, 40, 60, 80, 100]:
            x = px0 + (e - 1) / (n - 1) * (px1 - px0)
            d.text((x - d.textlength(str(e), font=MONO(15)) / 2, py1 + 12), str(e), font=MONO(15), fill=MUTED)
        d.line([(px0 + i / (n - 1) * (px1 - px0), py1 - to_y(v) * (py1 - py0)) for i, v in enumerate(values)],
               fill=color, width=4, joint="curve")

    panel(120, 450, "Accuracy", acc, [0, .25, .5, .75, 1.0], lambda v: f"{v:.2f}", lambda v: v, LILAC,
          f"start {acc[0]:.2f} · best {max(acc):.2f} · end {acc[-1]:.2f}")
    # loss spans 0.004 to 19 508, so it needs a log axis
    lo, hi = -3, 5
    panel(480, 830, "Loss (log scale)", loss, [1e-3, 1e-1, 1e1, 1e3, 1e5],
          lambda v: f"1e{int(round(math.log10(v)))}", lambda v: (math.log10(max(v, 1e-3)) - lo) / (hi - lo), PURPLE_LT,
          f"spikes at epochs 16, 45, 76–89 · peak {max(loss):,.0f}")
    return im.convert("RGB")

if __name__ == "__main__":
    hero().save(os.path.join(OUT, "hero.png"), optimize=True)
    pipeline().save(os.path.join(OUT, "pipeline.png"), optimize=True)
    training().save(os.path.join(OUT, "training.png"), optimize=True)
    print("figures ->", OUT)
