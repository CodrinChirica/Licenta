# from pylinkchecker.api import crawl
from pylinkchecker.api import crawl_with_options


def linkChecker(search_url):
    result = {}
    crawled_site = crawl_with_options(["http://www.info.uaic.ro/bin/Main"], {"run-once": True})
    number_of_crawled_pages = len(crawled_site.pages)
    number_of_errors = len(crawled_site.error_pages)

    result['is_ok'] = crawled_site.is_ok
    result['total_links'] = number_of_crawled_pages

    result['bad_links'] = {}
    result['bad_links']['count'] = number_of_errors

    result['bad_links']['list'] = []

    for bad_link, resource in crawled_site.error_pages.items():
        url = bad_link.netloc + bad_link.path
        status = resource.status
        link_info = {}
        link_info['url'] = url
        link_info['status'] = status
        result['bad_links']['list'].append(link_info)

    print(result)

    return result
    # print(crawled_site.error_pages)
