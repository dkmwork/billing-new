from django import template

register = template.Library()

'''def modify_name(value,arg):
    if arg=='upper':
        return value.upper()
    else:
        return value.capitalize()'''
def find_Gtotal(value):
    print(value)
    sum=0
    for item in value:
        sum=sum+item.item_amnt
    return sum

#register.filter('modify_name', modify_name)
register.filter('find_Gtotal', find_Gtotal)

    