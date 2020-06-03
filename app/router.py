"""
Router where the keys are the name of the page and value the html code that needs to be written.
"""
from typing import Dict

from app.controllers.archive import ArchiveController
from app.controllers.articles import ArticlesController
from app.controllers.index import IndexController
from app.models.date_parsing import file_name, page_title


def router(article_groups: dict) -> dict:
    """
    Assign the correct value to correct page.
    """
    menu = {}
    top_3_articles = sorted(article_groups, reverse=True)[:3]
    for article in top_3_articles:
        menu[page_title(article)] = file_name(article)

    index_page = IndexController(menu)
    archive_page = ArchiveController(menu)

    routes: Dict[str, str] = {
        'index.html': index_page.to_html(),
        'archive.html': archive_page.to_html(),
    }

    for year_month in article_groups:
        articles_in_group = article_groups[year_month]
        article_list = ArticlesController(menu, page_title(year_month), articles_in_group)
        routes[file_name(year_month)] = article_list.to_html()

    return routes
