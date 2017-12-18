import MeCab
text1='私は村田AのA10-1号室について知りたいです。？'
text3=[]
for text2 in MeCab.Tagger().parse(text1).splitlines()[:-1]:
      (w1,h1) = text2.split('\t')
      if h1.startswith('名詞'):
          text3.append(w1)
print(text3)
s="".join(text3)
print(s)
