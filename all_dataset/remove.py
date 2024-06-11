import os

# 폴더 경로 설정
img_folder = 'D:\\all_dataset\\img'
labels_folder = 'D:\\all_dataset\\labels'

# img 폴더의 모든 이미지 파일 이름 (확장자 제외)
img_files = {os.path.splitext(file_name)[0] for file_name in os.listdir(img_folder) 
             if file_name.lower().endswith(('.jpg', '.jpeg', '.png'))}

# labels 폴더의 모든 텍스트 파일 이름 (확장자 제외)
txt_files = {os.path.splitext(file_name)[0] for file_name in os.listdir(labels_folder) 
             if file_name.endswith('.txt')}

# 이미지 파일 중 대응하는 텍스트 파일이 없는 경우 삭제
for file_name in os.listdir(img_folder):
    if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
        file_base_name = os.path.splitext(file_name)[0]
        if file_base_name not in txt_files:
            file_path = os.path.join(img_folder, file_name)
            os.remove(file_path)
            print(f"Deleted image file: {file_path}")

# 텍스트 파일 중 대응하는 이미지 파일이 없는 경우 삭제
for file_name in os.listdir(labels_folder):
    if file_name.endswith('.txt'):
        file_base_name = os.path.splitext(file_name)[0]
        if file_base_name not in img_files:
            file_path = os.path.join(labels_folder, file_name)
            os.remove(file_path)
            print(f"Deleted text file: {file_path}")
