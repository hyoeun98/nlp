# Cleaning and Normalization
- Cleaning : corpus의 noise data 제거
  - 불용어 제거
  - 빈도가 적은 단어 제거
  - 길이가 짧은 단어 제거
```
import re
text = "I was wondering if anyone out there could enlighten me on this car."
shortword = re.compile(r'\W*\b\w{1,2}\b')
print(shortword.sub('', text))
```
```
was wondering anyone out there could enlighten this car.
```
길이가 2이하인 단어를 정규 표현식을 이용하여 삭제

- Normalization : 표현 방법이 다른 단어를 하나의 단어로 정규화
  - 이음동의어를 하나의 단어로 (ex. USA = US)
  - stemming, lemmatization 사용
  - 대, 소문자 통합
