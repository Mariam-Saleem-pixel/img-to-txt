from PIL import Image, ImageDraw, ImageFont

def text_to_image(text, font_size=40, image_width=400, image_height=200, text_color="black", background_color="white"):
    # Create a blank image with the specified background color
    img = Image.new('RGB', (image_width, image_height), color=background_color)
    
    # Initialize the drawing context
    draw = ImageDraw.Draw(img)
    
    # Load a font
    try:
        # Attempt to use a TrueType font
        font = ImageFont.truetype("arial.ttf", font_size)  # Adjust the font path if necessary
    except IOError:
        # Use a default font if the specified font is not found
        font = ImageFont.load_default()

    # Calculate the size and position of the text
    text_bbox = draw.textbbox((0, 0), text, font=font)  # Get bounding box for the text
    text_width = text_bbox[2] - text_bbox[0]  # Width = right - left
    text_height = text_bbox[3] - text_bbox[1]  # Height = bottom - top
    position = ((image_width - text_width) // 2, (image_height - text_height) // 2)

    # Add the text to the image
    draw.text(position, text, fill=text_color, font=font)
    
    # Save the image
    img.save("text_image.png")
    print("Image saved as 'text_image.png'")

# Example usage
text = "Hello, World!"
text_to_image(text)
