import os
import shutil

# 기본 경로 설정
base_folder = 'D:\\all_dataset'
labels_folder = os.path.join(base_folder, 'labels')
img_folder = os.path.join(base_folder, 'img')

# 폴더가 없으면 생성
os.makedirs(labels_folder, exist_ok=True)
os.makedirs(img_folder, exist_ok=True)

# 하위 폴더를 포함한 모든 파일 탐색
for root, dirs, files in os.walk(base_folder):
    for file_name in files:
        # 파일 경로 설정
        file_path = os.path.join(root, file_name)
        
        # .txt 파일 이동
        if file_name.endswith('.txt'):
            shutil.move(file_path, os.path.join(labels_folder, file_name))
            print(f"Moved {file_name} to {labels_folder}")
        
        # .jpg, .jpeg, .png 파일 이동
        elif file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
            shutil.move(file_path, os.path.join(img_folder, file_name))
            print(f"Moved {file_name} to {img_folder}")
