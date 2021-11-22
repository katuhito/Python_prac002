"""ジェネレータ"""
#メモリ効率の良いイテラブルなオブジェクト
#ジェネレータは、リストやタプルのように、for文で利用できるイテラブルナオブジェエクトである。リストやタプルは、全ての要素をメモリ上に保持するため、要素数が増えれば増えるほどメモリの消費量も増える欠点がある。
#これに対して、ジェネレータは、次の要素が求められるたびに新たな要素を生成して返すことができる。つまり、要素数にかかわらずメモリ使用量を小さく保つことができる。
#例えば、値を無限に返し続けるジェネレータinfを作成する場合。ジェネレータinfは通常の関数に見えるが、内部にあるyield式がジェネレータの目印である。このジェネレータをfor文で使用すると、引数に渡した値を無限に返し続ける。
#要素を無限に返すこの動きは、全ての要素をメモリに保持するリストやタプルでは実現できないものである。

#yieldを含む関数はジェネレータになる。
from _typeshed import StrPath
from os import stat_result


def inf(n):
    while True:
        yield n

#Ctrl+cで中断できる
for i in inf(3):
    print(i)

#ジェネレータの実装
#ジェネレータの作成方法は2つある。1つはジェネレータ関数を使う方法、もう一つはジェネレータ式を使う方法である。

#ジェネレータの関数
#ジェネレータ関数とは、内部でyield式を使っている関数のことを呼ぶ。ジェネレータ関数の戻り値は、ジェネレータイテレータと呼ばれるイテレータである。このイテレータは特殊メソッド__next__()が呼ばれるたびに、関数内の処理が次のyield式まで進む。そして呼び出し元にyield式に渡した値を返すと、そのときの状態を保持したまま、その行で処理を中断する。再度特殊メソッド__next__()が呼ばれると、次の行から処理が再開され、関数を抜けると自動でStopIterationが送出される。
def gen_function(n):
    print('start')
    while n:
        print(f'yield: {n}')
        yield n  #ここで1次中断される
        n -= 1

#戻り値はジェネレータイテレータ
gen = gen_function(2)
gen

#組み込み関数next()に渡すと__next__()が呼ばれる
next(gen)
# stat
# yield: 2
# 2  #これがnext(gen)の戻り値

next(gen)
# yield: 1
# 1

next(gen)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

#内包表記での利用
[i for i in gen_function(5)]
# start
# yield: 5
# yield: 4
# yield: 3
# yield: 2
# yield: 1
# [5, 4, 3, 2, 1]

#イテラブルを受け取る関数に渡す
max(gen_function(5))
# start
# yield: 5
# yield: 4
# yield: 3
# yield: 2
# yield: 1
# 5


#ジェネレータ式：内包表記を利用して作成する
#リストやタプルなどのイテラブルがあるときは、内包表記を用いてイテラブルからジェネレータを作成することができる、これはジェネレータ式と呼ばれ、リスト内包表記と同じ構文で[]の代わりに()を使う。
x = [1,2,3,4,5]

#これはリスト内包表記
listcomp = [i**2 for i in x]
listcomp  #全ての要素がメモリ上にすぐ展開される
#[1,4,9,16,25]

#これはジェネレータ式
gen = (i**2 for i in x)
gen  #各要素は必要になるまで計算されない

#リストにすると最後の要素まで計算される
list(gen)
#[1,4,9,16,25]

#関数の呼び出し時に渡したい引数がジェネレータ式ひとつだけの場合は、内包表記の()を省略できる
x = [1,2,3,4,5]
#max((i**3) for i in x))と等価
max(i**3 for i in x)
#125


#yield from式：サブジェネレータへ処理を委譲する
#ジェネレータ内部でさらにジェネレータを作成できる場合、yield from式を使うと簡潔に書き直せることがある。
#次のコードのchain()関数は、複数のイテラブルを連続した1つのイテラブルに変換するジェネレータである。
def chain(iterables):
    for iterable in iterables:
        for v in iterable:
            yield v

iterables = ('python', 'book')
list(chain(iterables))
#['p', 'y', 't', 'h', 'o', 'n', 'b', 'o', 'o', 'k']

#chain()関数の最後の2行は、ジェネレータ式に置き換えができる。ジェネレータ式に置き換えてyield from式を合わせて使うと、次のように書き直すことができる。
def chain(iterables):
    for iterable in iterables:
        yield from (v for v in iterable)

list(chain(iterables))
#['p', 'y', 't', 'h', 'o', 'n', 'b', 'o', 'o', 'k']


#ジェネレータを利用する際の注意点
#ジェネレータは、リストやタプルと同じくいイテラブルとして使うことができる。例えば、組み込み関数のzip()やfilter()は、ジェネレータを渡しても問題なく動作する。
def gen(n):
    while n:
        yield n 
        n -= 1

#zip()にリストとジェネレータを同時に渡す
x = [1,2,3,4,5]
[i for i in zip(x, gen(5))]
#[(1,5),(2,4),(3,3),(4,2),(5,1)]

#filter()にジェネレータを渡す
odd = filter(lambda v: v%2 == 1, gen(5))
[i for i in odd]
#[5,3,1]

#len()で利用する場合
#リストやタプルでよく利用される組み込み関数len()は、ジェネレータでは利用できない。そのためジェネレータをリストやタプルに変換して利用する
len(list(gen(5)))
#5

#巨大やジェネレータや値を無限に返すジェネレータをリストやタプルに渡すと、メモリを圧迫したり、無限ループが発生したりするので注意が必要である。
#値を無限に返すジェネレータ
g = gen(-1)

#リストやタプルへの変換は無限ループになる（Ctrl+cで中断できる）
list(g)

#len()を複数回利用する場合
#ジェネレータは、状態を保持する点に注意
g = gen(4)
len(list(g))
#4
len(list(g))
#0
#ここでは1回目のlen(list(g))で最後まで到達しているので、2回目以降の結果は常に0になる。同じジェネレータを何度も利用したい場合には、次のようにリストやタプルに変換したものを保持する。ただし、返還後のリストやタプルのサイズによってはメモリを圧迫するために注意が必要である。
list_nums = list(gen(4))
len(list_nums)
#4
len(list_nums)
#4



#ジェネレータの実例
#ジェネレータの実例=>ファイルの中身を大文字に変換するプログラム
#=> ファイルを1行ずつ読み込むジェネレータ関数reader()を作成し、その戻り値をwrite()関数に渡す。write()関数は、受け取ったイテレータを利用してファイルを1行筒読み込み、convert()関数で変換しながら、結果を新しいファイルに1行ずつ書き込んでいく。
#読み込み=>変換=>書き込みの一連の流れを1行ずつ行うため、元のファイルサイズが大きくてもメモリを圧迫することなく動作する。

#ファイルの中身を1行づつ読み込む
def reader(src):
    with open(src) as f:
        for line in f:
            yield line

#行単位で実行する変換処理
def convert(line):
    return line.upper()

#読み込み=>変換=>書き込みを1行ずつ行う
def writer(dest, reader):
    with open(dest, 'w') as f:
        for line in reader:
            f.write(convert(line))

#reader()には存在するファイルのパスを渡す
writer('dest.txt', reader('src.txt'))





