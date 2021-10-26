# Gradient Vanishing & Exploding

### Gradient Vanishing (기울기 소실)
- 역전파 과정에서 입력층에 가까울수록 기울기가 작아지는 현상

### Gradient Exploding (기울기 폭주)
- 기울기가 너무 커져 가중치들이 발산하는 현상, RNN에서 발생

### sigmoid 함수 사용 시 역전파 과정에서 기울기 소실 발생
- 은닉층에서 sigmoid 함수 사용 x
- ReLU, Leaky ReLU 등 사용

### Gradient Clipping
- 기울기 폭주를 막기 위해 기울기가 임계점을 넘지 않도록 자름(clipping)

### Weight Initialization
- Xavier Initialization : 이전 Layer와 다음 Layer의 뉴런의 개수에 따라 초기화 
  - sigmoid, hyperbolic tangent와 함께 사용
- He Initialization : 이전 Layer의 뉴런의 개수만 반영
  - ReLU, 변형 ReLU와 함께 사용

### Batch Normalization
- Internal Covariate Shift : 각 Layer마다 입력 데이터 분포가 달라지는 현상
  - Covariate Shift : train data의 분포와 test data의 분포가 달라지는 현상
  - 이전 층들의 가중치가 바뀌면, 현재 층에 전달되는 Input data가 현재 층이 학습했던 시점의 Input data와 다름
- 추가 필요
- ![image](https://user-images.githubusercontent.com/62679143/138884016-81039666-629e-405b-9880-0d96306aab8f.png)
### Layer Normalization

- ![image](https://user-images.githubusercontent.com/62679143/138884041-3fdb22ba-fa1a-43e7-a914-856301b07f13.png)


