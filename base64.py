# print('imported my base64.py')

"""importにおけるPythonのモジュール検索順序優先度
   1：ビルトインモジュール
   2：カレントディレクトリのモジュール
   3：ビルトインモジュール以外の標準ライブラリ
   =>モジュールがimportされない原因のひとつに、カレントディレクトリに同じ名前の
   モジュールが存在して、コンフリクトを起こしている場合がある。自作のみジュールなど
   を作成するときには、この名前の違いに気を付けておく。
"""