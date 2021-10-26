# Keras
- Tokenizer(): 토큰화, 정수 인코딩
- pad_sequence(): 기준보다 긴 문장은 자르고, 짧은 문장은 0으로 padding

### Word Enbedding
- 텍스트 내의 단어들을 dense vector로 만드는 것
- 밀집 벡터(dense vector) <--> 희소 벡터(sparse vector)
- embedding(): 정수 인코딩 된 단어들을 입력 받아 임베딩 수행

### Modeling
- Sequential()
```
model = Sequential()
model.add(...) # 층 추가
model.add(...) # 층 추가
model.add(...) # 층 추가
```

- Dense(): fully-connected layer 추가.
```
model = Sequential()
model.add(Dense(1, input_dim=3, activation='relu'))
```
- activation으로 linear(선형 회귀), sigmoid(이진 분류), softmax(다중 분류), relu(은닉층) 등
- summary(): 모델 정보

### Compile, Training
- compile(optimizer=' ',loss=' ', metrics=' ')
  - optimizer: 훈련과정
  - loss: loss function
  - metrics: 모니터링의 지표
  - ![image](https://user-images.githubusercontent.com/62679143/138888495-a00c1cdc-8b5a-4f81-a7d4-a88b528ac3b5.png)
- fit(): 모델의 training 시작
  - verbose
```
  # verbose = 0일 경우.
출력 x

  # verbose = 1일 경우.
Epoch 88/100
7/7 [==============================] - 0s 143us/step - loss: 0.1029 - acc: 1.0000

  # verbose = 2일 경우.
Epoch 88/100
 - 0s - loss: 0.1475 - acc: 1.0000
```

### Evaluation, Prediction
- evaluate(): 모델의 정확도 평가 
```
model.evaluate(X_test, y_test, batch_size=32)
```

- predict(): 임의의 입력에 대한 모델의 출력
```
model.predict(X_input, batch_size=32)
```

### Save, Load
- save(): 모델을 hdf5 파일에 save
- load.model(): 저장해둔 모델 load

### Keras Functional API
- 각 layer를 function으로 취급
- input shape를 명시한 input layer를 정의해두어야 함

- Input()에 입력 크기 정의
- 이전 층을 다음 층의 입력으로 사용하고 변수에 할당
- Model()에 input과 output 정의
```
inputs = Input(shape=(10,))
hidden1 = Dense(64, activation='relu')(inputs)  # <- 새로 추가
hidden2 = Dense(64, activation='relu')(hidden1) # <- 새로 추가
output = Dense(1, activation='sigmoid')(hidden2) # <- 새로 추가
```

### Keras Subclassing API
![image](https://user-images.githubusercontent.com/62679143/138896213-1ce4fbe5-4f4d-4907-b751-45896f04f11b.png)
- Sequential API, Function API로 구현 불가능한 모델 구현 가능

### Pros and Cons
- Sequential: 단순하게 층을 쌓는 방식으로 간단함, 다수의 입출력을 가지거나 layer 간 연결,연산하는 모델 구현x
- Function: Sequential로 구현하기 어려운 모델 구현 가능,input layer를 입력 크기와 함께 정의해주어야 함
- Subclassing: 모델 구현의 자유성, OOP에 익숙해야 하므로 까다로움

