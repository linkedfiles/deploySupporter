import paramiko

def read_lines_to_list(file_path):
    lines_list = []
    try:
        with open(file_path, 'r') as file:
            lines_list = file.readlines()
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {file_path}")
    except Exception as e:
        print(f"파일 읽기 오류: {e}")
    return lines_list

# 텍스트 파일 경로 설정
file_path = "test.txt"

# 파일의 각 줄을 리스트로 읽어옴
lines_list = read_lines_to_list(file_path)

# 내 워크 스페이스 경로 잡아주기
my_work_space = ""

# 정리된 리스트를 리스트에 담기

# sfpt 테스트

# 다운로드 받을 경로 잡아주기

# 서버에 있는 파일을 로컬로 백업 (true, false)
    # 파일 디렉토리 생성
    # 파일 다운로드

# 파일 Override 시킴

# 끝

print(lines_list)
