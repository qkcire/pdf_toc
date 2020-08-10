import os
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

def extract_toc_from_pdf(pdf, page_begin, page_end):
    pdf_object = PdfFileReader(pdf)
    for i in range(page_begin, page_end + 1):
        create_pdf_from_toc(pdf_object.getPage(i))
        # transform_toc_to_txt(pdf_object.getPage(i))

def create_pdf_from_toc(pdf_obj):
    pdf_merger = PdfFileMerger()
    for path in pdf_obj:
        pdf_merger.append(path)
    with open("toc.pdf", 'wb') as fileobj:
        pdf_merger.write(fileobj)


def transform_toc_to_txt(pdf_toc_page):
    text_file = open("toc.txt", "a")
    text_file.write(pdf_toc_page.extractText() + "\n")

def pdf_toc(arg_list):
    pdf = arg_list[0]
    toc_page_begin = int(arg_list[1])
    toc_page_end = int(arg_list[2])
    extract_toc_from_pdf(pdf, toc_page_begin, toc_page_end)

if __name__ == '__main__':
    cmnd_line_arg_list = []
    for arg in sys.argv[1:]:
        cmnd_line_arg_list.append(arg)
    pdf_toc(cmnd_line_arg_list)