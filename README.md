
# Text-to-Image Generation with Hugging Face Diffusion Models

## Introduction

This repository contains a Python script that utilizes Hugging Face's `diffusers` library to generate images from text prompts using a pre-trained diffusion model. Specifically, it employs the `runwayml/stable-diffusion-v1-5` model for generating high-quality images based on user-provided text descriptions.

## Prerequisites

- Python 3.x
- PyTorch
- Diffusers library (`pip install diffusers`)
- PIL (Pillow) for image processing (`pip install Pillow`)
- CUDA-enabled GPU (recommended for faster inference)

## Environment Setup

1. Install the required Python packages:
   ```bash
   pip install torch diffusers Pillow
   ```

2. Ensure you have a CUDA-enabled GPU and PyTorch is configured to use it.

3. Set the environment variable `HF_ENDPOINT` to a Hugging Face mirror if needed (optional):
   ```bash
   export HF_ENDPOINT="https://hf-mirror.com"  # For Unix-like systems
   set HF_ENDPOINT=https://hf-mirror.com        # For Windows
   ```

   Or, directly in your Python script:
   ```python
   import os
   os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
   ```

## Usage

1. Clone this repository or download the script.

2. Run the script `python generate_image.py` (assuming you've saved the script as `generate_image.py`).

3. Follow the prompts to input the text description of the image you want to generate.

4. The script will generate the image and save it to the specified directory (configurable in the script).

5. Optionally, you can run the script in a loop to generate multiple images by entering '1' when prompted.

## Customization

- **Model Selection**: You can change the model by modifying the `from_pretrained` method call in the script.
- **Output Directory**: Modify the `file_path` variable to save images to a different directory.
- **Image Quality**: Adjust `num_inference_steps` and `guidance_scale` parameters to improve or change the quality and style of the generated images.

## Example

```bash
please input what kind of photo you want to generate:(start with a photo of...)
A beautiful sunset over the ocean
it costs 25.3456789 seconds to generate such kind of photo: A beautiful sunset over the ocean
```

The script will save an image named `A beautiful sunset over the ocean.png` in the specified directory.

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

## Acknowledgments

- Thanks to Hugging Face for providing the `diffusers` library and pre-trained models.
- Thanks to the creators of the `runwayml/stable-diffusion-v1-5` model.
```

请确保将`generate_image.py`替换为你的实际脚本文件名，并根据需要调整其他细节。
