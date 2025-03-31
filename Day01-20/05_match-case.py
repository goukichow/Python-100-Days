status_code = input('请输入HTTP响应状态码：')
match status_code:
    case '401' | '403' | '404':
        description = 'Not Allowed'
    case '400' | '405':
        description = 'Invalid Request'
    case '404':
        description = 'Not Found'
    case _:
        description = 'Unknown Error'
print('状态码描述: ', description)
