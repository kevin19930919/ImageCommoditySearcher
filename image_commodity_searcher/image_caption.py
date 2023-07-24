import torch
from transformers import BlipProcessor, BlipForConditionalGeneration

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


class ImageCaptionHandler:
    def __init__(self):
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    
    def generate_caption(self, image):
        inputs = self.processor(images=image, return_tensors="pt").to(DEVICE)
        pixel_values = inputs.pixel_values

        generated_ids = self.model.generate(pixel_values=pixel_values, max_length=50)
        generated_caption = self.processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return generated_caption