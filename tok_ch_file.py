from __future__ import print_function, unicode_literals
from bosonnlp import BosonNLP
import jieba
import pynlpir

nlp = BosonNLP('CvKJONKW.33832.Txk4Jf6Sd3RY')
pynlpir.open()

def bosonnlp(content):
    bosonnlp_file = open('./test_set/bosonnlp_pc.true.ch','w',encoding='utf-8')
    for line in content:
        result = nlp.tag(line)
        for d in result:
            tar_line = ' '.join(['%s' % it for it in d['word']])
            temp = str.lower(tar_line)
            bosonnlp_file.write(temp+'\n')
    bosonnlp_file.close()
    print('--------bosonnlp finish !----------')

def jieba_text(content):
    jieba_file = open('./test_set/jieba_pc.true.ch', 'w', encoding='utf-8')
    for line in content:
        seg_list = jieba.cut(line)
        temp = ' '.join(seg_list)
        tar_line = str.lower(temp)
        jieba_file.write(tar_line)
    jieba_file.close()
    print('--------jieba finish !----------')

def nlpir(content):
    nlpir_file = open('./test_set/nlpir_pc.true.ch', 'w', encoding='utf-8')
    for line in content:
        seg_line = pynlpir.segment(line, pos_tagging=False)
        temp = ' '.join(seg_line)
        tar_line = str.lower(temp+'\n')
        nlpir_file.write(tar_line)
    nlpir_file.close()
    pynlpir.close()
    print('--------nlpir finish !----------')


def fenci(filename):
    file = open('%s' % filename, 'r', encoding='utf-8')
    content = file.readlines()
    bosonnlp(content)
    jieba_text(content)
    nlpir(content)
    file.close()


if __name__ == "__main__":
    source_file = './test_set/tb_pc.true.ch'
    fenci(source_file)
