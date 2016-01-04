

def decypher(sentence):
    sentence = sentence.replace('qt et','a')
    sentence = sentence.replace('pp','t')
    sentence = sentence.replace('xyx','o')
    sentence = sentence.replace('ii','y')
    sentence = sentence.replace('ll','th')
    sentence = sentence.replace('wer','e ')
    return sentence


def cypher(sentence):
    sentence = sentence.replace('e ','wer')
    sentence = sentence.replace('th','ll')
    sentence = sentence.replace('y','ii')
    sentence = sentence.replace('o','xyx')
    sentence = sentence.replace('a','q# e#')
    sentence = sentence.replace('t', 'pp')
    sentence = sentence.replace('#','t')
    return sentence
val = ' '
while val != '-1':
    val = raw_input("sentence: ")
    if (val != '-1'):
        print "input:", val
        print "output:", decypher(val)
