import base64
import sys

def str_to_base64(x):
    """文字列をbase64表現に変換する
       
       b64encode()はbytes-like objectを引数に取るため
       文字列はencode()でbyte型にして渡す
    """
    return base64.b64decode(x.encode('utf-8'))

# print(str_to_base64('pyth')) #4文字毎に変換

# target = sys.argv[1]
# print(str_to_base64(target))

def main():
    target = sys.argv[1]
    print(str_to_base64(target))

if __name__ == '__main__':
    main()

"""if __name__ == '__main__':ブロックの意味
   
   if __name__ == '__main__':の行が、モジュールをスクリプトとして利用したい場合に記述する
   Pythonのイディオムである。
   Pythonでは、モジュールをインポートしたり、スクリプトとしてpython3コマンドに渡した際には、
   そのファイルのトップレベルのコードが上から順に実行される。
   つまり、python3 encoder.py bookを実行すると次のようになる。

    1：base64モジュールをインポートする
    2：sysモジュールをインポートする
    3：str_to_base64()関数が定義される
    4：main()関数が定義される
    5：if文の条件式__name__ == '__main__'が評価され、真となる
    6：main()関数を呼び出す
    7：引数から変換対象の文字列を取得する(book)
    8：変換対象の文字列を渡してstr_to_base64()関数を実行した結果を出力する

   __name__ == '__main__'の評価結果が真となっているのは、Pythonが暗黙的に定義している変数
   __name__によって決められているからである。
   つまり、あるモジュールがpython3コマンドに渡されたとき、そのモジュール内の変数__name__の値
   は、文字列__main__になっている。
   このファイルのファイル名が文字列'__main__'と同じ名前ならば、main()関数を呼び出して実行しま
   すよ。という意味でプログラムの末尾に設定してある。モジュールのモジュール名でも同じ。
   ファイル内で先にインポートされたモジュールが先に勝手に実行されないように
   プログラムの最後にif文の条件式__name__ == '__main__'で真偽判定をして、真の判定で初めて
   ファイルが実行されるようにしている。
   (Pythonはインタプリタ仕様なので、先に実行されてしまうのを防いでいる。)

"""



