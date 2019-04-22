from __future__ import print_function, unicode_literals
from bosonnlp import BosonNLP

nlp = BosonNLP('CvKJONKW.33832.Txk4Jf6Sd3RY')

def bosonnlp(filename):
    file = open('%s'%filename,'r',encoding='utf-8')
    tar_file = open('./test_set/am_phone.true.ch','a+',encoding='utf-8')
    connent = file.readlines()
    for line in connent:
        result = nlp.tag(line)
        for d in result:
            tar_line = ' '.join(['%s' % it for it in d['word']])
            tar_file.write(tar_line+'\n')
    tar_file.close()
    file.close()

if __name__ == "__main__":
    source_file = './test_set/phone.ch.in'
    bosonnlp(source_file)
