# type: ignore
import logging
from src.data.models.details_model import DetailsModel

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
        finally:
            driver.quit()

    def get_details(self) -> DetailsModel:
        try:
            driver = configure_set_up_driver()
            driver.get(self.url)
            image: WebDriver = driver.find_element_by_tag_name('picture')
            type_poster: WebDriver = driver.find_element_by_class_name(
                'title-poster__badge').text
            image = get_image_page(image)
            year = driver.find_element_by_class_name('text-muted').text
            details = driver.find_elements_by_class_name(
                'detail-infos__detail--values')
            runtime = details[6].text
            list_gender = details[5].find_elements_by_tag_name('span')
            genders = []
            for gender in list_gender:
                if gender.text != ',' and gender.text != ', ':
                    genders.append(gender.text.replace(',', ''))
            title = driver.find_element_by_class_name(
                'title-block').find_element_by_tag_name('h1').text
            sinopse = driver.find_element_by_class_name(
                'text-wrap-pre-line').find_element_by_tag_name('span').text

            list_banners = driver.find_elements_by_class_name(
                'swiper-slide')
            list_seansons = driver.find_element_by_class_name(
                'horizontal-title-list').find_elements_by_tag_name('a')
            list_providers = driver.find_elements_by_class_name(
                'price-comparison__grid__row__element__icon')

            providers = []
            banners = []
            seansons = []

            buttonRight = driver.find_element_by_css_selector(
                "div.backdrop-carousel__arrows__arrow--right")
            for provider in list_providers:
                a = provider.find_element_by_tag_name('a')
                image = a.find_element_by_tag_name('img')

                providers.append(image.get_attribute('src'))
            for banners_image in list_banners:
                try:
                    picture = banners_image.find_element_by_tag_name('picture')
                    image = get_image_page(picture)
                    banners.append(image)
                    buttonRight.click()
                except Exception:
                    pass

            for se in list_seansons:
                try:
                    picture = se.find_element_by_tag_name('picture')
                    image = get_image_page(picture)
                    seansons.append(image)
                except Exception:
                    pass
            detailsModel = DetailsModel(
                title=title,
                banners=banners,
                poster_image=image,
                year=year,
                runtime=runtime,
                genders=genders,
                type_poster=type_poster,
                seansons=seansons,
                providers=providers,
                sinopse=sinopse,)
            return detailsModel
        except Exception as error:
            logging.exception(
                f"Failed to retrieve details on scraping: {error}")
            raise ScrapingFailure()
        finally:
            driver.quit()


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
