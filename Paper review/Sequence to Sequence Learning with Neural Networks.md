# Sequence to Sequence Learning with Neural Network
- LSTM 활용한 seq2seq 기계 번역 architecture
- Transformer 이전까지 SOTA로 사용
- seq => Encoder => context vector(fixed size) => Decoder => seq

### Language Model
- seq에 확률을 부여하는 model
- 다음에 나타날 문장이나 단어를 예측
- Statistical Language Model
  - 카운트 기반, 방대한 데이터 필요
  - N-gram 사용

### Seq2Seq
- Encoder가 고정된 크기의 context vector를 추출
- context vector로부터 Decoder가 결과 추론
- LSTM을 이용하여 성능향상
  - long-term dependency를 처리하기에 적합
  - Encoder의 마지막 hidden state만 context vector로 사용
  - 논문의 model은 4-layer LSTM 사용
- Encoder, Decoder의 가중치가 다르다
- 입력 문장의 순서를 거꾸로 했을 때 더 높은 정확도를 보임
- beam search decoder

### Referrence
[[딥러닝 기계 번역] Seq2Seq: Sequence to Sequence Learning with Neural Networks (꼼꼼한 딥러닝 논문 리뷰와 코드 실습)](https://www.youtube.com/watch?v=5n3uSXM2kU4)
