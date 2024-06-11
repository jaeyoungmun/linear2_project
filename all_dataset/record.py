import os

# 폴더 경로 설정
folder_path = 'D:\\all_dataset\\labels'

# 특정 문자열을 포함하는 파일 이름 설정
specific_string = 'teamA'

# 로그 파일 경로 설정
log_file_path = os.path.join(folder_path, 'first_char_log.txt')

# 하위 폴더를 포함한 모든 파일 탐색
with open(log_file_path, 'w') as log_file:
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            # teamA를 포함한 .txt 파일만 선택
            if specific_string in file_name and file_name.endswith('.txt'):
                file_path = os.path.join(root, file_name)
                
                # .txt 파일 열기
                with open(file_path, 'r') as file:
                    content = file.read()
                
                # 첫 번째 글자 기록
                if content:
                    first_char = content[0]
                    log_file.write(f"{file_name}: {first_char}\n")
                    print(f"Recorded first character of {file_name}: {first_char}")
                else:
                    log_file.write(f"{file_name}: (empty file)\n")
                    print(f"{file_name} is empty")
