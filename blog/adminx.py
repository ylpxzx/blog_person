import xadmin
from .models import Post,Category,Tag
from django.urls  import reverse
from django.utils.html import format_html
from multiplayer_blog.base_admin import BaseOwnerAdmin
from xadmin.filters import manager
from xadmin.filters import RelatedFieldListFilter
from xadmin.layout import Row,Fieldset,Container
from .adminforms import PostAdminForm
# Register your models here.


#在同一页面编辑关联数据
class PostInline:#可选择继承自admin.StackedInline以获取不同的展示样式
    form_layout = (
        Container(
            Row("title","desc"),
        )
    )
    extra = 1
    model = Post
    #在分类的编辑页面关联标题和摘要

@xadmin.sites.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    #inlines = [PostInline,]
    list_display = ('name','status','is_nav','created_time','post_count')
    fields = ('name','status','is_nav')

    def post_count(self,obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@xadmin.sites.register(Tag)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name','status','created_time')
    fields = ('name','status')


'''class CategoryOwnerFilter(admin.SimpleListFilter):
    """自定义过滤器只展示当前用户分类"""
    title = '分类过滤器'
    parameter_name = 'owner_category'
    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id','name')
    def queryset(self, request, queryset):
        category_id=self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset'''

class CategoryOwnerFilter(RelatedFieldListFilter):
    @classmethod
    def test(cls,field,request,params,model,admin_view,field_path):
        return field.name=='category'

    def __init__(self,field,request,params,model,model_admin,field_path):
        super().__init__(field,request,params,model,model_admin,field_path)
        #重新获取lookup_choices，根据owner过滤
        self.lookup_choices=Category.objects.filter(owner=request.user).values_list('id','name')
manager.register(CategoryOwnerFilter,take_priority=True)



@xadmin.sites.register(Post)
class PostAdmin(BaseOwnerAdmin):
    form=PostAdminForm
    list_display = [
        'title','category','status','image_img1',
        'created_time','owner','operator'
    ]
    list_display_links = []
    list_filter = ['category',]#'category'是字段名
    search_fields = ['title','category__name']
    save_on_top = True

    actions_on_top = True
    actions_on_bottom = True

    #编辑页面
    #save_on_top = True
    exclude = ['owner']
    '''fields = (
        ('category','title'),
        'desc',
        'status',
        'content',
        'tag',
    )'''
    form_layout=(
        Fieldset(
            '基础信息',
            Row("title","category"),
            'status',
            'tag',
        ),
        Fieldset(
            '内容信息',
            'desc',
            'is_md',
            'content_ck',
            'content_md',
            'content',
        ),
        Fieldset(
        '图片上传',
        'image1',
    )
    )



    #与上面list_display关联
    def operator(self,obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('xadmin:blog_post_change',args=(obj.id,))
        )
    operator.short_description = '操作'


    class Media:
        css={
            'all':("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",),
        }
        js=('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js',)
