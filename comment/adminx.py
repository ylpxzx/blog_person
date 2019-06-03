import xadmin
from .models import Comment
# Register your models here.

@xadmin.sites.register(Comment)
class CommentAdmin:
    list_display = ('target','nickname','content','website','created_time')

