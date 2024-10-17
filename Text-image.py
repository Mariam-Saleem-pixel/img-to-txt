 from PIL import Image, ImageDraw, ImageFont

def text_to_image(text, font_size=40, image_width=400, image_height=200, text_color="black", background_color="white"):
    # Create a blank image
    img = Image.new('RGB', (image_width, image_height), color=background_color)
    draw = ImageDraw.Draw(img)
    
    # Use the default font
    font = ImageFont.load_default()

    # Calculate text size and position
    text_width, text_height = draw.textsize(text, font=font)
    position = ((image_width - text_width) // 2, (image_height - text_height) // 2)
    
    # Draw the text
    draw.text(position, text, fill=text_color, font=font)
    
    # Save the image
    img.save("text_image.png")
    print("Image saved as 'text_image.png'")

# Example usage
text = "Hello, World!"
text_to_image(text)
