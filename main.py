import os
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

def extract_toc_from_pdf(pdf, page_begin, page_end):
    pdf_object = PdfFilereader(pdf)
    for i in range(page_begin, page_end + 1):
        transform_toc_to_txt(pdf_object.getPage(i))

def transform_toc_to_txt(pdf_toc_page):
    text_file = open("toc.txt", "a")
    text_file.write(pdf_toc_page.extractText())

def pdf_toc_to_txt(arg_list):
    pdf = arg_list[0]
    toc_page_begin = arg_list[1]
    toc_page_end = arg_list[2]
    extract_toc_from_pdf(pdf, toc_page_begin, toc_page_end)
    transform_toc_to_txt()

if __name__ == '__main__':
    cmnd_line_arg_list = []
    for arg in sys.argv[1:]:
        cmnd_line_arg_list.append(arg)
    pdf_toc_to_txt(cmnd_line_arg_list)