from django import template
register=template.Library()

def find_Gtotal(value):
    sum=0
    for item in value:
        sum=sum+item.item_amnt
    return sum

register.filter('find_Gtotal',find_Gtotal)