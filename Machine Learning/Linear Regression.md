# Linear Regression

### Simple Linear Regression Analysis
- 종속 변수 x, 독립 변수 y에 대해
  - y = Wx + b (W = weight, b = bias)

### Multiple Linear Regression Analysis
- 종속 변수 x와 그에 따른 가중치 W가 다수 존재
  - y = W1x1 + W2x2 + ... + Wnxn + b

### Hypothesis
- x와 y의 관계를 유추하는 수학적 식을 세우는 것

### Cost Fucntion
- 실제 값과 hypothesis로 얻은 예측값의 오차를 최소화 하는 식
- Objective function, Loss function
- 각 문제마다 적절한 cost function이 존재

### Mean Squared Error (평균 제곱 오차)
- 회귀 문제에 적합한 비용 함수
- 오차(실제 값과 예측 값의 차이)를 구해 제곱하여 더한 후 n으로 나눈 값
- MSE를 최소화하는 것이 관건

### Gradient Descent (경사하강법)
- 비용 함수를 미분하여 W를 변경
- 학습률(learning rate) : W를 변경할 때 한번에 움직이는 크기
- 학습률이 지나치게 크면 W값이 발산

```
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers

X=[1,2,3,4,5,6,7,8,9] # 공부하는 시간
y=[11,22,33,44,53,66,77,87,95] # 각 공부하는 시간에 맵핑되는 성적

model = Sequential()

# 입력 x의 차원은 1, 출력 y의 차원도 1. 선형 회귀이므로 activation은 'linear'
model.add(Dense(1, input_dim=1, activation='linear'))

# sgd는 경사 하강법을 의미. 학습률(learning rate, lr)은 0.01.
sgd = optimizers.SGD(lr=0.01)

# 손실 함수(Loss function)은 평균제곱오차 mse를 사용합니다.
model.compile(optimizer=sgd ,loss='mse',metrics=['mse'])

# 주어진 X와 y데이터에 대해서 오차를 최소화하는 작업을 300번 시도합니다.
model.fit(X,y, batch_size=1, epochs=300, shuffle=False)
```
```
Epoch 1/300
9/9 [==============================] - 0s 37ms/step - loss: 294.9226 - mean_squared_error: 294.9226
... 중략 ...
Epoch 167/300
9/9 [==============================] - 0s 1ms/step - loss: 2.1460 - mean_squared_error: 2.1460
... 중략 ...
Epoch 300/300
9/9 [==============================] - 0s 1ms/step - loss: 2.1460 - mean_squared_error: 2.1460
```
