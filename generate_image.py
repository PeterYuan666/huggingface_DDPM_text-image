import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
from diffusers import DiffusionPipeline
import torch
from PIL import Image
import time
# 加载模型到GPU（如果有的话）
pipeline = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
pipeline.to("cuda")
def maintype():
   print("please input what kind of photo you want to generate:(start with a photo of...)")
# 生成图像
   prompt = input()
   with torch.no_grad():  # 确保不计算梯度，节省计算资源
     time1=time.time()
     images = pipeline(prompt, num_inference_steps=50, guidance_scale=7.5).images  # 调整参数以获得最佳效果
     time2=time.time()
     print("it costs",time2-time1,"seconds to generate such kind of photo:",prompt)
# 选择第一张图像（索引为0）
   image = images[0]
   file_path = 'C://Users//30651//Desktop//github//diffusion_model//generate_picture_collection' # 注意：这是一个网络路径或双斜杠表示的UNC路径
   file_name = f"{prompt}.png"  # 使用f-string格式化文件名
   full_path = file_path + file_name  # 将路径和文件名连接起来  
   # 将PIL图像保存到本地文件
   image.save(full_path)  # 你可以更改文件名和扩展名（如.jpg）
def main():
   flag='1'
   while(flag=='1'):
        maintype()
        print("continue or quit?")
        print("if continue,input 1,if quit,input 2")
        flag=input()
main()
