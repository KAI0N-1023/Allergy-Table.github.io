import gspread
from google.oauth2.service_account import Credentials
# お決まりの文句
# 2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
#ダウンロードしたjsonファイル名をクレデンシャル変数に設定。
credentials = Credentials.from_service_account_file("C:\\Users\\いわせ　かいと\\Desktop\\課題研究改訂版\\kadaikenkyuu-ba9b9a469932.json", scopes=scope)
#OAuth2の資格情報を使用してGoogle APIにログイン。
gc = gspread.authorize(credentials)
#スプレッドシートIDを変数に格納する。
SPREADSHEET_KEY = '1p5-udDmIwLrUWrFiBH-FuK7AvFCoGg0ZbQyMPOPHU4Q'
# スプレッドシート（ブック）を開く
workbook = gc.open_by_key(SPREADSHEET_KEY)

workbook = workbook.worksheet('シート１')

worksheets = workbook.worksheet('シート１')

print(worksheets)

worksheet = workbook.worksheet('シート１')

worksheet.update_cell(2, 1, "test_value")