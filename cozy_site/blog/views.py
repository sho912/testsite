from django.shortcuts import render, get_object_or_404
from .models import News, Construction, Subsidy, Tag
from django.core.paginator import Paginator
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.urls.base import reverse_lazy
from django.views.generic import TemplateView



#記事タイプ「お知らせ」
def News_list(request):
    news_posts = News.objects.order_by('-pub_date')
    paginator = Paginator(news_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'news_posts': page_obj}
    return render(request, 'blog/page/news_list.html', context)

#お知らせ詳細ページ
def news_detail(request, slug):
    post = get_object_or_404(News, slug=slug)
    return render(request, 'blog/page/news_detail.html', {'post': post})



#記事タイプ「補助金」
def Subsidy_list(request):
    subsidy_posts = Subsidy.objects.order_by('-pub_date')[:5]
    context = {'subsidy_posts': subsidy_posts}
    return render(request, 'blog/page/subsidy_list.html', context)

#補助金詳細ページ
def subsidy_detail(request, slug):
    post = get_object_or_404(Subsidy, slug=slug)
    return render(request, 'blog/page/subsidy_detail.html', {'post': post})



#記事タイプ「施工事例」
def Construction_list(request):
    construction_posts = Construction.objects.order_by('-pub_date')[:9]
    context = {'construction_posts': construction_posts}
    return render(request, 'blog/page/construction_list.html', context)

#施工事例詳細ページ
def construction_detail(request, slug):
    post = get_object_or_404(Construction, slug=slug)
    context = {
        'post': post,
        'kitchen-B': post.kitchen_B,
        'kitchen-A': post.kitchen_A,
        'toilet-B': post.toilet_B,
        'toilet-A': post.toilet_A,
        'living-B': post.living_B,
        'living-A': post.living_A,
        'entrance-B': post.entrance_B,
        'entrance-A': post.entrance_A,
        'stairs-B': post.stairs_B,
        'stairs-A': post.stairs_A,
        'etc-B': post.etc_B,
        'etc-A': post.etc_A,
    }
    return render(request, 'blog/page/construction_detail.html', context)


#お問い合わせ
class ContactFormView(FormView):
    template_name = "blog/contact.html"
    form_class = ContactForm
    success_url = "送信完了/"

    def form_valid(self, form):
        form.send_email(
            username=self.request.user.username, 
            email=self.request.user.email
        )
        return super().form_valid(form)

class ContactResultView(TemplateView):
    template_name = "blog/contact_result.html"



#htmlファイル紐づけ
def frontpage(request):
    news_posts = News.objects.order_by('-pub_date')[:5]
    construction_list = Construction.objects.order_by('-pub_date')[:5]
    subsidy_list = Subsidy.objects.order_by('-pub_date')[:5]

    return render(request, "blog/frontpage.html", {
        "news_posts": news_posts,
        "construction_list": construction_list,
        "subsidy_list": subsidy_list
    })


#あと下記を1個にまとめる
def information_view(request):
    return render(request, 'blog/information.html')

def inspection_view(request):
    return render(request, 'blog/inspection.html')

def stock_view(request):
    return render(request, 'blog/stock.html')

    
#まとめるここまで