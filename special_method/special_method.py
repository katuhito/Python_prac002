"""特殊メソッド"""
#Pythonが暗黙的に呼び出すメソッド。例えば、組み込み関数len()は引数に渡したオブジェクトの特殊メソッド__len__()を暗黙的に利用する。

class A:
    def __len__(self):
        return 5

a = A()
len(a)
#=> 5

#自分が定義したクラスでも、特殊メソッドを実装すると多くの演算子や構文を実装できる。
#それぞれの特殊メソッドは、どのような実装をすべきか決められている。
#例えば、__len__()の場合には、0以上の整数を返す必要があり、これに従っていない場合には、実行時のチェックでエラーになる。

#__str__(), __repr__()：オブジェクトを文字列で表現する。
#python対話モードでは、オブジェクト名を入力すると、そのオブジェクトの文字列表現を得られる。
#同じように、組み込み関数Print()でもオブジェクトを文字列で出力できる。しかし、この両者の結果は、次のように結果が一致しない場合がある。
#これは、オブジェクト名のみを入力した際は__repr__()が呼び出され、組み込み関数print()に渡された際には、__str__()が呼び出されるためである。
#この2つの特殊メソッドは、どちらもオブジェクトの文字列表現を返すのだが、主な用途が異なる。

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
    def __str__(self):
        return f'({self.x}, {self.y})'

p = Point(1, 2)
p  # => Point(1, 2)
print(p)  # => (1, 2)

#__repr__()は、デバッグなどに役立つ情報を提供するために利用される特殊メソッドである。可能であれば、そのオブジェクトを再現するために有効なPythonの式がよいとされている。
#__str__()は、組み込み関数であるprint()やstr(), f'{}'などで利用ユーザーフレンドリーな文字列を返す特殊メソッドである。人の目で見てわかりやすい文字列表現を考えるとよい。もし、__str__()が実装されていない場合は、__repr__()がよばれるので、__repr__()から先に実装するのがよい。


#__bool__()：オブジェクトを真理値で評価する。
#Pythonでは、すべてのオブジェクトが真理値評価することができる。偽となるオブジェクト以外はすべて真となる。ユーザー定義のクラスやインスタンスはデフォルトで真と評価されるが、特殊メソッド__bool__()を実装するとその判定処理を変更することができる。
#次のQueryParamsクラスは、保持している辞書の評価結果を、自分自身の評価結果として返している。

class QueryParams:
    def __init__(self, params):
        self.params = params
    def __bool__(self):
        return bool(self.params)

query = QueryParams({})
bool(query)
# => False
query = QueryParams({'key':'value'})
bool(query)
# => True

#__bool__()を実装すると真理値評価の結果を制御できるが、真理値評価に影響する特殊メソッドは__bool__()だけではない。__bool__()を実装せずに__len__()が0を返すと、そのオブジェクトは偽になる。上記のQueryParamsクラスも__bool__()を削除し、代わりに__len__()を実装しても同じ結果を得ることができる。

class QueryParams:
    def __init__(self, params):
        self.params = params
    def __len__(self):
        return bool(self.params)

#__len__()が0なので偽になる
bool(QueryParams({}))
# => False


#__call__()：インスタンスを関数のように扱う
#__call__()を実装したクラスでは、インスタンスを関数のように呼び出すことができる。関数との主な違いは、インスタンスであれば状態を保持できる点である。
#インスタンス変数を使って、呼び出し時に利用する共通のパラメータや設定情報を呼び出したり、呼び出し回数や結果などを保持できる。

class Adder:
    def __init__(self):
        self._values = []
    def add(self, x):
        self._values.append(x)
    def __call__(self):
        return sum(self._values)

adder = Adder()
adder.add(1)
adder.add(3)
adder()
# => 4
adder.add(5)
adder()
# => 9

#Pythonの関数オブジェクト一覧には属性__call__があり、関数オブジェクトの実体が__call__()を実装したfunctionクラスのインスタンスであることがわかる。__call__()はPythonをバックグラウンドで支えている機能の1つでもある。


"""属性への動的アクセス"""
#Pythonは動的型付き言語なので、プログラムの実行中にオブジェクトの属性を追加したり、削除できたりする。これらが可能なメソッドをうまく活用すると、コード量を大幅に削減することができる。ただし、使いすぎるとコードの可読性や保守性が損なわれるので注意が必要である。

#__setattr__()：属性への代入で呼び出される
#__setattr__()は、p.x = 1などの属性への代入で呼ばれる特殊メソッドである。この場合は__setattr__()の第2引数に'x'が、第3引数に1が渡されて呼び出される。
#次の例では__setattr__()を活用し、属性の代入を属性名で制限している。

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __setattr__(self, name, value):
        if name not in ('x', 'y'):
            raise AttributeError('Not allowed')
        super().__setattr__(name, value)

p = Point(1, 2)
p.z = 3

p.x = 3
p.x  # => 3

