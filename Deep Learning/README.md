# Deep Learning

### Perceptron
![image](https://user-images.githubusercontent.com/62679143/137453262-f68dbad9-2c7a-4991-8223-806605e56f22.png)

![image](https://user-images.githubusercontent.com/62679143/137453612-b30c91f8-8bbd-4423-b296-4553f2927575.png)
- 가중치 W와 편향 b의 최적값을 찾아야 함.
- Activation Function(활성화 함수) - 출력값을 변경시키는 함수 ex)sigmoid, softmax

### Single-Layer Perceptron
- Input Layer와 Output Layer만 존재
- 선형 영역에 대해서만 분리 가능 (하나의 직선으로 분리 가능)
-  AND, OR, NAND gate는 구현 가능하지만 XOR gate는 불가능 (하나의 직선으로 분리 불가능)

### Multi-Layer Perceptron
- Input, Output 이외에도 Hidden Layer(은닉층) 존재
- Deep Neural Network - 은닉층이 2개 이상인 신경망

### Forward propagation
- 입력층에서 출력층 방향으로 예측값의 연산이 진행되는 과정

### Loss function 손실함수
- 실제값과 예측값의 차이(오차)를 수치화하는 함수
- MSE(Mean Square Error) : 연속형 변수(선형회귀 등)
- Cross Entropy : Classification

### Optimizer
- Batch Gradient Descent : 1 epoch당 1번 업데이트, batch size가 전체 데이터
- Stochastic Gradient Descent(SGD) : batch size가 1
- Mini-Batch Gradient Descent : batch size를 정해놓아 비교적 빠르고 안정적
- Momentum : 기울기가 minimum일 때 한 시점 전의 기울기를 일정한 비율만큼 반영
- Adagrad : 각 매개변수에 서로 다른 학습률을 적용함
- RMSprop : 학습이 계속되면 학습률이 지나치게 떨어지는 Adagrad의 단점 개선
- Adam : RMSprop + Momentum

### Back Propagation
- 순전파의 반대 방향으로 연산하며 가중치 업데이트

### Epoch
- 전체 데이터에서 순전파와 역전파가 끝난 상태
- 학습하는 횟수

### Batch size
- 매개변수를 업데이트할 때까지 필요한 데이터 개수
- batch size가 200이면 200개의 데이터마다 매개변수를 업데이트

### Iteration
- epoch가 1번 끝나기 위해 필요한 배치의 수
- 전체 데이터 수/배치의 크기
- 1 epoch 당 매개변수 업데이트가 Iteration 번 일어남
