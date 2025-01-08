import os

# Đọc nội dung từ file plates_info.txt và trích xuất các tên file
plates_info_file = 'plates_info.txt'
image_names = set()

# Đọc file plates_info.txt
with open(plates_info_file, 'r') as file:
    for line in file:
        # Lấy phần trước dấu ',' và thêm vào danh sách
        image_name = line.split(',')[0].strip()
        image_names.add(image_name)

# Lấy danh sách tất cả các file .jpg trong thư mục ./train/blur
blur_folder = './test/blur'
all_images_in_blur = [f for f in os.listdir(blur_folder) if f.endswith('.jpg')]

# Kiểm tra và xóa các file không có trong danh sách plates_info.txt
for img in all_images_in_blur:
    if img not in image_names:
        file_path = os.path.join(blur_folder, img)
        os.remove(file_path)
        ##print(f"Đã xóa file: {img}")

print("Hoàn thành xóa các file không có trong plates_info.txt.")
