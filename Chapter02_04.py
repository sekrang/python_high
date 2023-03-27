"""
Section 2
Parallelism with Multiprocessing - multiprocessing(3) - ProcessPoolExecutor
Keyword - ProcessPoolExecutor, as_completed, futures, timeout, dict

"""
from concurrent.futures import ProcessPoolExecutor, as_completed
from operator import le
import urllib.requestw

# 조회 URLS
URLS = [
    'https://www.daum.net',
    'https://www.cnn.com/',
    'https://www.naver.com',
    'https://www.youtube.com',
    'https://www.twitch.com'
]

# 실행 함수
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

def main():
    # 프로세스풀 Context 영역
    with ProcessPoolExecutor(max_workers=5) as executor:
        # Future 로드(실행X)
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}

        # 중간 확인
        # print(future_to_url)

        # 실행
        for future in as_completed(future_to_url): #timeout = 1
            # Key값이 Future 객체
            url = future_to_url[future]

            try:
                #결과
                data = future.result()
            except Exception as exc:
                # 예외 처리
                print('%r generated an exception: %s' % (url, exc))
            else:
                # 결과 확인
                print('%r page is %d bytes' % (url, len(data)))
if __name__ == ' __main__':
    main()