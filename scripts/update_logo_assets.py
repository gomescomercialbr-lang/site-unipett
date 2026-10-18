from PIL import Image

def crop_with_padding(path, pad_frac=0.03):
    im = Image.open(path).convert("RGBA")
    bbox = im.getbbox()
    l, t, r, b = bbox
    w, h = r - l, b - t
    pad = int(max(w, h) * pad_frac)
    l2 = max(0, l - pad)
    t2 = max(0, t - pad)
    r2 = min(im.width, r + pad)
    b2 = min(im.height, b + pad)
    return im.crop((l2, t2, r2, b2))

# ---------- 1/2: logo.webp (header + footer), max 400px width ----------
full = crop_with_padding("assets/source/logo.png", pad_frac=0.03)
target_w = 400
target_h = int(full.height * (target_w / full.width))
logo = full.resize((target_w, target_h), Image.LANCZOS)
logo.save("assets/logo.webp", quality=92, lossless=False, method=6)
print("logo.webp", logo.size)

# ---------- 3: favicon from logo-icone.png ----------
icon = crop_with_padding("assets/source/logo-icone.png", pad_frac=0.04)
side = max(icon.size)
square = Image.new("RGBA", (side, side), (0, 0, 0, 0))
square.paste(icon, ((side - icon.width) // 2, (side - icon.height) // 2), icon)

# favicon.ico at 32x32
fav32 = square.resize((32, 32), Image.LANCZOS)
fav32.save("assets/favicon.ico", sizes=[(32, 32)])

# favicon-192.png
square.resize((192, 192), Image.LANCZOS).save("assets/favicon-192.png")

# apple-touch-icon.png 180x180 with cream background (no transparency allowed on iOS)
CREAM = (0xFA, 0xF3, 0xE6, 255)
apple_canvas = Image.new("RGBA", (side, side), CREAM)
apple_canvas.paste(icon, ((side - icon.width) // 2, (side - icon.height) // 2), icon)
apple = apple_canvas.convert("RGB").resize((180, 180), Image.LANCZOS)
apple.save("assets/apple-touch-icon.png")

print("favicon set regenerated")

# ---------- 5: og-image with logo applied over hero ----------
hero = Image.open("assets/hero.webp").convert("RGB")
target_w, target_h = 1200, 630
sw, sh = hero.size
scale = max(target_w / sw, target_h / sh)
nw, nh = int(sw * scale) + 1, int(sh * scale) + 1
hero_r = hero.resize((nw, nh), Image.LANCZOS)
left = (nw - target_w) // 2
top = (nh - target_h) // 2
og = hero_r.crop((left, top, left + target_w, top + target_h)).convert("RGBA")

# Place logo (with a soft cream card behind it for legibility) bottom-left
logo_og_w = 260
logo_og_h = int(full.height * (logo_og_w / full.width))
logo_og = full.resize((logo_og_w, logo_og_h), Image.LANCZOS)

pad = 24
card_w, card_h = logo_og_w + pad * 2, logo_og_h + pad * 2
card = Image.new("RGBA", (card_w, card_h), (0xFA, 0xF3, 0xE6, 235))
# rounded corners
from PIL import ImageDraw
mask = Image.new("L", (card_w, card_h), 0)
ImageDraw.Draw(mask).rounded_rectangle([0, 0, card_w, card_h], radius=20, fill=255)
card.putalpha(mask)

margin = 40
og.alpha_composite(card, (margin, target_h - card_h - margin))
og.alpha_composite(logo_og, (margin + pad, target_h - card_h - margin + pad))

og.convert("RGB").save("assets/og-image.jpg", quality=88)
print("og-image.jpg updated", og.size)
