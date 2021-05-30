# type: ignore
import logging
from src.data.models.poster_model import PosterModel
from src.data.models.result_search_model import ResultSearchModel
from typing import Any, List
from src.domain.errors.failures import ScrapingFailure
from bs4 import BeautifulSoup
from src.data.datasources.scraping_datasource import ScrapingDatasource


class Bs4(ScrapingDatasource):
    def __init__(self, bs4: BeautifulSoup):
        self.bs4 = bs4

    def get_posters(self) -> List[PosterModel]:
        try:
            list_posters: List[PosterModel] = []
            posters = self.bs4.findAll(
                'div', class_='title-list-grid__item')
            for post in posters:
                link = get_link_poster(post)
                image = get_image_poster(post)
                type_poster = get_type_poster(post)
                poster_model = PosterModel(
                    url=link, image=image, type_poster=type_poster)
                list_posters.append(poster_model)
            return list_posters
        except Exception as error:
            logging.exception(
                f"Failed to retrieve posts on scraping: {error}")
            raise ScrapingFailure()

    def result_search(self) -> List[ResultSearchModel]:
        pass


def get_link_poster(post: Any) -> str:
    link = post.find('a', href=True)
    link = link["href"]
    return link


def get_result_title(result: Any) -> str:
    title = result.findAll('ion-col', class_='md hydrated')[1]
    title = title.find('span', class_='title-list-row__row__title').text
    return title


def get_image_poster(post: Any):
    image = post.find('picture').find('source')
    if image is not None:
        try:
            image = image["srcset"]
        except KeyError:
            image = image['data-srcset']
            pass
        image = image.split(',')
        image = image[0]
    return image


def get_type_poster(post: Any):
    type_poster = post.find('span', class_='title-poster__badge')
    if type_poster is None:
        return None
    return type_poster.text
