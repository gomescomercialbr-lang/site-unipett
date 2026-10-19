from PIL import Image, ImageDraw, ImageFont
import os

TEAL = (1, 193, 194, 255)
PINK = (255, 117, 176, 255)
CREAM = (250, 243, 230, 255)
INK = (32, 31, 34, 255)

os.makedirs("assets", exist_ok=True)


def draw_paw(size, teal=TEAL, pink=PINK, bg=None):
    img = Image.new("RGBA", (size, size), bg if bg else (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    s = size / 48.0

    def ov(cx, cy, rx, ry, color):
        d.ellipse([ (cx-rx)*s, (cy-ry)*s, (cx+rx)*s, (cy+ry)*s ], fill=color)

    # main pad
    ov(24, 31, 13, 10.5, teal)
    # toes
    ov(11, 16, 5.2, 5.2, pink)
    ov(20.5, 9, 5.6, 5.6, pink)
    ov(27.5, 9, 5.6, 5.6, pink)
    ov(37, 16, 5.2, 5.2, pink)
    return img


# ---- favicon set ----
fav512 = draw_paw(512)
fav32 = fav512.resize((32, 32), Image.LANCZOS)
fav32.save("assets/favicon.ico", sizes=[(32, 32)])
fav512.resize((192, 192), Image.LANCZOS).save("assets/favicon-192.png")

apple_canvas = draw_paw(180, bg=CREAM)
apple_canvas.convert("RGB").save("assets/apple-touch-icon.png")

# ---- standalone SVG (for reference / external use) ----
svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">
  <ellipse cx="24" cy="31" rx="13" ry="10.5" fill="#01C1C2"/>
  <circle cx="11" cy="16" r="5.2" fill="#FF75B0"/>
  <circle cx="20.5" cy="9" r="5.6" fill="#FF75B0"/>
  <circle cx="27.5" cy="9" r="5.6" fill="#FF75B0"/>
  <circle cx="37" cy="16" r="5.2" fill="#FF75B0"/>
</svg>
'''
with open("assets/logo-petvida.svg", "w", encoding="utf-8") as f:
    f.write(svg)

# ---- og-image (1200x630) ----
base_path = "assets/abertura.webp"
hero = Image.open(base_path).convert("RGB")
tw, th = 1200, 630
sw, sh = hero.size
scale = max(tw / sw, th / sh)
nw, nh = int(sw * scale) + 1, int(sh * scale) + 1
hero_r = hero.resize((nw, nh), Image.LANCZOS)
left = (nw - tw) // 2
top = (nh - th) // 2
og = hero_r.crop((left, top, left + tw, top + th)).convert("RGBA")

# card with paw + name
try:
    font = ImageFont.truetype("C:/Windows/Fonts/georgia.ttf", 54)
except Exception:
    font = ImageFont.load_default()

paw = draw_paw(70)
name = "Pet Vida"
dummy = Image.new("RGBA", (10, 10))
dd = ImageDraw.Draw(dummy)
bbox = dd.textbbox((0, 0), name, font=font)
text_w = bbox[2] - bbox[0]
text_h = bbox[3] - bbox[1]

pad = 24
gap = 18
card_w = pad * 2 + paw.width + gap + text_w + 10
card_h = pad * 2 + max(paw.height, text_h + 10)
card = Image.new("RGBA", (card_w, card_h), (250, 243, 230, 235))
mask = Image.new("L", (card_w, card_h), 0)
ImageDraw.Draw(mask).rounded_rectangle([0, 0, card_w, card_h], radius=20, fill=255)
card.putalpha(mask)

card.alpha_composite(paw, (pad, (card_h - paw.height) // 2))
cd = ImageDraw.Draw(card)
cd.text((pad + paw.width + gap, (card_h - text_h) // 2 - bbox[1]), name, font=font, fill=INK)

margin = 40
og.alpha_composite(card, (margin, th - card_h - margin))
og.convert("RGB").save("assets/og-image.jpg", quality=88)

print("Pet Vida brand assets generated.")
