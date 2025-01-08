from PIL import Image
import os

def check_image_validity(directory):
    invalid_images = []
    
    # Duyệt qua các tệp trong thư mục
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Kiểm tra xem tệp có phải là ảnh không
        try:
            with Image.open(file_path) as img:
                img.verify()  # Kiểm tra ảnh hợp lệ
        except (IOError, SyntaxError) as e:
            invalid_images.append(file_path)  # Thêm ảnh không hợp lệ vào danh sách
    
    return invalid_images

# Kiểm tra ảnh trong hai thư mục
blur_invalid = check_image_validity('./train/blur')
sharp_invalid = check_image_validity('./train/sharp')

# In kết quả
if blur_invalid:
    print("Ảnh không hợp lệ trong thư mục ./train/blur:")
    for img in blur_invalid:
        print(img)

if sharp_invalid:
    print("Ảnh không hợp lệ trong thư mục ./train/sharp:")
    for img in sharp_invalid:
        print(img)

if not blur_invalid and not sharp_invalid:
    print("Tất cả ảnh đều hợp lệ.")
