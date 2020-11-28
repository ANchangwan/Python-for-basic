# Chapter06-3-1
# 파이선 심화
# Future 동시성
# 비동기 작업 실행
# 지연시간(Block) CPU 및 리소스 낭비 방지 -> (File)Network I/O 관련 작업 동시성 활용 권장
# 적합한 작업일 경우 순차 진행보다 압도적으로 성능 향상

# 실습 대상 3가지 경우

# 순차 실행
# concurrent.futures 방법1 map
# concurrent.futures 방법2 submit


# Google Python GIL(Global Interpreter LOCK)
# Gil은 한 번에 하나의 스레드만 수행 할 수 있게 인터프리터 자체에서 락을 거는 것. because it must safe





import os   # 경로 확인
import time # 성능측정
import sys
import csv # cs 파일을 읽기 위해서
from concurrent import futures

# concurrent.futures 방법1(ThreadPoolExecutor, ProcessPoolExecutor)
# map()
# 서로 다른 스레드 또는 프로세스에서 실행 가능
#내부 과정 알 필요 없으며, 고수준으로 인터페이스 제공

# 국가정보
NATION_LS = ('Singapore Germany Israel Norway Italy Canada France Spain Mexico').split()

# 초기 csv 위치
TARGET_CSV = 'C:/Users/multi/OneDrive/문서/Python/resources/nations.csv'

# 저장 폴더 위치
DEST_DIR = '/Advanced_Python/csvs'

# CSV 헤더 기초 정보
HEADER = ['Region','Country','Item Type','Sales Channel','Order Priority','Order Date','Order ID','Ship Date',
          'Units Sold','Unit Price','Unit Cost','Total Revenue','Total Cost','Total Profit']

#국가별 csv 파일 저장
def save_csv(data, filename):
    # 최종 경로 생성
    path = os.path.join(DEST_DIR, filename)

    with open(path, 'w',newline='') as fp:
        writer = csv.DictWriter(fp, fieldnames=HEADER)
        # Header Write
        writer.writeheader()
        # Dict to CSV Write
        for row in data:
            writer.writerow(row)




# 국가별 분리
def get_sales_data(nt):
    with open(TARGET_CSV, 'r') as f:
        reader = csv.DictReader(f)
        # Dict을 리스트로 적재
        data = []
        # Header 확인
        #print(reader.fieldnames)
        for r in reader:
            # OrderedDict 확인
            # print(r)
            # 조건에 맞는 국가만 삽입
            if r['Country'] == nt:
                data.append(r)
    return data

# 중간 상황 출력
def show(text):
    print(text, end= ' ')
    # 중간 출력(버퍼 비우기)
    sys.stdout.flush()




# 국가 별 분리 함수 실행
def separate_many(nt):
    # 분리 데이터
    data = get_sales_data(nt)
    # 상황 출력
    show(nt)
    # 파일 저장
    save_csv(data,nt.lower() + '.csv')

    return nt




# 간 측정 및 메인 함수
def main(separate_many):
    # worker 개수
    worker = min(20, len(NATION_LS))


    # 시작 시간
    start_tm = time.time()
    # futures
    futures_list = []
    # 결과 건수
    # ProcessPoolExecutor : GIL 우회, 변경 후 -> os.cpu_count()
    # ThreadPoolExecutor : GIL 종속
    with futures.ProcessPoolExecutor() as excutor:
        # Submit -> callable 객체 스케쥴링(실행 예약) -> Future
        # Future -> result(), done(), as_complete() 주로 사용

        for nt in sorted(NATION_LS):
            # future 반환
            future = excutor.submit(separate_many,nt)
            # 스케쥴링
            futures_list.append(future)
            # 출력1
            # print('Scheduled for {} : {}'.format(nt, future))
            # print()

        for future in futures.as_completed(futures_list):
            result = future.result()
            done = future.done()
            cancelled = future.cancelled()
            # future 결과 확인
            print('Future Result : {}, Done : {}'.format(result, done))
            print('Future Cancelled : {}'.format(cancelled))

    # 종료 시간
    end_tm = time.time() - start_tm


    msg = '\n csv separated in {:.2f}s'
    # 최종 결과 출력
    # print(msg.format(list(futures_list),end_tm))
    print(msg.format(end_tm))



# 실행
if __name__ == '__main__':
    main(separate_many)



