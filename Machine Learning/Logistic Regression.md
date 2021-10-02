# Logistic Regression
- Binary Classification을 위한 알고리즘
- Sigmoid 함수 사용

### Sigmoid function
![1024px-Logistic-curve](https://user-images.githubusercontent.com/62679143/135709463-67c1e5b9-a0d2-486f-9a2c-216a7a43587f.png)
![image](https://user-images.githubusercontent.com/62679143/135709491-92dcaa9d-edcc-438b-a9e7-458153d6bc5b.png)

- 0 ~ 1의 값을 가지며 S자형 곡선을 가지는 함수
- 0.5 이상은 1, 0.5 이하는 0
- W가 커질수록 경사가 가파르다

### Cost funcction
- MSE를 사용하면 잘못된 최솟값(기울기가 0인 지점)에 도달할 수 있다
-> Cross Entropy function 사용

```
import numpy as np
%matplotlib inline
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers

X = np.array([-50, -40, -30, -20, -10, -5, 0, 5, 10, 20, 30, 40, 50])
y = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]) # 10이상부터 1, 그 이하는 0으로 맵핑

model = Sequential()
model.add(Dense(1, input_dim=1, activation='sigmoid'))

# 옵티마이저는 경사하강법 sgd를 사용합니다.
# 손실 함수(Loss function)는 binary_crossentropy(이진 크로스 엔트로피)를 사용합니다.
sgd = optimizers.SGD(lr=0.01)
model.compile(optimizer=sgd ,loss='binary_crossentropy', metrics=['binary_accuracy'])

# 주어진 X와 y데이터에 대해서 오차를 최소화하는 작업을 200번 시도합니다.
model.fit(X,y, batch_size=1, epochs=200, shuffle=False)
```

```
Epoch 1/200
13/13 [==============================] - 1s 65ms/step - loss: 0.3375 - binary_accuracy: 0.8462
... 중략 ...
Epoch 192/200
13/13 [==============================] - 0s 1ms/step - loss: 0.0898 - binary_accuracy: 1.0000
... 중략 ...
Epoch 200/200
13/13 [==============================] - 0s 1ms/step - loss: 0.0883 - binary_accuracy: 1.0000
```
