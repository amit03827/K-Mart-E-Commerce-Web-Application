from cms.models import WebsiteSetting

def website_seting(request):
    website_seting=WebsiteSetting.objects.all().last()
    return { 'global_website_seting' : website_seting,}