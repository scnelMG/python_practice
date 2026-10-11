<h1 align="center">Python Practice Archive</h1>

<p align="center">Python 기초부터 데이터 분석·머신러닝·이스포츠 분석 프로젝트까지 이어지는 학습 기록</p>

<p align="center">Python · Jupyter Notebook · pandas · NumPy · Matplotlib · scikit-learn</p>

> 수업 실습, 라이브러리 실험, 과제, 개인 미니 프로젝트를 보존한 저장소입니다. 완성형 제품이 아닌 학습 과정과 문제 해결의 흔적을 확인하는 용도입니다.

---

## 학습 범위

| 영역 | 내용 |
| --- | --- |
| Python 기초 | 문법, 함수, 파일 입출력, 객체지향, 과제 풀이 |
| 라이브러리 | NumPy, pandas, SciPy, Matplotlib, OpenCV, Tkinter 실습 |
| 데이터 분석 | 전처리, 시각화, 시계열, 회귀, 분류, 텍스트 분석 |
| 머신러닝 | Iris 분류, 의사결정나무, LSTM·ARIMA 실험 |
| 프로젝트 | OP.GG/League of Legends 데이터 수집·분석 실습 |

## 폴더 안내

```text
Colab Notebooks/       # 데이터 분석 수업 실습과 과제
Library_practice/      # Python 라이브러리별 실험
project/e_sports_data/ # OP.GG 기반 이스포츠 분석 프로젝트
homework_help/         # 과제 풀이와 보조 코드
make alone/            # 개인 실습
PythonWorkspace/       # 기초 문법·알고리즘 연습
WebCrawling/           # 웹 크롤링 실습
```

## 대표 산출물

- `Python_quiz/01. 파이썬 시작하기 (001 ~ 010).ipynb`: Python 기초 문법 문제 풀이
- `Library_practice/Pandas/Pandas_practice_01.ipynb`: pandas 기반 데이터 처리 실습
- `Colab Notebooks/IDS/`: 데이터 분석 수업 주차별 과제
- `project/e_sports_data/`: 경기 데이터 수집, 전처리, 시각화, 모델링 실습

## 실행 방법

각 노트북은 Jupyter 또는 Google Colab에서 실행합니다.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install jupyter pandas numpy matplotlib scikit-learn
jupyter notebook
```

외부 API·크롤링·대용량 데이터가 필요한 일부 실습은 당시의 로컬 환경 또는 별도 키가 필요할 수 있습니다.

### Riot API 실습

이스포츠 노트북은 `RIOT_API_KEY` 환경변수를 읽습니다. Jupyter를 시작할 터미널에서 본인의 유효한 키를 설정하세요. 키를 코드·출력·커밋에 넣지 마세요. 환경변수가 없으면 API 요청 전에 실행이 중단됩니다.

```powershell
$env:RIOT_API_KEY = Read-Host 'Riot API key' -MaskInput
jupyter notebook
```

위 입력 명령은 PowerShell 7.1 이상 기준입니다. Colab에서는 비밀 저장소에 `RIOT_API_KEY`를 등록한 뒤 아래 셀을 먼저 실행합니다.

```python
import os
from google.colab import userdata
os.environ['RIOT_API_KEY'] = userdata.get('RIOT_API_KEY')
```

`python scripts/check_riot_keys.py`는 현재 추적 파일의 Riot 키 문자열을 검사하며 CI에서도 실행합니다. Git 오류를 정상 결과로 처리하지 않습니다. 과거 커밋·포크·외부 사본의 삭제나 노출된 키의 폐기를 대신하는 검사는 아닙니다. 과거에 커밋한 키는 재사용하지 말고 Riot 개발자 포털에서 폐기·재발급 여부를 확인하세요.

## 보존 정책

- 수업 원본·중간 실험·checkpoint 파일을 학습 이력으로 보존합니다.
- 다른 저장소에서 포트폴리오로 정리된 이스포츠 프로젝트와 일부 내용이 겹칠 수 있습니다.
- 공개 권한이 불명확한 원본 데이터와 개인 키는 README의 재현 범위에 포함하지 않습니다.

## 이용 안내

이 저장소는 포트폴리오·학습 기록 열람을 위해 공개합니다. 코드·문서·이미지의 재사용, 수정, 배포는 사전 문의가 필요합니다.
