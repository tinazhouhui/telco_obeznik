

from app.models.date_parsing import file_name, page_title


def create_all_links(pages_groups: dict) -> dict:
    """
    creates a dictionary with month = page as key and file link as value
    """
    all_links = {}
    all_pages = sorted(pages_groups, reverse=True)
    for page in all_pages:
        all_links[page_title(page)] = file_name(page)

    return all_links


def create_latest_page(all_links: dict) -> str:
    """
    returns latest page and its link.
    """
    latest_page = list(all_links.values())[0]

    return latest_page


def create_menu(all_links: dict) -> dict:
    """
    returns latest three pages and their links
    """
    menu = {k: all_links[k] for k in list(all_links)[:3]}

    return menu
