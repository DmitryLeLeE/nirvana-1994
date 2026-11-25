# -*- coding: utf-8 -*-
"""Generates all retro graphics for the Nirvana memorial site.
Run once:  python tools/gen_assets.py
Idempotent (fixed random seeds). Windows font Arial Bold is used for text.
"""
import os
import random
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets")
os.makedirs(OUT, exist_ok=True)
FB = r"C:\Windows\Fonts\arialbd.ttf"


def tw(d, t, f):
    b = d.textbbox((0, 0), t, font=f)
    return b[2] - b[0], b[3] - b[1]


def bevel(d, xy, text, font, fill, dark, light, depth=2):
    x, y = xy
    d.text((x + depth, y + depth), text, font=font, fill=dark)
    d.text((x - 1, y - 1), text, font=font, fill=light)
    d.text((x, y), text, font=font, fill=fill)


def grad(w, h, c1, c2):
    img = Image.new("RGB", (w, h))
    px = img.load()
    for y in range(h):
        t = y / max(h - 1, 1)
        r = int(c1[0] + (c2[0] - c1[0]) * t)
        g = int(c1[1] + (c2[1] - c1[1]) * t)
        b = int(c1[2] + (c2[2] - c1[2]) * t)
        for x in range(w):
            px[x, y] = (r, g, b)
    return img


def save_gif(img, path):
    img.convert("P", palette=Image.ADAPTIVE).save(path)


# ---------- тайловая текстура фона ----------
random.seed(1994)
T = 96
tile = Image.new("RGB", (T, T), (216, 205, 180))
d = ImageDraw.Draw(tile)
for y in range(T):
    for x in range(T):
        if random.random() < 0.06:
            v = random.randint(170, 205)
            d.point((x, y), fill=(v, v - 6, v - 18))
for gy in range(0, T, 16):
    for gx in range(0, T, 16):
        d.point((gx, gy), fill=(188, 176, 152))
tile.save(os.path.join(OUT, "bg-tile.png"))

