# Overfitting
- train data에 대해 과하게 학습되어 새로운 데이터에 대해 제대로 동작하지 않음

### 데이터의 양을 늘리기
-  데이터의 양이 적으면 특정 패턴이나 노이즈까지 학습함
-  Data Augmentation : 기존의 데이터를 변형하고 추가하여 데이터의 양을 늘림

### 모델의 복잡도 줄이기
- capacity(수용력) : 모델의 매개변수의 수
- 은닉층, 매개변수를 줄이기

### 가중치 규제(Regularization)
- L1 규제 : 가중치들의 절대값 합계를 Cost function에 추가
  - 어떤 특성이 모델에 영향을 주는지 판단할 때 유용
- L2 규제(weight decay) : 가중치들의 제곱합을 Cost function에 추가 

### Dropout
- 학습 과정에서 신경망의 일부를 사용하지 않는 방법
- 학습 시에만 사용하고 예측 시에는 사용하지 않음
- 특정 뉴런이나 조합에 의존적이게 되는 것을 방지