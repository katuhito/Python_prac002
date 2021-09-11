from typing import Optional

def increment(page_num: int, last: int, *, ignore_error: bool = False) -> Optional[int]:
    """次ページの番号を返す
    
    :param page_num: 元のページの番号
    :param last: 最終ページの番号
    :param ignore_error: Truの場合ページのオーバーで例外を送出しない
    :return ignore_error: 次のページの番号
    """

    next_page = page_num + 1
    if next_page <= last:
        return next_page
    if ignore_error:
        return None
    raise ValueError("Invalid arguments")

increment(1, 10, ignore_error=1)
