def increment(page_num, last, *, ignore_error=False):
    """"次のページ番号を返す
        :param page_num: 元のページの番号
        :type page_num: int
        :param last: 最終ページの番号
        :type last: int
        :param ignore_error: Trueの場合ページのオーバーで例外を送出しない
        :type ignore_error: bool
        :rtype: int
    """

    next_page = page_num + 1
    if next_page <= last:
        return next_page
    if ignore_error:
        return None
    raise ValueError('Invalid arguments')