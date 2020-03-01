from django.conf.urls import url
from django.conf import settings
from . import views
from django.views.static import serve
from django.conf.urls.static import static

app_name = "outsource"
urlpatterns = [
    # http://127.0.0.1:8000/
    url(r'^$', views.index, name='index'),
    # http://127.0.0.1:8000/index/
    url(r'^index$', views.index),
    # # http://127.0.0.1:8000/news/detail/projects_id  新闻详情页
    # url(r'^news/detail/(\d+)$', views.news_detail),

    # 图片上传
    url(r'^media/(?P<path>.*)$', serve, {'media_root': settings.MEDIA_ROOT}),

    # 项目列表页
    # http://127.0.0.1:8000/projects
    url(r'^projects$', views.projects, name='projects'),

    # 项目详情页
    # http://127.0.0.1:8000/projects/detail/projects_id
    url(r'^projects/detail/(?P<projects_id>\d+)$', views.projects_detail, name='detail'),

    # 开发者列表页
    # http://127.0.0.1:8000/developers
    url(r'^developers$', views.developers, name='developers'),

    # 开发者详情页
    # http://127.0.0.1:8000/developers/detail/developers_id
    url(r'^developers/detail/(\d+)$', views.developers_detail, name='developers_detail'),

    # 帮助页
    # http://127.0.0.1:8000/help
    url(r'^help$', views.help_menu, name='help'),

    # 项目发布页
    # http://127.0.0.1:8000/publish
    url(r'^publish$', views.publish, name='publish'),

    # 申请开发者页
    # http://127.0.0.1:8000/reg_dev
    url(r'^reg_dev$', views.reg_dev, name="reg_dev"),

    # 需求方帮助页
    # http://127.0.0.1:8000/help/guide1
    url(r'^help/guide1$', views.guide1, name='guide1'),

    # 开发者帮助页
    # http://127.0.0.1:8000/help/guide2
    url(r'^help/guide2$', views.guide2, name='guide2'),

    # 项目收藏
    # http://127.0.0.1:8000/collection
    url(r'^collection/$', views.collection, name='collection'),

    # http://127.0.0.1:8000/jingbiao
    url(r'^jingbiao/$', views.jingbiao, name='jingbiao'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
