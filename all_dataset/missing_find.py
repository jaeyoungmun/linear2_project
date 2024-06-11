import os

# 폴더 경로 설정
labels_folder = 'D:\\all_dataset\\labels'

# 0에서 30 사이의 모든 숫자 집합
all_numbers_set = set(range(31))

# labels 폴더의 모든 .txt 파일 이름 (확장자 제외)
txt_files = [file_name for file_name in os.listdir(labels_folder) if file_name.endswith('.txt')]

# 0번째 및 1번째 인덱스의 숫자를 저장할 집합
found_numbers_set = set()

# 모든 .txt 파일 열기
for file_name in txt_files:
    file_path = os.path.join(labels_folder, file_name)
    
    # .txt 파일 열기
    with open(file_path, 'r') as file:
        content = file.read()
    
    # 두 자리 숫자 확인
    if len(content) >= 2:
        if content[:2].isdigit():
            number = int(content[:2])
            found_numbers_set.add(number)
        elif content[0].isdigit():
            number = int(content[0])
            found_numbers_set.add(number)

# 0에서 30 사이의 숫자 중 누락된 숫자 계산
missing_numbers = all_numbers_set - found_numbers_set

# 누락된 숫자 출력
print(f"Missing numbers in the range 0-30: {sorted(missing_numbers)}")
