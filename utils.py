from datetime import datetime


def commit_errors(erro):
    print(f'ERROR: {erro} -- {datetime.now().strftime("%H:%M:%S")}')
    try:
        with open(f'{BASE_DIR}/.seln.log', 'a') as logging:
            logging.writelines(f'ERROR: {erro} -- {datetime.now().strftime("%H:%M:%S")}\n')
    except Exception as err:
        raise(erro)