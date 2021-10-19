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


