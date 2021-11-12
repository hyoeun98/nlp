# Attention Is All You Need(2017)
- GPT : Transformer의 Decoder 활용
- BERT : Transformer의 Encoder 활용
- Attention mechanism 등장 이후부터 입력 seq전체에서 정보를 추출하는 방향으로 발전

- 기존 seq2seq모델
  - context vector(고정된 크기)에 소스 문장의 정보 압축 -> 병목현상 발생
  - with attention -> decoder가 encoder의 모든 output(hidden state) 참고 
  - Energy = decoder에서 1 step 전에 출력한 값과 encoder의 모든 hidden state와의 연관성
  - Weight = Energe에 softmax함수를 취해 확률을 구함
  - 각 weight를 encoder의 hidden state와 곱해 decoder의 입력으로 보냄

### Transformer
- RNN, CNN을 필요로 하지 않음.
- Positional Encoding 사용 (위치 정보 포함)
  - 상대적인 위치 정보를 전달하기 위해 주기 함수(sin, cos 등)를 활용 
- last encoder's layer -> all decoder's layer
- RNN보다 일반적으로 time complexity가 낮음
  - RNN : encoder의 개수가 고정, input token의 개수만큼 encoder layer를 반복
  - Transformer : seq단위로 input, 다수의 encoder를 병렬적으로 거침

##### Encoder
- Positional Encoding + Embedding MAtrix -> Attention
- 성능 향상을 위해 Residual learning 사용 (특정 layer를 건너뛰는 기법)
- Attention과 normalization을 반복하여 layer를 쌓음(각 layer는 서로 다른 patameter를 가짐)


##### Decoder
- layer에서 2번의 attention 실행
  - self attention (각 단어들 간의 연관성)
  - encoder-decoder attention (output의 단어들과 소스 문장의 단어들의 연관성)

### Attention
-  Multi-head attention
-  query, key, value
-  encoder-decoder attention의 출력(query)는 encoder의 출력(key, value)를 참고
-  mask matrix를 통해 특정단어 무시 가능
  - attention energy와 같은 dim mask matrix 생성하여 음수 무한 값을 넣음
-  encoder self-attention - 각 단어들과 다른 단어들과의 연관성
-  masked decoder self-attention - 각각의 출력 단어가 앞서 등장했던 단어만 참고 (BERT와 다른 점?)
-  encdoer-decoder attention - decoder의 query가 encoder의 key, value 참고
-  

### Referrence
[[딥러닝 기계 번역] Transformer: Attention Is All You Need (꼼꼼한 딥러닝 논문 리뷰와 코드 실습)
](https://www.youtube.com/watch?v=AA621UofTUA)
