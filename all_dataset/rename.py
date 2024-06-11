import os
import re

# 특정 폴더 경로와 파일 이름에 포함될 부분 설정
folder_path = 'D:/all_dataset/labels'
specific_file_name_part = 'MJY'

# 지정된 폴더에 있는 모든 파일 확인
for file_name in os.listdir(folder_path):
    # .txt 파일만 선택
    if file_name.endswith('.txt') and specific_file_name_part in file_name:
        # 파일 경로 설정
        file_path = os.path.join(folder_path, file_name)
        
        # 파일 열기
        with open(file_path, 'r') as file:
            content = file.read()
        
        # 첫 번째 숫자 찾기
        first_number = re.search(r'\d+', content)
        
        if first_number:
            # 첫 번째 숫자의 시작과 끝 위치
            start, end = first_number.span()
            # 새 숫자로 변경 (예: 0번째 인덱스 숫자를 99로 변경)
            new_content = content[:start] + '21' + content[end:]
            
            # 파일에 새 내용 쓰기
            with open(file_path, 'w') as file:
                file.write(new_content)
                
            print(f"Updated first number in file: {file_name}")
        else:
            print(f"No numbers found in file: {file_name}")
