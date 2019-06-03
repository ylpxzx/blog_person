from django.contrib.admin import AdminSite

class CustomSite(AdminSite):
    site_header = 'multiplayer_blog'
    site_title = 'multiplayer_blog管理后台'
    index_title = '首页'

custom_site=CustomSite(name='xadmin')