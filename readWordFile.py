import docx2txt

def ReadWordFile(filename):
    return   docx2txt.process(filename)
