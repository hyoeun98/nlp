# Tensor 
- 0D tensor
  - 하나의 실수로 이루어진 스칼라 값
- 1D tensor
  - 1차원 배열로 이루어진 벡터 값  
- 2D tensor
  - 2차원 배열로 이루어진 행렬
- 3D tensor
  - 3차원 배열로 이루어진 텐서
  - DS에서 주로 3차원 이상의 배열을 텐서라고 부름(convention)
  - sequence data를 표현할 때 사용됨 (batch size, timesteps, word dim) = 데이터의 개수, 한 시퀀스의 길이, word의 차원

- 벡터와 행렬의 연산

- 독립 변수 = 입력 행렬, 종속 변수  = 출력 행렬
- ![image](https://user-images.githubusercontent.com/62679143/135986233-88f99853-586c-4d47-8866-d0785d214014.png)

- 미니배치 학습 : 전체 데이터를 n개씩 묶어서 학습 (n = batch size)
  
