"""
Section 3
Concurrency, CPU Bound vs I/O Bound - I/O Bound(2) - threading vs asyncio vs multiprocessing
Keyword - I/O Bound, asyncio

"""

import multiprocessing
import requests
import time
import asyncio
import aiohttp

# 각 프로세스 메모리 영역에 생성되는 객체(독립적)
# 함수 실행 할 때 마다 객체 생성은 좋지 않음. - > 각프로세스마다 할당

# I/O Bound Asyncio 예제
# Threading 보다 높은 코드 복잡도 -> Async, Await 적절하게 코딩

session = None

def set_global_session():
    global session
    if not session:
        session = requests.Session()

# 실행 함수 1번 (다운로드)
async def request_site(session, url):

    # 세션 확인
    print(session)
    
    async with session.get(url) as response:
        print(f'Read Contents {0}, from {1}'.format(response.content_length, url))


# 실행 함수 2번 요청
async def request_all_site(urls):
    
    async with aiohttp.ClientSession() as session:
        # 작업목록
        tasks = []
        for url in urls:
            # 태스크 목록 생성
            task = asyncio.ensure_future(request_site(session, url))
            tasks.append(task)

        # 태스크 확인
        # print(*tasks)
        # print(tasks)

        await asyncio.gather(*tasks, return_exceptions=True)

def main():
    # 테스트 URLS
    urls = [
        "https://www.jypthon.org",
        "https://olympus.realpython.org/dice",
        "https://realpython.com"
    ] * 3

    # 실행 시간 측정
    start_time = time.time()

    # Async 실행
    # Python 3.7 이상
    asyncio.run(request_all_site(urls))
    # asyncio.get_event_loop().run_until_complete(request_all_site(urls)) 파이썬 3.5 이하

    # 실행 시간 종료
    duration = time.time() - start_time

    # 결과 출력
    print(f'Downloaded {len(urls)} sites in {duration} seconds')

if __name__ == "__main__":
    main()