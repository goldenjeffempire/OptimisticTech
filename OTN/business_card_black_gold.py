from PIL import Image, ImageDraw, ImageFont
import qrcode

# Create the image canvas (business card size: 3.5" x 2")
card_width = 1050  # 3.5 inches at 300 DPI
card_height = 600  # 2 inches at 300 DPI
card = Image.new("RGB", (card_width, card_height), "#000000")  # Black background

draw = ImageDraw.Draw(card)

# Load font (adjust path if necessary)
font_bold = ImageFont.truetype("arial.ttf", 60)  # Use bold font for the name
font_regular = ImageFont.truetype("arial.ttf", 40)  # Regular font for the title and details
font_tagline = ImageFont.truetype("arial.ttf", 30)  # Smaller font for the tagline

# Define colors
gold = "#FFD700"
dark_gold = "#B8860B"
white = "#FFFFFF"

# Draw Name (bold and large)
name_text = "Jeffery Onome Emuodafevware"
draw.text((50, 100), name_text, font=font_bold, fill=gold)

# Draw Title (below the name)
title_text = "Full Stack Software Engineer & Web Developer"
draw.text((50, 200), title_text, font=font_regular, fill=white)

# Draw Tagline (below the title)
tagline_text = '"Where Optimism Meets Innovative Technology"'
draw.text((50, 300), tagline_text, font=font_tagline, fill=gold)

# Contact Info
contact_y_position = 370  # Starting Y position for contact info
contact_info = [
    ("Phone: +234 8052587419", white),
    ("Email: your-email@example.com", white),
    ("Portfolio: www.yourwebsite.com", white),
    ("LinkedIn: linkedin.com/in/jeffery", white)
]

# Draw the contact info on the card
for contact in contact_info:
    draw.text((50, contact_y_position), contact[0], font=font_regular, fill=contact[1])
    contact_y_position += 40  # Increase Y position for the next contact info

# Add QR code (Generate it)
qr_link = "https://www.linkedin.com/in/jeffery"  # Replace with your actual URL
qr = qrcode.make(qr_link)
qr = qr.resize((150, 150))  # Resize the QR code to fit on the business card

# Paste the QR code on the card (bottom-right corner)
card.paste(qr, (card_width - 160, card_height - 160))

# Save the business card image
card.save("business_card_black_gold.png")

print("Business card created and saved as 'business_card_black_gold.png'")