# ---------- мигающие бейджи ----------
def blink_badge(path, text, bg, fg_on, fg_off, w=64, h=24):
    frames = []
    for i in range(2):
        img = Image.new("RGB", (w, h), bg)
        d = ImageDraw.Draw(img)
        d.rectangle([0, 0, w - 1, h - 1], outline="#000000")
        f = ImageFont.truetype(FB, 16)
        tw2, th2 = tw(d, text, f)
        d.text(((w - tw2) // 2, (h - th2) // 2 - 2), text, font=f,
               fill=fg_on if i == 0 else fg_off)
        frames.append(img)
    frames[0].save(path, save_all=True, append_images=frames[1:], duration=500, loop=0)

blink_badge(os.path.join(OUT, "new.gif"), "NEW!", "#cc0000", "#ffff00", "#ffffff")
blink_badge(os.path.join(OUT, "hot.gif"), "HOT!", "#ff6600", "#ffffff", "#ffcc00")

# ---------- UNDER CONSTRUCTION ----------
frames = []
for i in range(2):
    img = Image.new("RGB", (360, 48), "#ffcc00")
    d = ImageDraw.Draw(img)
    for x in range(-48, 360 + 48, 24):
        d.polygon([(x, 48), (x + 12, 48), (x + 12 + 48, 0), (x + 48, 0)], fill="#000000")
    d.rectangle([38, 10, 322, 38], fill="#000000")
    f = ImageFont.truetype(FB, 20)
    w, h = tw(d, "UNDER CONSTRUCTION", f)
    d.text(((360 - w) // 2, (48 - h) // 2 - 2), "UNDER CONSTRUCTION", font=f,
           fill="#ffcc00" if i == 0 else "#ffffff")
    frames.append(img)
frames[0].save(os.path.join(OUT, "under-construction.gif"),
               save_all=True, append_images=frames[1:], duration=600, loop=0)

# ---------- радужный разделитель ----------
img = Image.new("RGB", (560, 8))
d = ImageDraw.Draw(img)
colors = ["#ff0000", "#ff8800", "#ffff00", "#00cc00", "#0088ff", "#8800ff"]
cw = 560 // 6
for i, c in enumerate(colors):
    d.rectangle([i * cw, 0, (i + 1) * cw - 1, 7], fill=c)
img.save(os.path.join(OUT, "divider.gif"))

# ---------- баннеры-шапки ----------
BANNERS = [
    ("index",       "IN MEMORY OF KURT COBAIN", (12, 20, 90),  (60, 90, 180),  (255, 215, 0)),
    ("about",       "THE BAND",                 (70, 10, 10),  (165, 42, 42),  (255, 255, 255)),
    ("timeline",    "TIMELINE",                 (10, 55, 10),  (45, 125, 45),  (255, 235, 130)),
    ("discography", "DISCOGRAPHY",              (45, 10, 75),  (115, 40, 165), (255, 255, 255)),
    ("kurt",        "KURT COBAIN",              (8, 55, 55),   (30, 130, 130), (255, 215, 0)),
    ("family",      "FAMILY",                   (65, 10, 40),  (155, 40, 100), (255, 255, 255)),
    ("death",       "DEATH & LEGACY",           (28, 28, 28),  (85, 85, 85),   (240, 240, 240)),
    ("27club",      "THE 27 CLUB",              (30, 5, 45),   (95, 20, 115),  (255, 90, 90)),
    ("songs",       "SONGS",                    (60, 30, 5),   (155, 95, 30),  (255, 240, 200)),
    ("quotes",      "KURT'S WORDS",             (10, 32, 65),  (45, 95, 155),  (150, 240, 255)),
    ("media",       "MEDIA",                    (18, 18, 18),  (62, 62, 72),   (130, 255, 130)),
    ("guestbook",   "GUESTBOOK",                (55, 32, 10),  (135, 82, 32),  (255, 222, 150)),
    ("links",       "SOURCES",                  (22, 26, 55),  (62, 72, 125),  (222, 222, 255)),
    ("scene",       "THE SCENE",                (8, 40, 20),   (30, 110, 60),  (255, 215, 0)),
]

for name, title, c1, c2, gold in BANNERS:
    img = grad(600, 80, c1, c2)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 599, 79], outline=(0, 0, 0))
    d.line([(0, 0), (599, 0)], fill=(255, 255, 255))
    d.line([(0, 1), (599, 1)], fill=(255, 255, 255))
    d.line([(0, 78), (599, 78)], fill=(0, 0, 0))
    f_small = ImageFont.truetype(FB, 16)
    f_big = ImageFont.truetype(FB, 34)
    bevel(d, (14, 6), "NIRVANA", f_small, gold, (60, 40, 0), (255, 255, 200))
    w, h = tw(d, title, f_big)
    bevel(d, (16, 34), title, f_big, (240, 240, 240), (40, 40, 40), (255, 255, 255))
    save_gif(img, os.path.join(OUT, "banner-%s.gif" % name))

# ---------- кнопки 88x31 ----------
def button(path, bg, text, fg, w=88, h=31, size=11):
    img = Image.new("RGB", (w, h), bg)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, w - 1, h - 1], outline=(0, 0, 0))
    d.line([(0, 0), (w - 1, 0)], fill=(200, 200, 200))
    d.line([(0, 0), (0, h - 1)], fill=(200, 200, 200))
    f = ImageFont.truetype(FB, size)
    tw2, th2 = tw(d, text, f)
    x = (w - tw2) // 2
    y = (h - th2) // 2
    d.text((x + 1, y + 1), text, font=f, fill=(0, 0, 0))
    d.text((x, y), text, font=f, fill=fg)
    save_gif(img, path)

button(os.path.join(OUT, "btn-netscape.gif"),  (90, 90, 90),   "GET NETSCAPE",     (255, 255, 255))
button(os.path.join(OUT, "btn-notepad.gif"),  (230, 230, 230), "MADE WITH NOTEPAD", (0, 0, 0))
button(os.path.join(OUT, "btn-guestbook.gif"), (0, 0, 0),      "SIGN MY GUESTBOOK", (255, 200, 0))
button(os.path.join(OUT, "btn-webring.gif"),  (0, 30, 80),     "NIRVANA WEBRING",  (130, 240, 130))
button(os.path.join(OUT, "btn-free.gif"),     (120, 10, 10),   "FREE HOMEPAGE!",   (255, 255, 0))

