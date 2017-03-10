import io
import xlsxwriter
from datetime import date
from urllib.request import urlopen

# ================= пример создания простой книги =============
workbook = xlsxwriter.Workbook('hello.xlsx')
day_format = workbook.add_format({'num_format': 'yyyy-mm-dd'})

worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Hello world')
# ================= форматы =============
worksheet.write('B1', date(2017, 3, 9), day_format)
worksheet.set_column(1, 1, 15)
worksheet.write('C1', date(2017, 3, 9))
worksheet.set_column(2, 2, 15, day_format)

# ================== Вставка картинки =============
# worksheet.insert_image('B10', 'logo-icon-big.png')

# ================== Вставка картинки по URL =============
# url = 'https://deutscheam.com/globalassets/siteresources/img/logo-icon-big.png'
# image_data = io.BytesIO(urlopen(url).read())
# worksheet.insert_image(
#     'B10',
#     'logo-icon-big.png',
#     {
#         'x_offset': 10,
#         'y_offset': 10,
#         'x_scale': 3,
#         'y_scale': 3,
#         'url': 'http://db.com',
#         'tip': 'DB LOGO',
#         'image_data': None,
#         'positioning': None,
#     }
# )


# ================== Вставка диаграммы =============
# worksheet2 = workbook.add_worksheet('series')
# worksheet2.write(0, 0, 'x')
# worksheet2.write(0, 1, 's1')
# worksheet2.write(0, 2, 's2')
# for i in range(10):
#     worksheet2.write(i+1, 0, i)
#     worksheet2.write(i+1, 1, (i*i*17+4) % 13)
#     worksheet2.write(i+1, 2, (i*i*17+11) % 15)
#
# chart = workbook.add_chart({'type': 'column'})
#
# chart.add_series({
#     'categories': '=series!$A$2:$A$11',
#     'values': '=series!$B$2:$B$11',
#     'name': 's1'
# })
# chart.add_series({
#     'categories': '=series!$A$2:$A$11',
#     'values': '=series!$C$2:$C$11',
#     'name': 's2'
# })
# worksheet2.insert_chart('E1', chart)
# worksheet2.activate()

# ================== объединение ячеек ===========
# worksheet.merge_range('B3:D4', 'Merged Cells')

# ================== автофильтр ===========
# worksheet.write('A2', 'row1')
# worksheet.write('B2', 'row2')
# for x in range(8):
#     worksheet.write(x+2, 0, x)
#     worksheet.write(x+2, 1, x % 5)
# worksheet.autofilter('A2:B10')

# ================== закрепление областей ===========
# worksheet.freeze_panes(2, 1)


workbook.close()
