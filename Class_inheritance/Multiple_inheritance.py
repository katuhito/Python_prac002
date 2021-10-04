#クラスの多重継承
class Page:

    def __init__(self, num, content):
        self.num = num
        self.content = content

    def output(self):
        return f'{self.content}'

#HTMLPageMixinクラス
class HTMLPageMixin:
    def to_html(self):
        return f'<html><body>{self.output()}</body></html>'

"""クラスを分離する
    HTMLPageMixinではなく、Pageクラスのサブクラスでメソッドto_html()を定義しても同じ処理は
    実現可能である。しかし、~Mixinを使った場合は、Pageクラスの責任範囲をページの内容にかかわる部分に限定でき、
    そのページをどのように扱うかというロジックをPageクラスから分離して管理できるメリットがある。
"""

#上記2つのクラスを多重継承
class WebPage(Page, HTMLPageMixin):
    pass

#多重継承したWebPageクラスをインスタンス化
page = WebPage(0, 'web content')
# page.to_html()
print(page.to_html())
