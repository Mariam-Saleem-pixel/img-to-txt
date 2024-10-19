# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("image-to-text", model="microsoft/trocr-base-handwritten")

 # Load model directly
from transformers import AutoTokenizer, VisionEncoderDecoderModel 

tokenizer = AutoTokenizer.from_pretrained("microsoft/trocr-base-handwritten", clean_up_tokenization_spaces=True) # Set clean_up_tokenization_spaces to True
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")

from transformers import TrOCRProcessor, VisionEncoderDecoderModel, AutoTokenizer
from PIL import Image

# load image from the IAM database
image = Image.open(input("url")).convert("RGB") 

# Explicitly set clean_up_tokenization_spaces to False to avoid future warnings
tokenizer = AutoTokenizer.from_pretrained("microsoft/trocr-base-handwritten", clean_up_tokenization_spaces=False) 
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")

processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-handwritten')
pixel_values = processor(images=image, return_tensors="pt").pixel_values

generated_ids = model.generate(pixel_values)
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

print(generated_text) # Print the generated text
