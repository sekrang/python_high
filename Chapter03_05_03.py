"""
Section 3
Concurrency, CPU Bound vs I/O Bound - I/O Bound(2) - asyncio basic
Keyword - asyncio

"""
"""
동시 프로그래밍 패러다임 변화
싱글 코어 -> 처리향상 미미, 저하 -> 비동기 프로그래밍 -> CPU연산, DB연동, API 호출 대기시간 늘어남
파이썬 3.4 -> 비동기(asyncio) 표준라이브러리 등장 
"""

import time
import asyncio

async def exe_calculate_async(name, n):
    for i in range(1, n + 1):
        print(f'{name} -> {i} of {n} is calculating...')
        asyncio.sleep(1)
    print(f'{name} - {n} working done!')

async def process_async():
    start = time.time()

    await asyncio.wait([
        exe_calculate_async('One', 3),
        exe_calculate_async('Two', 2),
        exe_calculate_async('Three', 1),
    ])

    end = time.time()
    
    print(f'>>> total seconds :  {end - start}')

def exe_calculate_sync(name, n):
    for i in range(1, n + 1):
        print(f'{name} -> {i} of {n} is calculating...')
        time.sleep(1)
    print(f'{name} - {n} working done!')

def process_sync():
    start = time.time()

    exe_calculate_sync('One', 3)
    exe_calculate_sync('Two', 2)
    exe_calculate_sync('Three', 1)

    end = time.time()
    
    print(f'>>> total seconds :  {end - start}')

if __name__ == '__main__':
    #Sync 실행
    # process_sync()

    # Async 실행
    # Python 3.7 이상
    asyncio.run(process_async())
    # asyncio.get_event_loop().run_until_complete(process_async()) 파이썬 3.5 이하