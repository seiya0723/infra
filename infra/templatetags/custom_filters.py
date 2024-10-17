import re
from django import template

from infra.models import BridgePicture

register = template.Library()

@register.filter
def split_comma(value):
    # valueがNoneの場合、空のリストを返す
    if not value:
        return []
    return value.split(",")

@register.filter(name='store')
def store(value, storage):
    if 'value' not in storage:
        storage['value'] = value
        return None
    previous = storage['value']
    storage['value'] = value
    return previous

@register.filter(name='remove_prefix')
def remove_prefix(value, arg):
    """指定されたプレフィックスを削除するフィルター"""
    if value.startswith(arg):
        return value[len(arg):]
    return value

@register.filter
def sort_list(value):
    try:
        return sorted(value)
    except TypeError:
        return value
    
# 2つのforループを合体させて同じ挙動とする(bridge_table.html)
@register.filter
def zip_lists(a, b):
    return zip(a.split(','), b.split(','))

# 異なるモデルのデータをテンプレートに表示
@register.filter
def get_bridge_picture(pictures, picture):
    try:
        return pictures.get(this_time_picture=picture)
    except BridgePicture.DoesNotExist:
        return None