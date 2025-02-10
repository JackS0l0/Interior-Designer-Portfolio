from articles.models import Categories,Products
from main.models import MainTexts,AboutInFooter,HeaderBackgroud,Partners
def common_data():
    return{
        'cate':Categories.objects.all().order_by('name'),
        'partners':Partners.objects.all(),
        'mt':MainTexts.objects.all(),
        'aif':AboutInFooter.objects.all(),
        'hb':HeaderBackgroud.objects.all(),
    }