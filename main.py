from PIL import Image
import tkinter as tk
from tkinter import filedialog

def resize_image(input_image_path, output_image_path, background_color):
    img = Image.open(input_image_path)
    img_width, img_height = img.size
    size = max(img_width, img_height)
    
    new_img = Image.new("RGB", (size, size), background_color)
    new_img.paste(img, ((size - img_width) // 2, (size - img_height) // 2))

    new_img.save(output_image_path, quality=75)

def get_color_input():
    color = input("배경색을 RGB 형식으로 입력하세요 (블랙: 0,0,0 / 화이트: 255,255,255): ")
    return tuple(map(int, color.split(',')))

def main():
    root = tk.Tk()
    root.withdraw()

    file_paths = filedialog.askopenfilenames(title='변환할 이미지 파일을 선택하세요')
    output_folder = filedialog.askdirectory(title='이미지를 저장할 폴더를 선택하세요')
    color = get_color_input()

    for file_path in root.tk.splitlist(file_paths):
        output_path = f"{output_folder}/{file_path.split('/')[-1]}"
        resize_image(file_path, output_path, color)

    print("이미지 변환 작업이 완료되었습니다.")

if __name__ == "__main__":
    main()