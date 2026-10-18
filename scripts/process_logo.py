from PIL import Image

def crop_with_padding(path, pad_frac=0.06):
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

# Icon (dog+cat on pink cross) for favicon + header mark
icon = crop_with_padding("assets/source/logo-icone.png", pad_frac=0.04)
# Make square canvas (center on largest side) for favicon use
side = max(icon.size)
square = Image.new("RGBA", (side, side), (0, 0, 0, 0))
square.paste(icon, ((side - icon.width) // 2, (side - icon.height) // 2), icon)

for s in [16, 32, 48, 180, 192, 512]:
    square.resize((s, s), Image.LANCZOS).save(f"assets/favicon-{s}.png")

ico_sizes = [16, 32, 48]
ico_imgs = [square.resize((s, s), Image.LANCZOS) for s in ico_sizes]
ico_imgs[0].save("assets/favicon.ico", sizes=[(s, s) for s in ico_sizes])

# Header mark: icon only, transparent, modest size for crisp small display
icon_header = icon.copy()
icon_header.thumbnail((160, 160), Image.LANCZOS)
icon_header.save("assets/logo-icon.png")

# Full lockup (icon + wordmark) for footer
full = crop_with_padding("assets/source/logo.png", pad_frac=0.03)
full_w = 420
full_h = int(full.height * (full_w / full.width))
full = full.resize((full_w, full_h), Image.LANCZOS)
full.save("assets/logo-full.png")

print("icon header size", icon_header.size)
print("full logo size", full.size)
