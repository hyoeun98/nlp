# Language Model
- 단어 시퀀스에 확률을 할당
- 주어진 단어들로부터 다음 단어를 예측

### 통계적 언어 모델(Statistical Language Model)
- 카운트 기반의 접근
  - 방대한 양의 corpus 필요
  - 데이터의 양이 부족하면 희소 문제(sparsity problem) 발생

### N-gram Language Model
- SLM의 일종
- N개의 단어를 하나의 토큰으로 간주
  - 여전히 희소 문제가 존재
  - 전체 문장을 고려한 모델보다 정확도가 떨어짐
  - n 선택의 어려움

- 적용 분야에 맞는 코퍼스를 수집해야 함
- 선천적인 문제점으로 인해 인공 신경망을 사용한 언어 모델이 대세

### Korean Language Model
- 어순이 중요하지 않음
- 토큰화를 통해 단어를 분리해야 함
- 띄어쓰기가 지켜지지 않음

### Perplexity(PPL) #perplexed 헷갈리는
- 모델 내에서 성능을 수치화하는 내부 평가(Intrinsic evaluation)
- 선택 가능한 경우의 수를 의미하는 분기계수(branching factor)
