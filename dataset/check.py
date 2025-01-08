import os
import pandas as pd
# Đọc nội dung từ file plates_info.txt và trích xuất các tên file
plates_info_file = 'plate_info.txt'
image_names = set()

df = pd.read_csv(plates_info_file, header=None,
                             names=['ImageName', 'PlateInfo'])

# Đọc file plates_info.txt
image_names = set(df['ImageName'])

# Lấy danh sách tất cả các file .jpg trong thư mục ./train/blur
blur_folder = './train/blur'
all_images_in_blur = set(f for f in os.listdir(blur_folder) if f.endswith('.jpg'))

# Kiểm tra các file không có trong danh sách plates_info.txt
missing_images = all_images_in_blur - image_names

print(len(missing_images))

# In ra các file không có trong plates_info.txt
if missing_images:
    print("Các file không có trong plates_info.txt:")
    for img in missing_images:
        print(img)
else:
    print("Tất cả các file .jpg trong thư mục ./train/blur đều có tên trong plates_info.txt.")
