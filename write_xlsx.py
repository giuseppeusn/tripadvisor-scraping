from xlwt import Workbook, Font, XFStyle
import os

def write_headers(num_comments):
    global wb, sh
    wb = Workbook()
    sh = wb.add_sheet('Sheet 1')
    sh.col(3).width = 12000
    sh.col(8).width = 9000

    header_font = Font()
    header_font.bold = True

    header_style = XFStyle()
    header_style.font = header_font

    sh.write(0, 0, 'Nome', header_style)
    sh.write(0, 1, 'Nota', header_style)
    sh.write(0, 2, 'Avaliações', header_style)
    sh.write(0, 3, 'Serviços', header_style)

    if num_comments:
        sh.write(0, 5, 'Nome cliente', header_style)
        sh.write(0, 6, 'Título avaliação', header_style)
        sh.write(0, 7, 'Avaliação', header_style)
        sh.write(0, 8, 'Data estadia', header_style)

def write_reviews(title, score, avaliacoes):
    sh.write(1, 0, title)
    sh.write(1, 1, score)
    sh.write(1, 2, avaliacoes)

def write_services(services):
    for i, service in enumerate(services):
        sh.write(i + 1, 3, [service.get_attribute("innerText")])

def write_comments(comments):
    for i, comment in  enumerate(comments):
        sh.write(i + 1, 5, comment["name"])
        sh.write(i + 1, 6, comment["title"])
        sh.write(i + 1, 7, comment["review"])
        sh.write(i + 1, 8, comment["date"])

def save_file(name_file):
    if not (os.path.exists('./data')):
        os.mkdir('./data')

    wb.save(f'./data/{name_file}.xls')