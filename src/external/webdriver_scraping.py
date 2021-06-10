# type: ignore
import logging
from src.domain.entities.result_search_entity import ResultSearchEntity
from src.domain.entities.poster_entity import PosterEntity
from src.domain.entities.details_entity import DetailsEntity
from selenium.webdriver.chrome.webdriver import WebDriver
from typing import List
from src.domain.errors.failures import ScrapingFailure
from selenium import webdriver
from src.data.datasources.scraping_datasource import ScrapingDatasource
import os


class WebDiverScraping(ScrapingDatasource):
    def __init__(self, url: str):
        self.url = url

    def get_posters(self) -> List[PosterEntity]:
        try:
            driver = configure_set_up_driver()
            driver.get(self.url)
            driver = page_down(driver)
            driver = page_down(driver)
            driver = page_down(driver)
            driver = page_down(driver)

            list_posters = driver.find_elements_by_class_name(
                'title-list-grid__item')
            posters = []
            for poster in list_posters:
                link = get_url_page(poster)
                type_poster = get_type_page(poster)
                image = get_image_page(poster)
                poster_entity = PosterEntity(
                    url=link, type_poster=type_poster, image=image)
                posters.append(poster_entity)
            return posters
        except Exception as error:
            logging.exception(
                f"Failed to retrieve posts on scraping: {error}")
            raise ScrapingFailure()
        finally:
            driver.quit()

    def result_search(self) -> List[ResultSearchEntity]:
        try:
            list_results_search: List[ResultSearchEntity] = []
            driver = configure_set_up_driver()
            driver.get(self.url)
            driver = page_down(driver)
            driver = page_down(driver)
            driver = page_down(driver)
            driver = page_down(driver)

            results = driver.find_elements_by_tag_name('ion-row')
            for result in results:
                col1:  WebDriver = result.find_elements_by_tag_name(
                    'ion-col')[0]
                col2:  WebDriver = result.find_elements_by_tag_name(
                    'ion-col')[1]
                title: str = get_title_page(col2)
                year: str = get_year_page(col2)
                type_poster: str = get_type_page(col1)
                url: str = get_url_page(col1)
                list_providers = get_providers_page(col2)
                image = get_image_page(col1)
                poster = PosterEntity(url=url, image=image,
                                      type_poster=type_poster)
                result_model = ResultSearchEntity(
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

    def get_details(self) -> DetailsEntity:
        try:
            driver = configure_set_up_driver()
            driver.get(self.url)
            driver = page_down(driver)
            image: WebDriver = driver.find_element_by_tag_name('picture')
            type_poster: str = get_type_page(driver)
            image: str = get_image_page(image)
            year: str = driver.find_element_by_class_name('text-muted').text
            details = driver.find_elements_by_class_name(
                'detail-infos__detail--values')
            runtime: str = details[6].text
            list_gender = details[5].find_elements_by_tag_name('span')
            title: str = driver.find_element_by_class_name(
                'title-block').find_element_by_tag_name('h1').text
            sinopse: str = driver.find_element_by_class_name(
                'text-wrap-pre-line').find_element_by_tag_name('span').text
            list_banners = driver.find_elements_by_class_name(
                'swiper-slide')
            list_seansons = driver.find_element_by_class_name(
                'horizontal-title-list').find_elements_by_tag_name('a')
            list_providers = driver.find_elements_by_class_name(
                'price-comparison__grid__row__element__icon')

            genders = getGenders(list_gender)
            providers = getProviders(list_providers)
            banners = getBanners(list_banners, driver)
            seansons = getSeansons(list_seansons, type_poster)

            details = DetailsEntity(
                title=title,
                banners=banners,
                poster_image=image,
                year=year,
                runtime=runtime,
                genders=genders,
                type_poster=type_poster,
                seansons=seansons,
                providers=providers,
                sinopse=sinopse
            )
            return details
        except Exception as error:
            logging.exception(
                f"Failed to retrieve details on scraping: {error}")
            raise ScrapingFailure()
        finally:
            driver.quit()


def get_title_page(col2):
    return col2.find_element_by_class_name(
        'title-list-row__row__title').text


def get_year_page(col2):
    return col2.find_element_by_class_name(
        'title-list-row__row--muted').text


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
    try:
        image = col1.find_element_by_tag_name('source')
        image = image.get_attribute('srcset')
    except Exception:
        image = col1.find_element_by_tag_name('source')
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
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    return webdriver.Chrome(
        executable_path=os.environ.get("CHROMEDRIVER_PATH"),
        options=chrome_options
    )


def getProviders(list_providers: list) -> list:
    providers = []
    for provider in list_providers:
        a = provider.find_element_by_tag_name('a')
        image = a.find_element_by_tag_name('img')

        providers.append(image.get_attribute('src'))
    return providers


def getGenders(list_gender: list) -> list:
    genders = []
    for gender in list_gender:
        if gender.text != ',' and gender.text != ', ':
            genders.append(gender.text.replace(',', ''))
    return genders


def getBanners(list_banners: list, driver) -> list:
    script = '''document.getElementsByClassName('backdrop-carousel__arrows__arrow--right')
    [0].click()'''
    banners = []
    for banners_image in list_banners:
        try:
            driver.execute_script(script)
            picture = banners_image.find_element_by_tag_name('picture')
            image = get_image_page(picture)
            banners.append(image)

        except Exception:
            pass
    return banners


def getSeansons(list_seansons: list, type_poster) -> list:
    seansons: List[PosterEntity] = None
    for se in list_seansons:
        try:
            picture = se.find_element_by_tag_name('picture')
            image = get_image_page(picture)
            if image is not None:
                poster = PosterEntity(
                    image=image, type_poster=type_poster, url='NOT_URL')
                seansons.append(poster)

        except Exception:
            pass
    return seansons


def page_down(element):
    script = '''function doScrolling(elementY, duration){
    var startingY = window.pageYOffset;
    var diff = elementY - startingY;
    var start;
    window.requestAnimationFrame(function step(timestamp) {
        if (!start) start = timestamp;
        // Elapsed milliseconds since start of scrolling.
        var time = timestamp - start;
        // Get percent of completion in range [0, 1].
        var percent = Math.min(time / duration, 1);

        window.scrollTo(0, startingY + diff * percent);

        // Proceed with animation as long as we wanted it to.
        if (time < duration) {
        window.requestAnimationFrame(step);
        }
    })
    }
    doScrolling(document.body.scrollHeight, 5000)
    '''

    element.execute_script(script)
    return element
