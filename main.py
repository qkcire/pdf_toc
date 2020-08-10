import os
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

def extract_toc_from_pdf(pdf, page_begin, page_end):
    toc_paths = []
    # split pdf into individual pages containing toc
    pdf_read_obj = PdfFileReader(pdf)
    for page in range(page_begin, page_end + 1):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf_read_obj.getPage(page))
        toc_pdf_filename = 'toc_page_{}.pdf'.format(page)
        toc_paths.append(toc_pdf_filename)
        with open(toc_pdf_filename, 'wb') as out:
            pdf_writer.write(out)
    # merge individual pages into a seperate toc.pdf
    pdf_merge_obj = PdfFileMerger()
    for path in toc_paths:
        pdf_merge_obj.append(path)
    with open('toc.pdf', 'wb') as out:
        pdf_merge_obj.write(out)
    # turn toc.pdf into toc.txt
    toc_pdf_read_obj = PdfFileReader('toc.pdf')
    for i in range(toc_pdf_read_obj.getNumPages()):
        transform_toc_to_txt(toc_pdf_read_obj.getPage(i))
    # clean up / remove individual pages from directory
    for path in toc_paths:
        cmnd = "rm {}".format(path)
        os.system(cmnd)

def transform_toc_to_txt(pdf_toc_page):
    text_file = open("toc.txt", "a")
    text_file.write(pdf_toc_page.extractText() + "\n")

def pdf_toc_to_txt(arg_list):
    pdf = arg_list[0]
    toc_page_begin = int(arg_list[1])
    toc_page_end = int(arg_list[2])
    extract_toc_from_pdf(pdf, toc_page_begin, toc_page_end)

if __name__ == '__main__':
    cmnd_line_arg_list = []
    for arg in sys.argv[1:]:
        cmnd_line_arg_list.append(arg)
    pdf_toc_to_txt(cmnd_line_arg_list)