# ---------- баннер-реклама 468x60 ----------
frames = []
for i in range(2):
    img = Image.new("RGB", (468, 60), "#000066" if i == 0 else "#330000")
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 467, 59], outline="#ffff00")
    f = ImageFont.truetype(FB, 26)
    t1 = "CONGRATULATIONS!!"
    w1, h1 = tw(d, t1, f)
    d.text(((468 - w1) // 2, 4), t1, font=f, fill="#ffff00" if i == 0 else "#ffffff")
    f2 = ImageFont.truetype(FB, 18)
    t2 = "You are visitor 1,000,000 — CLAIM YOUR PRIZE!"
    w2, h2 = tw(d, t2, f2)
    d.text(((468 - w2) // 2, 36), t2, font=f2, fill="#ffffff" if i == 0 else "#ffff00")
    frames.append(img)
frames[0].save(os.path.join(OUT, "ad-banner.gif"),
               save_all=True, append_images=frames[1:], duration=500, loop=0)

# ---------- пиксельное пламя ----------
shapes = [
    [(7, 1, 2, 1, "#ff6600"), (6, 2, 4, 1, "#ff9900"), (7, 3, 2, 2, "#ffcc00"), (7, 5, 2, 1, "#ffee66")],
    [(8, 0, 1, 2, "#ff6600"), (7, 2, 2, 1, "#ff9900"), (6, 3, 4, 1, "#ff9900"), (7, 4, 2, 2, "#ffcc00")],
    [(7, 1, 2, 1, "#ff6600"), (6, 2, 4, 1, "#ff9900"), (7, 3, 2, 2, "#ffcc00"), (7, 5, 2, 1, "#ffee66")],
    [(6, 1, 4, 1, "#ff6600"), (7, 2, 2, 1, "#ff9900"), (6, 3, 4, 1, "#ff9900"), (7, 4, 2, 1, "#ffcc00"), (7, 5, 2, 1, "#ffee66")],
]
frames = []
for sh in shapes:
    img = Image.new("RGB", (16, 16), "#000000")
    d = ImageDraw.Draw(img)
    for x, y, w, h, c in sh:
        d.rectangle([x, y, x + w - 1, y + h - 1], fill=c)
    frames.append(img)
frames[0].save(os.path.join(OUT, "flame.gif"),
               save_all=True, append_images=frames[1:], duration=150, loop=0)

# ---------- почтовый ящик ----------
frames = []
for up in [True, False]:
    img = Image.new("RGB", (100, 70), "#d8cdb4")
    d = ImageDraw.Draw(img)
    d.rectangle([48, 30, 54, 66], fill="#666666")
    d.rectangle([10, 22, 90, 44], fill="#444444")
    d.rectangle([10, 22, 90, 26], fill="#555555")
    if up:
        d.rectangle([16, 8, 20, 22], fill="#cc0000")
        d.rectangle([20, 8, 30, 11], fill="#cc0000")
    else:
        d.rectangle([16, 18, 20, 22], fill="#cc0000")
        d.rectangle([20, 18, 30, 21], fill="#cc0000")
    f = ImageFont.truetype(FB, 14)
    d.text((6, 48), "EMAIL ME", font=f, fill="#000000")
    frames.append(img)
frames[0].save(os.path.join(OUT, "mailbox.gif"),
               save_all=True, append_images=frames[1:], duration=500, loop=0)

# ---------- favicon.ico (пиксельная свеча) ----------
icon = Image.new("RGBA", (32, 32), (18, 18, 22, 255))
d = ImageDraw.Draw(icon)
d.rectangle([13, 2, 18, 3], fill=(255, 102, 0, 255))
d.rectangle([11, 4, 20, 5], fill=(255, 153, 0, 255))
d.rectangle([12, 6, 19, 7], fill=(255, 204, 0, 255))
d.rectangle([14, 8, 17, 11], fill=(255, 238, 102, 255))
d.rectangle([15, 12, 16, 13], fill=(51, 51, 51, 255))
d.rectangle([12, 14, 19, 26], fill=(240, 234, 208, 255))
d.rectangle([14, 14, 17, 26], fill=(255, 255, 255, 255))
d.rectangle([8, 27, 23, 29], fill=(136, 102, 68, 255))
icon.save(os.path.join(ROOT, "favicon.ico"), sizes=[(16, 16), (32, 32)])

# ---------- og-image.png (1200x630) ----------
og = Image.new("RGB", (1200, 630), (216, 205, 180))
d = ImageDraw.Draw(og)
random.seed(94)
for _ in range(5000):
    x = random.randint(0, 1199)
    y = random.randint(0, 629)
    v = random.randint(180, 216)
    d.point((x, y), fill=(v, v - 4, v - 14))
d.rectangle([10, 10, 1189, 619], outline=(23, 19, 14), width=4)
d.rectangle([16, 16, 1183, 613], outline=(23, 19, 14), width=2)
f_big = ImageFont.truetype(FB, 150)
bevel(d, (120, 140), "NIRVANA", f_big, (23, 19, 14), (110, 90, 70), (255, 250, 240), depth=3)
f_sub = ImageFont.truetype(FB, 52)
bevel(d, (180, 350), "IN MEMORY OF KURT COBAIN", f_sub, (140, 16, 16), (60, 8, 8), (255, 240, 240), depth=2)
f_dates = ImageFont.truetype(FB, 40)
d.text((430, 430), "1967 - 1994", font=f_dates, fill=(60, 50, 40))
f_small = ImageFont.truetype(FB, 30)
d.text((250, 520), "a hand-made 1994 fan site", font=f_small, fill=(90, 75, 60))
og.save(os.path.join(ROOT, "og-image.png"))

# ---------- ещё реклама ----------
def fake_ad(path, bg1, bg2, text1, text2):
    frames = []
    for i in range(2):
        img = Image.new("RGB", (468, 60), bg1 if i == 0 else bg2)
        d = ImageDraw.Draw(img)
        d.rectangle([0, 0, 467, 59], outline="#ffff00" if i == 0 else "#ffffff")
        f = ImageFont.truetype(FB, 24)
        w1, h1 = tw(d, text1, f)
        d.text(((468 - w1) // 2, 4), text1, font=f, fill="#ffffff" if i == 0 else "#ffff00")
        f2 = ImageFont.truetype(FB, 16)
        w2, h2 = tw(d, text2, f2)
        d.text(((468 - w2) // 2, 36), text2, font=f2, fill="#ffff00" if i == 0 else "#ffffff")
        frames.append(img)
    frames[0].save(path, save_all=True, append_images=frames[1:], duration=600, loop=0)

fake_ad(os.path.join(OUT, "ad-ringtone.gif"), "#003300", "#330000",
        "FREE GRUNGE RINGTONES!", "call 1-900-GRUNGE now — $2.99/min, 18+")
fake_ad(os.path.join(OUT, "ad-homepage.gif"), "#000033", "#333300",
        "GET YOUR OWN FREE HOMEPAGE!", "no HTML skills needed — sign up today!!")
fake_ad(os.path.join(OUT, "ad-chat.gif"), "#330033", "#003333",
        "TALK GRUNGE LIVE!", "24/7 chat room — 56k modems welcome")

# ---------- ещё бейджи ----------
blink_badge(os.path.join(OUT, "wow.gif"), "WOW!", "#0000cc", "#ffffff", "#66ccff")
blink_badge(os.path.join(OUT, "cool.gif"), "COOL!", "#008800", "#ffffff", "#66ff66")

# ---------- анимированный радужный разделитель ----------
frames = []
cols = ["#ff0000", "#ff8800", "#ffff00", "#00cc00", "#0088ff", "#8800ff"]
for shift in range(6):
    img = Image.new("RGB", (560, 8))
    d = ImageDraw.Draw(img)
    cw = 560 // 6
    for i in range(6):
        c = cols[(i + shift) % 6]
        d.rectangle([i * cw, 0, (i + 1) * cw - 1, 7], fill=c)
    frames.append(img)
frames[0].save(os.path.join(OUT, "divider-anim.gif"),
               save_all=True, append_images=frames[1:], duration=200, loop=0)

print("DONE")
