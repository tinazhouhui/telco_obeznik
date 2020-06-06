"""
Router where the keys are the name of the page and value the html code that needs to be written.
"""
from typing import Dict

from app.controllers.archive import ArchiveController
from app.controllers.articles import ArticlesController
from app.controllers.index import IndexController
from app.models.date_parsing import file_name, page_title


def router(pages_groups: dict) -> dict:
    """
    Assign the correct value to correct page.
    """
    menu_all = {}
    all_pages = sorted(pages_groups, reverse=True)
    for page in all_pages:
        menu_all[page_title(page)] = file_name(page)

    latest_page = list(menu_all.values())[0]
    menu = {k: menu_all[k] for k in list(menu_all)[:3]}
    print(menu)


    index_page = IndexController(menu, latest_page)
    archive_page = ArchiveController(menu, menu_all)

    routes: Dict[str, str] = {
        'index.html': index_page.to_html(),
        'archive.html': archive_page.to_html(),
    }

    for year_month in pages_groups:
        articles_per_page = pages_groups[year_month]
        article_list = ArticlesController(menu, page_title(year_month), articles_per_page)
        routes[file_name(year_month)] = article_list.to_html()

    return routes
