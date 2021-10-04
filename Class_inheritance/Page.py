#クラスの継承
class Page:
    def __init__(self, num, content):
        self.num = num
        self.content = content

    def output(self):
        return f'{self.content}'

#メソッドのオーバーライド
class TitlePage(Page):
    def output(self):
        #基底クラスのメソッドは自動では呼ばれないので、明示的に呼び出す
        title = super().output()
        return title.upper()


#インスタンス化
title = TitlePage(0, 'Python Practice Book')
# title.output()
print(title.output())



