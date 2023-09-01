from django.shortcuts import render
from .models import News

# Create your views here.
def news(req):
    news = News.objects.all().order_by("-date")
    ctxt= {"News":news}
    return render(req, "news.html", ctxt)
