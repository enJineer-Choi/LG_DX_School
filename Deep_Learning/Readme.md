# 🧠 Deep Learning 학습 정리

> 딥러닝 기초 개념부터 CNN, RNN, LLM/RAG까지 단계별 학습 내용 정리

---

## 1. 딥러닝 기초

- 머신러닝 복습 (지도 / 비지도 / 강화학습, 평가지표)
- 선형 회귀, 로지스틱 회귀 개념
- 경사하강법(Gradient Descent), 오차 역전파(Back Propagation)
- 퍼셉트론 구조 및 딥러닝 vs 머신러닝 차이점
- 활성화 함수(Activation Function)의 역할 — 비선형성 부여

---

## 2. MLP 모델 설계 (회귀 / 분류)

- **회귀** : 학생 성적 데이터로 최종 성적 예측
- **이진 분류** : 유방암 환자 데이터로 암 여부 분류
- **다중 분류** : MNIST 손글씨 데이터로 숫자 분류
- 활성화 함수 + 최적화 함수 조합별 성능 비교
  - Sigmoid + SGD / ReLU + SGD / ReLU + Adam

---

## 3. 특수 목적 신경망

- **CNN (합성곱 신경망)** : 이미지 분류 (개/고양이 데이터), MLP와 성능 비교
- **RNN (순환 신경망)** : 시퀀스 데이터 처리, 다음 문자 예측 실습

---

## 4. LLM / RAG (LangChain)

- LLM의 한계 및 LangChain 라이브러리 개요
- LangChain 주요 구성 요소 : Data Sources, Embeddings, Vector DB
- OpenAI API 연동 실습
- **RAG (Retrieval-Augmented Generation)** 구조 및 프로세스
  - 문서 로드 → 텍스트 분할 → 임베딩 → 검색 → 생성
  - PDF 문서 기반 나만의 챗봇 구현 실습
