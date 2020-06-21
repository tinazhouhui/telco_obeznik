"""
output dictionary prep to insert into views.
"""

from app.models.date_parsing import file_name, page_title


def translate(month: str) -> str:
    """
    translates months to czech
    """
    months_dict = {
        'January': 'Leden',
        'February': 'Únor',
        'March': 'Březen',
        'April': 'Duben',
        'May': 'Květen',
        'June': 'Červen',
        'July': 'Červenec',
        'August': 'Srpen',
        'September': 'Září',
        'October': 'Říjen',
        'November': 'Listopad',
        'December': 'Prosinec',
    }
    if month not in months_dict:
        raise Exception('Only months in English with first capital letter')

    month_translated = months_dict[month]

    return month_translated


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
    returns latest page's link.
    """
    latest_page = list(all_links.values())[0]

    return latest_page


def create_latest_month(all_links:dict) -> str:
    """
    returns latest page's title.
    """
    latest_month = list(all_links.keys())[0]

    return latest_month


def create_menu(all_links: dict) -> dict:
    """
    returns latest three pages and their links
    """
    menu = {k: all_links[k] for k in list(all_links)[:3]}

    return menu


def create_archive_menu(all_links: dict) -> dict:
    """
    returns links per year for archive
    """

    archive_menu = {}

    for key, value in all_links.items():
        year = ''.join(list(filter(str.isdigit, value)))
        if year not in archive_menu:
            archive_menu[year] = {
                key: value
            }
        else:
            archive_menu[year][key] = value

    return archive_menu
