"""
Transform the key in the form of year and month to editable strings to be put into titles.
"""

from datetime import datetime
import re


def year_month_parsing(year_month: str) -> str:
    """
    Transforming the year month to a editable string.
    """
    parsed_date = datetime.strptime(year_month, "%Y-%m").strftime("%B %Y")


    return parsed_date

# should be a class? or separate function? also write tests


def page_title(year_month: str) -> str:
    """
    Format year month string to title page format.
    """
    parsed_date = year_month_parsing(year_month)
    title = parsed_date[:-5]

    return title


def filename(year_month: str) -> str:
    """
    Format year month string to filename format.
    """
    parsed_date = year_month_parsing(year_month)
    filename = parsed_date.lower().replace(re.search(r"\s\d{2}", parsed_date).group(), "") + ".html"

    return filename
