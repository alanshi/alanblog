from django.views.generic import View
from django.shortcuts import render

from .models import Article


class Index(View):
    template_name = 'index.html'

    def get(self, request):
        articles  = Article.objects.all()
        return render(
            request,
            self.template_name,
            {
                'articles': articles,
            }
        )

class Detail(View):

    template_name = 'view.html'

    def get(self, request, pk):
        artcile = Article.objects.get(pk=pk)
        return render(
            request,
            self.template_name,
            {
                'artcile': artcile
            }
        )