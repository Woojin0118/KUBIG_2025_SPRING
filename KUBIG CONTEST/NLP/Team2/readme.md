# **WikiRAG: 유사 문서 기반 단어 설명 생성기**

- 위키백과 기반 RAG(Retrieval-Augmented Generation) 기법을 활용해 유사 문서를 검색하고 단어 설명을 생성하는 AI 서비스.
- 영문 정보 탐색 과정에서의 피로도를 줄이고 정확한 단어 설명 제공을 목표로 함.

---

## 팀원

- 20기 이예지 21기 이영서, 이예일

---

## **개발 과정**

### **1. 데이터 전처리**

- Hugging Face의 **`lsb/simplewiki2023`** 데이터셋 사용
- 너무 긴 텍스트 필터링 (1000자 이내)

### **2. VectorDB 구축**

- **`Semantic Chunker`** 사용해 의미 기반 청킹
- **`all-MiniLM-L6-v2`** 임베딩 모델 적용
- **`ChromaDB`** 활용해 벡터 검색 수행

### **3. 유사 문서 검색**

- 1차 기준: Title이 정확히 일치하는가
- 2차 기준: Title이 유사한가
- 검색된 문서 중 3개 선택

### **4. 설명 생성**

- **`propositionizer-wiki-flan-t5-large`** 모델 사용

### **5. 서비스 구현**

- 백엔드: **`FastAPI`**
- 프론트엔드: **`Codepen`** 활용
