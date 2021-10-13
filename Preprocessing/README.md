# Preprocessing

- Cleaning(특수문자 제거, 짧은 단어 제거, 소문자 변환)
- 토큰화
- 불용어 제거

### Detokenization
```
# 역토큰화 (토큰화 작업을 역으로 되돌림)
detokenized_doc = []
for i in range(len(news_df)):
    t = ' '.join(tokenized_doc[i])
    detokenized_doc.append(t)

news_df['clean_doc'] = detokenized_doc
```
