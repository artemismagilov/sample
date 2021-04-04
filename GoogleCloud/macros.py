import locale
import apiclient
import httplib2
import sys
from oauth2client.service_account import ServiceAccountCredentials


def reformat(s):
    ss = s.strip().split('\n')
    tb = [i.strip().split('\t') for i in ss]
    length = max(max(len(w) for w in words) for words in tb) + 4
    return '\n'.join(''.join(f'{w:{length}}' for w in words) for words in tb)


def add_args(args: list):
    if len(args) == 3:
        return '!'.join(args[1:3])
    print('Вы не ввели аргументы в командной строке, поэтому страница(Лист1!) и промежуток(A1:C7) по умолчанию')
    return 'Лист1!A1:C7'


locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
CREDENTIALS_FILE = 'подставить имя скаченного файла с закрытым ключом'  # 1← имя скаченного файла с закрытым ключом
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                               ['https://www.googleapis.com/auth/spreadsheets',
                                                                'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

spreadsheetId = 'подставить id из ссылки вашей таблицы'  # 2← имя id из ссылки вашей таблицы
range_name = add_args(sys.argv)
table = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=range_name).execute()
lines = table['values']

with open(file='report.txt', mode='w', encoding='utf-8') as f:
    strings = ''
    for line in lines:
        if '' in line:
            continue
        strings += '\t'.join(line)+'\n'
    f.write(reformat(strings))
