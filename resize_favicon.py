from PIL import Image
import os

def resize_and_save_favicon():
    # 检查原始图片是否存在
    head_png_path = 'images/head.png'
    if not os.path.exists(head_png_path):
        print(f"错误：找不到 {head_png_path} 文件")
        return
    
    # 打开原始图片
    original = Image.open(head_png_path)
    print(f"原始图片尺寸: {original.size}")
    
    # 确保images目录存在
    images_dir = 'images'
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)
    
    # 定义需要生成的尺寸和对应的文件名
    sizes = [
        (192, 192, 'android-chrome-192x192.png'),
        (512, 512, 'android-chrome-512x512.png'),
        (32, 32, 'favicon-32x32.png'),
        (16, 16, 'favicon-16x16.png'),
        (180, 180, 'apple-touch-icon.png')  # 也更新苹果设备的图标
    ]
    
    # 调整尺寸并保存
    for width, height, filename in sizes:
        # 使用高质量的重采样算法
        resized = original.resize((width, height), Image.Resampling.LANCZOS)
        
        # 保存到images目录
        output_path = os.path.join(images_dir, filename)
        resized.save(output_path, 'PNG', optimize=True)
        print(f"已生成: {output_path} ({width}x{height})")
    
    # 生成favicon.ico文件（包含多个尺寸）
    ico_sizes = [(16, 16), (32, 32), (48, 48)]
    ico_images = []
    for width, height in ico_sizes:
        resized = original.resize((width, height), Image.Resampling.LANCZOS)
        ico_images.append(resized)
    
    # 保存为ico文件
    ico_path = os.path.join(images_dir, 'favicon.ico')
    ico_images[0].save(ico_path, format='ICO', sizes=[(img.width, img.height) for img in ico_images])
    print(f"已生成: {ico_path} (多尺寸ICO文件)")
    
    print("\n所有favicon文件已成功更新！")

if __name__ == "__main__":
    resize_and_save_favicon() 