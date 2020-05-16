class ArticleListRender:
    """
    Class to render articles.
    """
    def __init__(self, article_list):
        self.article_list = article_list

    def to_html(self):
        article_list_html = ''
        for article in self.article_list:

            title = article['title']
            link = article['link']
            rendered_title = '<h3><a href="{1}">{0}</a></h3>'.format(title, link)

            source = article['source']
            rendered_source = '<h5>{}</h5>'.format(source)

            summary = article['summary']
            rendered_body ='<p>{}</p>'.format(summary)

            article_list_html += rendered_title + rendered_source + rendered_body

        return article_list_html

    def sub_heading(self, source):
        rendered_sub_heading = [source]
        return rendered_sub_heading

    def body(self, summary):
        rendered_body = [summary]
        return rendered_body

# TODO: render should render per article rather than heading, body..delete this and create ArticleListRender
