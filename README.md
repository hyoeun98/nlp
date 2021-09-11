# NLP

## Preprocessing

### Tokenization

#### BPE(Byte Pair Encoding)
- 기계가 모르는 단어 Out-Of-Vocabulary or Unknown Token -> OOV 문제
- Subword segmentation
- 희귀 단어, 신조어 파악 가능
- 연속적으로 가장 많이 등장한 글자의 쌍을 찾아서 하나의 글자로 병합
'''
aaabdaaabac

ZabdZabac
Z=aa

ZYdZYac
Y=ab
Z=aa

XdXac
X=ZY
Y=ab
Z=aa
'''
1. 단어를 글자 단위로 분리하여 vocabulary 생성
2. 가장 많이 등장하는 unigram pair를 병합하여 vocabulary에 추가 (n번 반복)
3. 새로운 단어 등장 시 글자 단위로 분리하여 vocabulary에서 탐색

- WPM (WordPiece Model)
-- BPE는 빈도 수에 기반하여 병합하지만, WPM는 병합되었을 때 corpus의 likelihood가 가장 높은 pair 병합
'''
WPM을 수행하기 이전의 문장: Jet makers feud over seat width with big orders at stake
WPM을 수행한 결과(wordpieces): _J et _makers _fe ud _over _seat _width _with _big _orders _at _stake
'''

-- 모든 단어의 앞에 _를 붙이고, 통계에 기반하여 subword 분리 
-- underscore _는 subword의 분리와 기존의 띄어쓰기를 구분하기 위함, 

- Unigram Language Model Tokenizer
-- 각각의 subword들에 대한 loss 계산 (subword가 vocabulary에서 제거되었을 때 감소하는 likelihood)
-- 손실이 가장 큰 토큰부터 제거

## Model

## 참고 
- https://kcorpus.korean.go.kr/, https://corpus.korean.go.kr/ (Korean corpus)
- https://wikidocs.net/book/2155 (딥 러닝을 이용한 자연어 처리 입문)
- https://www.kaggle.com/ (kaggle)
- http://www.ontorus.net/page/default.aspx (Korean thesaurus)
