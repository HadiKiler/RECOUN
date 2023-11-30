# python -m pip install python-Wappalyzer
from Wappalyzer import Wappalyzer, WebPage


def get_wappalyzer(url):
    wappalyzer = Wappalyzer.latest()
    webpage = WebPage.new_from_url('https://' + url)
    data = wappalyzer.analyze_with_versions_and_categories(webpage)
    return data

