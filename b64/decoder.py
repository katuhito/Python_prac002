import base64
import sys

def base64_to_str(x):
    """base64表現を文字列に変換する
       b64decode()の戻り値はbytes型であるため
       decode()で文字列にしてから返す"""
    
    return base64.b64decode(x).decode('utf-8')

def main():
    target = sys.argv[1]
    print(base64_to_str(target))

if __name__ == '__main__':
    main()