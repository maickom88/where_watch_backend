# type: ignore
import logging

from selenium.webdriver.chrome.webdriver import WebDriver
from src.data.models.poster_model import PosterModel
from src.data.models.result_search_model import ResultSearchModel
from typing import List
from src.domain.errors.failures import ScrapingFailure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from src.data.datasources.scraping_datasource import ScrapingDatasource


class WebDiverScraping(ScrapingDatasource):
    def __init__(self, url: str):
        self.url = url

    def get_posters(self) -> List[PosterModel]:
        pass

    def result_search(self) -> List[ResultSearchModel]:
        try:
            list_results_search: List[ResultSearchModel] = []
            driver = configure_set_up_driver()
            driver.get(self.url)

            results = driver.find_elements_by_tag_name('ion-row')
            for result in results:
                col1:  WebDriver = result.find_elements_by_tag_name(
                    'ion-col')[0]
                col2:  WebDriver = result.find_elements_by_tag_name(
                    'ion-col')[1]
                title = get_title_page(col2)
                year = get_year_page(col2)
                type_poster = get_type_page(col1)
                url = get_url_page(col1)
                list_providers = get_providers_page(col2)
                image = get_image_page(col1)
                poster = PosterModel(url=url, image=image,
                                     type_poster=type_poster)
                result_model = ResultSearchModel(
                    title=title,
                    providers=list_providers,
                    year=year,
                    posters=poster
                )
                list_results_search.append(result_model)

            return list_results_search
        except Exception as error:
            logging.exception(
                f"Failed to retrieve posts on scraping: {error}")
            raise ScrapingFailure()


def get_title_page(col2):
    return col2.find_element_by_class_name(
        'title-list-row__row__title')


def get_year_page(col2):
    return col2.find_element_by_class_name(
        'title-list-row__row--muted')


def get_type_page(col1):
    try:
        type_poster = col1.find_element_by_class_name(
            'title-poster__badge').text
        if type_poster is None:
            return ''
        return type_poster
    except Exception:
        pass


def get_url_page(col1):
    return col1.find_element_by_tag_name(
        'a').get_attribute("href")


def get_image_page(col1):
    image = col1.find_element_by_tag_name('source')
    try:
        image = image.get_attribute('srcset')
    except Exception:
        image = image.get_attribute('data-srcset')
        pass
    image = image.split(',')
    image = image[0]
    return image


def get_providers_page(col2):
    providers = col2.find_elements_by_class_name(
        'jw-provider-icon')
    list_providers = []
    for provider in providers:
        list_providers.append(provider.get_attribute('src'))
    return list_providers


def configure_set_up_driver() -> WebDriver:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('window-size=1920x1080')
    chrome_options.add_argument("disable-gpu")
    return webdriver.Chrome(
        ChromeDriverManager().install(), options=chrome_options)
