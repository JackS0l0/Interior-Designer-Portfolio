from articles.models import Categories,Products
def common_data():
    return{
        'cate':Categories.objects.all().order_by('name'),
    }