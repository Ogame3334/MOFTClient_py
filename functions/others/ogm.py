#Error
def error_output() -> str:
    import traceback, datetime
    now = datetime.datetime.now()
    filename = now.strftime('%Y%m%d_%H%M%S')
    error_text = traceback.format_exc()
    with open('.\\error_log\\' + filename + '.txt', 'w', encoding='UTF-8') as error_massage:
        error_massage.write(error_text)

    return error_text
