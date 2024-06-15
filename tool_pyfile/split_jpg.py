from PIL import Image

def split_image(image_path, output_path1, output_path2):
    try:
        # 打开图像文件
        img = Image.open(image_path)
        
        # 获取图像尺寸
        width, height = img.size
        
        # 计算切割后每个部分的尺寸
        left_box = (0, 0, width//2, height)
        right_box = (width//2, 0, width, height)
        
        # 切割图像并保存
        left_img = img.crop(left_box)
        right_img = img.crop(right_box)
        
        left_img.save(output_path1)
        right_img.save(output_path2)
        
        print(f"图像成功切割并保存为 {output_path1} 和 {output_path2}")
    
    except Exception as e:
        print(f"出现错误：{e}")

# 调用函数进行切割示例
if __name__ == "__main__":
    image_path = "Assets\img\conan_full_door.jpg"  # 输入你的图片路径
    output_path1 = "Assets\img\conan_left_door.jpg"
    output_path2 = "Assets\img\conan_right_door.jpg"
    
    split_image(image_path, output_path1, output_path2)
