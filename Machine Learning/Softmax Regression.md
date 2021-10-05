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