#__setattr__()の内部でself.x = 1 と書くと、__setattr__()　が再度呼ばれるため無限ループとなり例外RecursionErrorが発生する。このため、__setattrの内部で自分自身に属性を追加する際には、必ず組み込み関数super()を使って基底クラスの__setattr__()を呼び出す。


#__delattr__()：属性の削除で呼び出される。
#__delattr__()は、属性の削除で呼び出される。それ以外は__setattr__()と同じである。
#下記の例では、属性名を見て削除の実行を制限している。
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __delattr__(self, name):
        if name in ('x', 'y'):
            raise AttributeError('Not allowed')
        super().__delattr__(name)

p = Point(1, 2)
del p.x


#__getattr__(),  __getattribute__()：属性アクセスで呼び出される
#__getattr__(), __getattribute__()は、どちらもp.xのような属性アクセスで呼び出され、第2引数に属性名'x'が渡される。両者の挙動には違いがあり、それを理解するためには、Pythonオブジェクトが持つ属性__dict__について知る必要がある。
class Point:
    pass

p = Point()
p.__dict__  # => {}

#p.__dict__['x'] = 1 に変換される
p.x = 1
p.__dict__  # => {'x':1}

#__dict__は直接書き込み可能
p.__dict__['y'] = 2
p.y  # => 2

# 属性辞書__dict__には代入された属性が格納されている。インスタンスの名前空間の実態はこの辞書であり、属性の参照時にはまずこの辞書から検索が行われる。
#__getattr__()と__getattribute__()の違い
#__getattr__()は属性アクセス時に対象の名前が属性辞書__dict__に存在しない場合にのみ呼ばれ、__getattribute__()は全ての属性アクセスで呼び出される。これたの特殊メソッドを利用すると、実際にはインスタンスが持っていない属性でもあたかもその属性を持っているかのように振る舞いを定義することができる。
#下記の例では、設定ファイルの情報をインスタンス属性のように参照する。
#設定ファイル：config.json
#この設定ファイルを扱うクラスを作成する。インスタンスconfは属性urlを持っていないが、conf.urlのようにアクセスされると設定ファイルに記載された値を返す。
import json

class Config:
    def __init__(self, filename):
        self.config = json.load(open(filename))
    def __getattr__(self, name):
        if name in self.config:
            return self.config[name]
        #存在しない設定値へのアクセスはエラーとする
        raise AttributeError()

conf = Config('config.json')
conf.url   # => 'https://api.github.com/'



"""イテラブルなオブジェクトとして振る舞う"""
#イテラブルなオブジェクトを一言で表すと、for文や内包表記で使えるオブジェクトである。ユーザー定義のクラスでも特殊メソッド__iter__()を実装すると、イテラブルとして利用できる。

#__iter__()：イテレータオブジェクトを返す
#for i in x と書いたとき、for文はxの__iter__()を呼び出し、その戻り値を利用する。この戻り値はイテレータと呼ばれるオブジェクトであり、__iter__()と__next__()の両方が実装されている。

#次のIterableクラスは、__iter__()を実装し、その戻り値がイテレータになっているためfor文や内包表記で利用できる。
#__iter__()の内部では、組み込み関数iter()を利用して、組み込み関数range()によって作成されたオブジェクトの__iter__()を呼び出している。つまり、このクラスが返すイテレータは組み込み関数range()が返すイテレータとなるので、range()と同じように動作する。

class Iterable:
    def __init__(self, num):
        self.num = num
    def __iter__(self):
        return iter(range(self.num))

[val for val in Iterable(3)]
# => [0,1,2]


#__next__()：次の要素を返す
#特殊メソッドの__iter__()と__next__()を実装したオブジェクトをイテレータと呼ぶ。イテレータ__iter__()の戻り値は,必ずそのイテレータ自身とする。
#__next__()はループのたびに呼ばれ、その戻り値がfor i in x　のiに渡される。__next__()で返す値がなくなった際には、例外StopIterationを送出してループを終了させる。
#なお、組み込み関数next()にイテレータを渡すと、そのイテレータの__next__()が呼び出され、その戻り値をそのままnext()の戻り値として受け取ることができる。

#次のReverserクラスは、引数のオブジェクトを逆順にして返すイテレータである。イテレータは必ず自分自身を返す__iter__()を実装しているので、イテラブルなオブジェクトとしても利用できる。

class Reverser:
    def __init__(self, x):
        self.x = x
    def __iter__(self):
        return self
    def __next__(self):
        try:
            return self.x.pop()
        except IndexError:
            raise StopIteration()

[val for val in Reverser([1,2,3])]
# => [3,2,1]

#イテラブルとイテレータは違う概念であることに注意。イテレータは必ずイテラブルであるが、イテラブルはイテレータとは限らない。
#イテラブル：
    #__iter__()を実装したオブジェクト
    #__iter__()の戻り値は任意のイテレータ
#イテレータ：
    #__iter__()と__next__()を実装したオブジェクト
    #__iter__()の戻り値は自分自身(self)




        

