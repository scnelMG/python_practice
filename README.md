<h1 align="center">Python Practice Archive</h1>

<p align="center">Python 기초부터 데이터 분석·머신러닝·이스포츠 분석 프로젝트까지 이어지는 학습 기록</p>

<p align="center">Python · Jupyter Notebook · pandas · NumPy · Matplotlib · scikit-learn</p>

> 수업 실습, 라이브러리 실험, 과제, 개인 미니 프로젝트를 보존한 저장소입니다. 완성형 제품이 아닌 학습 과정과 문제 해결의 흔적을 확인하는 용도입니다.

---

## 목차

- [학습 범위](#학습-범위)
- [폴더 안내](#폴더-안내)
- [대표 산출물](#대표-산출물)
- [실행 방법](#실행-방법)
- [보존 정책](#보존-정책)

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

- `01. 기본 환경 구성.ipynb`: Python·Jupyter 실행 환경 학습
- `02. 붓꽃의 품종 분류.ipynb`: Iris 데이터셋 기반 분류 실습
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

## 보존 정책

- 수업 원본·중간 실험·checkpoint 파일을 학습 이력으로 보존합니다.
- 다른 저장소에서 포트폴리오로 정리된 이스포츠 프로젝트와 일부 내용이 겹칠 수 있습니다.
- 공개 권한이 불명확한 원본 데이터와 개인 키는 README의 재현 범위에 포함하지 않습니다.
