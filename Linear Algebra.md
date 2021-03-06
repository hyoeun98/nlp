# 선형대수학
### Keyword
Span, linearly independent, linearly dependent
- Rn의 Subspace V에 대해
  - 0벡터를 포함
  - V의 원소인 벡터x는 c * x를 하더라도 V에 포함되어 있다 (closure under scaler multiplication)
  - 벡터a와 벡터b가 V에 포함되어 있다면 a+b도 포함되어 있다 (closure under addition)

basis : 어떠한 공간을 생성하는데 필요한 minimum set
  - S(set of vectors)가  subspace을 span한다
  - 선형 독립이다

Dot Product(내적)
- 두 벡터의 성분을 서로 곱하여 더한 실수 값(scalar)
- 두 벡터의 내적은 벡터 길이와 cosine의 곱과 같다
![image](https://user-images.githubusercontent.com/62679143/135958645-3bd08114-b58e-4fc0-88c0-3c1d560cc656.png)

Length

![image](https://user-images.githubusercontent.com/62679143/135800054-3d24015d-e595-4616-b1ae-f60a073bb7eb.png) 
- 길이의 제곱은 같은 벡터를 내적한 값과 같다


Cauchy Schwarz Inequality
- 두 벡터의 내적의 절댓값은 두 벡터의 길이의 곱보다 작거나 같다 
- 한 벡터가 다른 벡터의 스칼라배일 때 두 벡터의 길이의 곱은 내적과 같다

Triangle Inequality
- 두 벡터의 합의 길이는 각각의 길이의 합보다 작거나 같다
- 한 벡터가 다른 벡터의 스칼라배일 때 등식이 성립한다

Perpendicular
- 영벡터가 아닌 두 벡터 사이의 각도가 90, 내적 값이 0
  - Orthogonal : 두 벡터의 내적 값이 0 
- 영벡터는 모든 벡터와 orthogonal이지만 perpendicular는 아님

normal vector (법선 벡터)
- 면의 모든 벡터와 직각을 이루는 벡터
- 법선 벡터와 3차원 면 위에 존재하는 두 점의 차는 수직이다. 
- 평면 Ax+By+Cz=D에서 법선벡터는 Ai+Bj+Ck이다. 


Cross Product (외적)
- 3차원 실수 공간에서만 정의 
- 두 벡터에 대해 모두 orthogonal한 벡터가 결과로 나옴
- 두 벡터의 외적의 절댓값은 평행사변형의 넓이와 같다
- ![image](https://user-images.githubusercontent.com/62679143/135953755-91d4f424-8996-4212-9329-068184982b7b.png)

![image](https://user-images.githubusercontent.com/62679143/135958650-04acf084-4861-4888-8b59-5e3179c2cebf.png)

- dot product = ab* cos(두 벡터가 얼마나 같은 방향을 향하는가)
- cross product = ab* sin (두 벡터가 얼마나 수직인가)
- orthographic projection (정사영)

Triple product
- ![image](https://user-images.githubusercontent.com/62679143/136934863-81abeab4-e0b7-4443-ab4b-212e75b23767.png)

점과 평면 사이의 거리
- ![image](https://user-images.githubusercontent.com/62679143/137434240-92a1da80-1d59-438b-b828-8d7aa0fa423a.png)

평면 사이의 거리
- 평행하지 않은 평면 간의 거리는 0
- 평면 위의 한 점과 다른 평면과의 거리를 구함


기약행사다리꼴 (Reduced Row-Echelon Form)
- 선행계수(row에서 처음 등장하는 0이 아닌 수)가 모두 1인 행사다리꼴(Row-Echelon Form)
- Pivot Entry : 각 column에서 유일하게 0이 아닌 수
- zeroed out row : row의 모든 계수가 0인 행, 행렬의 가장 밑에 존재
- Pivot variable <--> Free variable
- 한 row의 vector 가 모두 0일때
  - 0 = N no solution
  - 0 = 0 have free entry, 0 infinite solution

Subspace 
- 부분공간은 덧셈, 곱셈에 대해 닫혀있다 
- 부분공간은 영벡터를 포함한다

null space
- 행렬 A에 대해 A *(dot prouct) N = 0 을 만족하는 벡터의 집합 N
- A의 영공간은 A의 기약행사다리꼴의 영공간과 같다. 
- A의 열벡터들이 선형독립이라면 N(A)  = 0벡터이다.
  - = A의 null space가 0벡터를 포함한다면 A의 column vector는 선형독립이다. 
- Nullity(A): A의 null space의 dimension = # of non-pivot variable in rref(A)
 
Column Space
- 행렬 A의 column vector들의 모든 linear combination = span(column vectors)
- A의 column space = column vector의 너비
- column vector들이 linear independent라면 column space의 basis가 된다
- A의 span은 A의 column vector의 생성과 같다
- pivot 변수를 가진 행들의 linear combination으로 free 변수를 가진 행을 나타낼 수 있다
- basis vector는 자신들의 column space에 존재함
- basis of C(A) = rref(A)의 pivot columns
- basis of C(A)의 dimension(rank) = # of pivot columns
  - rank: dimension of column space 


### 선형독립
- 선형 결합시 0벡터가 되기 위해 모든 상수c가 0이 되어야 한다. 
- 
### 특이값 분해 (Singular Value Decomposition)
- 
### 전치 행렬(Transposed Matrix)
- 행렬의 row와 column을 뒤바꾼 행렬

### 단위 행렬(Identify Matrix)
- 주대각선의 원소가 모두 1이며 나머지 원소는 모두 0인 정사각 행렬

### 역행렬(Inverse Matrix)
- 어떤 행렬과 곱했을 때, 단위 행렬이 나오는 행렬

### 직교 행렬(Orthogonal Matrix)
- 직교 행렬이 역행렬이 되는 행렬

### 대각 행렬(Diagonal Matrix)
- 주대각선을 제외한 원소가 모두 0인 행렬
