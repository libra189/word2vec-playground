from django.shortcuts import render
from django.http.response import HttpResponse
import gensim
import json

model = gensim.models.doc2vec.Doc2Vec.load('models/doc2vec.model')

# Create your views here.
def word2vec(request):
    word = request.GET.get('word')
    sims = model.most_similar(word, topn=10)

    d_list = []
    for sim in sims:
        d_list.append({sim[0] : sim[1]})
    
    jsonItem = json.dumps(d_list, ensure_ascii=False)
    return HttpResponse(jsonItem)