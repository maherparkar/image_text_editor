from PIL import Image, ImageDraw, ImageFont
import pytesseract

# ✅ Use the exact filename of your image
image_path = ""
img = Image.open(image_path).convert("RGB")
draw = ImageDraw.Draw(img)

# ✅ Old text and replacement
old_text = ""
new_text = "" 

# ✅ Tesseract OCR
data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)

for i in range(len(data["text"])):
    words = data["text"][i:i+8]
    phrase = " ".join(w for w in words if w.strip())

    if phrase.lower() == old_text.lower():
        x = data["left"][i]
        y = data["top"][i]
        w = sum(data["width"][i:i+8])
        h = max(data["height"][i:i+8])

        # Cover old text with a blank rectangle
        bg_color = img.getpixel((x + 2, y + 2))  # Get nearby background color
        draw.rectangle([x, y, x + w, y + h], fill=bg_color)

        # ✅ Font path (pick any valid .ttf from Fonts/Supplemental)
        font_path = "/System/Library/Fonts/Supplemental/Arial.ttf"
        font = ImageFont.truetype(font_path, size=h - 4)

        # ✅ Draw new text
        draw.text((x, y), new_text, font=font, fill=(255, 255, 255))
        break

# ✅ Save or show result
img.save("edited_output.jpeg")
img.show()
