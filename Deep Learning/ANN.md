# Artificial Neural Network

### Feed-forward Neural Network
- 단방향(입력층 -> 출력층)으로 연산이 전개되는 신경망

### Fully-connected Layer, Dense Layer
- 모든 뉴런이 이전 층의 모든 뉴런과 연결되어 있는 Layer

### Activation Function
- 뉴런의 출력값을 결정하는 함수
- 비선형 함수여야 한다
- Step function - deprecated
- Sigmoid function - vanishing gradient 문제,Binary Classification
- Hyperbolic tangent function - Sigmoid보다 기울기 소실이 적음
- ReLU function - dying ReLU 문제
- Leaky ReLU - Input이 음수일 경우 매우 작은 수(hyper parameter) 변환
- Softmax function - 출력층에서 사용, Multi-Class Classification
