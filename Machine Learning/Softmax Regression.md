# Softmax Regression
- Multi-class Classification을 위한 알고리즘

### softmax function
- 분류해야 하는 class의 개수 = k
- k차원의 벡터를 입력 받아 각 원소를 0 ~ 1 값으로 변경 후 리턴
- 모든 원소의 합은 1 
- 입력 벡터의 차원을 k로 변환해야 함
  - 각 원소에 k개의 가중치를 곱해서 변환

### One-Hot vector
- 각 클래스 간의 관계가 균등할 때 적절한 labeling
- 단어의 similarity를 구할 수 없음
- 정수 인코딩 시 오차를 구할 때 오류가 나타날 수 있음

### Cost function
- Cross Entropy

![image](https://user-images.githubusercontent.com/62679143/135991984-4bca6ffd-8c30-43b5-ae5c-77d29d0ffba1.png)
```
import pandas as pd
data = pd.read_csv('/content/Iris.csv',encoding = 'latin1')

data['Species'] = data['Species'].replace(['Iris-virginica','Iris-setosa','Iris-versicolor'],[0,1,2]) # 정수 인코딩
from sklearn.model_selection import train_test_split
data_X = data[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].values
data_y = data['Species'].values
(X_train, X_test, y_train, y_test) = train_test_split(data_X, data_y, train_size=0.8, random_state=1) # train data, test data 분리

from tensorflow.keras.utils import to_categorical
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
# 훈련 데이터와 테스트 데이터에 대해서 원-핫 인코딩
```
전처리

```
from tensorflow.keras.models import Sequential # 케라스의 Sequential()을 임포트
from tensorflow.keras.layers import Dense # 케라스의 Dense()를 임포트
from tensorflow.keras import optimizers # 케라스의 옵티마이저를 임포트

model=Sequential()
model.add(Dense(3, input_dim=4, activation='softmax'))
sgd=optimizers.SGD(learning_rate=0.01)
model.compile(loss='categorical_crossentropy', optimizer='adam',metrics=['accuracy'])
# 옵티마이저는 경사하강법의 일종인 adam을 사용합니다.
# 손실 함수(Loss function)는 크로스 엔트로피 함수를 사용합니다.
history=model.fit(X_train,y_train, batch_size=1, epochs=200, validation_data=(X_test, y_test))
```
- binary classification : binary_crossentropy
- multi-class classification : categorical_crossentropy
```
print("\n 테스트 정확도: %.4f" % (model.evaluate(X_test, y_test)[1]))
```
```
30/30 [==============================] - 0s 33us/step
테스트 정확도: 1.0000
```
