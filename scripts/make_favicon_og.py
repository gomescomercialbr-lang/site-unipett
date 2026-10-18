import math
from PIL import Image, ImageDraw

BROWN = (43, 30, 24, 255)
PINK = (236, 111, 169, 255)
TEAL = (22, 175, 168, 255)
CREAM = (250, 243, 232, 255)

def draw_paw(size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx, cy = size / 2, size / 2
    r = size * 0.46
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=TEAL)

    pad_r = size * 0.195
    pad_cy = size * 0.62
    d.ellipse([cx - pad_r, pad_cy - pad_r, cx + pad_r, pad_cy + pad_r], fill=CREAM)

    toe_r = size * 0.115
    offsets = [(-0.30, -0.14), (-0.115, -0.26), (0.115, -0.26), (0.30, -0.14)]
    for ox, oy in offsets:
        tx = cx + ox * size
        ty = cy + oy * size
        d.ellipse([tx - toe_r, ty - toe_r, tx + toe_r, ty + toe_r], fill=CREAM)
    return img

for s in [16, 32, 180, 192, 512]:
    draw_paw(s).save(f"assets/favicon-{s}.png")

icon_sizes = [16, 32, 48]
imgs = [draw_paw(s) for s in icon_sizes]
imgs[0].save("assets/favicon.ico", sizes=[(s, s) for s in icon_sizes])

hero = Image.open("assets/hero.webp").convert("RGB")
target_w, target_h = 1200, 630
sw, sh = hero.size
scale = max(target_w / sw, target_h / sh)
nw, nh = int(sw * scale) + 1, int(sh * scale) + 1
hero_r = hero.resize((nw, nh), Image.LANCZOS)
left = (nw - target_w) // 2
top = (nh - target_h) // 2
og = hero_r.crop((left, top, left + target_w, top + target_h))
og.save("assets/og-image.jpg", quality=86)

print("done")
