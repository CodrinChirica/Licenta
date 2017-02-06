from django.http import HttpResponse
from django.template import loader, Context
from .functionality import *


def index(request):
    context = Context({})
    if request.method == 'POST':
        if 'search_url' in request.POST:
            if request.POST['search_url'] is not None:
                search_url = request.POST['search_url']
                context['search_url'] = search_url

#                #--------------MOBILE SCREENSHOT API----------------

                # use hardcoded json
                screenshotJson = {'status': 'finished', 'image_url': 'http://api.page2images.com/ccimages/a7/2a/7j1EXDWFvka7ofQP.png',
                                  'duration': 1, 'left_calls': '2981', 'mobileok': 'fuuuuck', 'ori_url': 'http://www.google.com'}

                # screenshotJson = getMobileScreenshot(search_url)
                if screenshotJson is not None:
                    context['screenshot_url'] = screenshotJson
                    # context.update({'screenshot_url': screenshotJson})

#                #--------------GOOD/BAD LINKS API-------------------

                # linkChecker(search_url)

#                #--------------VALIDATORS----------------------------
                markupValidator(search_url)
    else:
        pass
    # if screenshotJson is not None:

    template = loader.get_template('licenta_gui/index.html')
    print(context)
    return HttpResponse(template.render(context, request))

    # return HttpResponse(my_data, content_type='application/vnd.ms-excel')


def googleRankChecker(request):
    print(request.POST)
    keyword = request.POST['rankKeyword']
    search_url = request.POST['search_url']
    # if request.POST['keyword'] is not None:
    # keyword = request.POST['keyword']
    google_rank = rank_checker(keyword, search_url)
    return HttpResponse(json.dumps({'google_rank': google_rank}), content_type='application/json')
