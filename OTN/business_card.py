from PIL import Image, ImageDraw, ImageFont
import qrcode

# Step 1: Define business card details
name = "Jeffery Onome Emuodafevware"
title = "Full Stack Software Engineer & Web Developer"
tagline = "Where Optimism Meets Innovative Technology"
phone = "+234 8052587419"
email = "jeffemuodafe124@@gmail.com"
portfolio = "https://goldenjeffempire.github.io/Portfolio/"
linkedin = "linkedin.com/in/jeffery-emuodafevware"
qr_link = "https://goldenjeffempire.github.io/Portfolio/"

# Step 2: Generate QR Code
qr = qrcode.QRCode(box_size=10, border=2)
qr.add_data(qr_link)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white")

# Step 3: Define card dimensions and colors
card_width, card_height = 1000, 600
background_color = "#1A1A2E"  # Dark blue
text_color = "#FFFFFF"  # White
accent_color = "#4CAF50"  # Green accent

# Step 4: Create the business card canvas
card = Image.new("RGB", (card_width, card_height), color=background_color)
draw = ImageDraw.Draw(card)

# Step 5: Load fonts
try:
    font_bold = ImageFont.truetype("arialbd.ttf", 36)  # Bold font for name
    font_regular = ImageFont.truetype("arial.ttf", 24)  # Regular font for details
    font_small = ImageFont.truetype("arial.ttf", 20)  # Small font for tagline
except:
    raise Exception("Please install 'arial.ttf' and 'arialbd.ttf' fonts.")

# Step 6: Add text and design
# Add Name
draw.text((50, 50), name, font=font_bold, fill=text_color)

# Add Title
draw.text((50, 110), title, font=font_regular, fill=text_color)

# Add Tagline
draw.text((50, 160), tagline, font=font_small, fill=accent_color)

# Add Contact Information
contact_info = f"Phone: {phone}\nEmail: {email}\nPortfolio: {portfolio}\nLinkedIn: {linkedin}"
draw.text((50, 220), contact_info, font=font_regular, fill=text_color)

# Step 7: Add QR code to the back of the card
qr_img = qr_img.resize((150, 150))
card.paste(qr_img, (800, 400))

# Step 8: Add a tech-inspired background (optional)
for i in range(20):
    x_start, y_start = (i * 50, 0)
    x_end, y_end = (card_width, i * 30)
    draw.line((x_start, y_start, x_end, y_end), fill="#303040", width=1)
    draw.rectangle((10, 10, card_width - 10, card_height - 10), outline=accent_color, width=5)

# Step 9: Add logo
# Draw a simple logo as a circle with the initials "JN"
logo_size = 100
logo_x, logo_y = 800, 50
draw.ellipse((logo_x, logo_y, logo_x + logo_size, logo_y + logo_size), fill=accent_color)
draw.text((logo_x + 25, logo_y + 25), "JN", font=font_bold, fill=background_color)

# Step 10: Save the business card
card.save("business_card.png")
print("Business card created and saved as 'business_card.png'!")
