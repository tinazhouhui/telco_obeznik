"""
Rendering of articles to html code.
"""


class ArticleListRender:
    """
    Class to render articles.
    """

    def __init__(self, article_list):
        self.article_list = article_list

    def to_html(self):
        """
        renders each article to an html string and creates one continuous string.
        """
        article_list_html = ''
        for article in self.article_list:

            title = article['title']
            link = article['link']
            rendered_title = '<h3><a href="{1}">{0}</a></h3>'.format(title, link)

            source = article['source']
            rendered_source = '<h5>{}</h5>'.format(source)

            summary = article['summary']
            rendered_body = '<p>{}</p>'.format(summary)

            article_list_html += rendered_title + rendered_source + rendered_body

        return article_list_html
