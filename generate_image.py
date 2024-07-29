# Set the Hugging Face endpoint to a mirror URL  
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"  
  
from diffusers import DiffusionPipeline  
import torch  
from PIL import Image  
import time  
  
# Load the model to GPU if available  
pipeline = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)  
pipeline.to("cuda")  
  
def main_function():  
    print("Please input what kind of photo you want to generate: (start with a description, e.g., 'A photo of...')")  
    # Generate an image  
    prompt = input()  
    with torch.no_grad():  # Ensure no gradients are computed to save computational resources  
        start_time = time.time()  
        images = pipeline(prompt, num_inference_steps=50, guidance_scale=7.5).images  # Adjust parameters for optimal results  
        end_time = time.time()  
        print(f"It took {end_time - start_time} seconds to generate the photo: {prompt}")  
      
    # Select the first image (index 0)  
    image = images[0]  
    file_path = 'C://Users//30651//Desktop//github//diffusion_model//generate_picture_collection'  # Note: This is a network path or a UNC path with double slashes  
    file_name = f"{prompt.replace(' ', '_')}.png"  # Replace spaces in the prompt for a valid filename  
    full_path = file_path + '/' + file_name  # Use '/' as the path separator for compatibility  
      
    # Save the PIL image to a local file  
    image.save(full_path)  # You can change the filename and extension (e.g., .jpg)  
  
def main():  
    flag = '1'  
    while flag == '1':  
        main_function()  
        print("Continue or quit?")  
        print("If continue, input 1. If quit, input 2.")  
        flag = input()  
  
main()
