from django.shortcuts import render
from django.http.response import HttpResponse
import gensim
import json

model = gensim.models.doc2vec.Doc2Vec.load('models/doc2vec.model')

# Create your views here.
def word2vec(request):
    sims = None
    mode = request.GET.get('mode')
    
    if mode == '0':
        words = request.GET.get('pos')
        word = words.split(',')[0]
        sims = model.most_similar(word, topn=10)
    elif mode == '1':
        pos_words = request.GET.get('pos')
        neg_words = request.GET.get('neg')
        sims = model.most_similar(positive=pos_words.split(','), negative=neg_words.split(','), topn=10)
    else:
        return None

    d_list = []
    for sim in sims:
        d_list.append({sim[0] : sim[1]})
        jsonItem = json.dumps(d_list, ensure_ascii=False)
        return HttpResponse(jsonItem)