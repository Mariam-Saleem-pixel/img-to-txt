from PIL import Image, ImageDraw, ImageFont

def text_to_image(text, font_size=40, image_width=400, image_height=200, text_color="black", background_color="white"):
    # Create a blank image with a white background
    img = Image.new('RGB', (image_width, image_height), color=background_color)
    
    # Initialize drawing object
    draw = ImageDraw.Draw(img)
    
    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", font_size)  # Use a TrueType font
    except IOError:
        font = ImageFont.load_default()  # Fallback to default font if 'arial.ttf' not found

    # Calculate the size and position of the text to center it
    text_width, text_height = draw.textsize(text, font=font)
    position = ((image_width - text_width) // 2, (image_height - text_height) // 2)
    
    # Add the text to the image
    draw.text(position, text, fill=text_color, font=font)
    
    # Save the image
    img.save("text_image.png")

    return img

# Example usage
text = "Hello, World!"
text_to_image(text)

# To display the image directly in a notebook, use this line
# img.show()  # Uncomment if running in a local environment
