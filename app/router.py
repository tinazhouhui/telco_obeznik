"""
Router where the keys are the name of the page and value the html code that needs to be written.
"""
from typing import Dict

from app.controllers.archive import ArchiveController
from app.controllers.articles import ArticlesController
from app.controllers.index import IndexController
from app.models.date_parsing import file_name, page_title
from app.models.output_prep import create_all_links, create_latest_page, create_menu


def router(pages_groups: dict) -> dict:
    """
    Assign the correct value to correct page.
    """
    all_links = create_all_links(pages_groups)
    latest_page = create_latest_page(all_links)
    menu = create_menu(all_links)

    index_page = IndexController(menu, latest_page)
    archive_page = ArchiveController(menu, all_links)

    routes: Dict[str, str] = {
        'index.html': index_page.to_html(),
        'archive.html': archive_page.to_html(),
    }

    for year_month in pages_groups:
        articles_per_page = pages_groups[year_month]
        article_list = ArticlesController(menu, page_title(year_month), articles_per_page)
        routes[file_name(year_month)] = article_list.to_html()

    return routes
