from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('企業情報/', views.information_view, name='information'),
    path('住宅診断/', views.inspection_view, name='inspection'),
    path('ストック住宅について/', views.stock_view, name='stock'),
    path('お知らせ/', views.News_list, name='news_list'),
    path('お知らせ/<slug:slug>/', views.news_detail, name='news_detail'),
    path('補助金/', views.Subsidy_list, name='subsidy_list'),
    path('補助金/<slug:slug>/', views.subsidy_detail, name='subsidy_detail'),
    path("お問い合わせ/", views.ContactFormView.as_view(), name="contact"),
    path("お問い合わせ/送信完了/", views.ContactResultView.as_view(), name="contact_result"),
    path('施工事例/', views.Construction_list, name='construction_list'),
    path('施工事例/<slug:slug>/', views.construction_detail, name='construction_detail'),
]