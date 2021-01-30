from textblob import TextBlob

'''
CC coordinating conjunction
CD cardinal digit
DT determiner
EX existential there (like: “there is” … think of it like “there exists”)
FW foreign word
IN preposition/subordinating conjunction
JJ adjective ‘big’
JJR adjective, comparative ‘bigger’
JJS adjective, superlative ‘biggest’
LS list marker 1)
MD modal could, will
NN noun, singular ‘desk’
NNS noun plural ‘desks’
NNP proper noun, singular ‘Harrison’
NNPS proper noun, plural ‘Americans’
PDT predeterminer ‘all the kids’
POS possessive ending parent‘s
PRP personal pronoun I, he, she
PRP$ possessive pronoun my, his, hers
RB adverb very, silently,
RBR adverb, comparative better
RBS adverb, superlative best
RP particle give up
TO to go ‘to‘ the store.
UH interjection errrrrrrrm
VB verb, base form take
VBD verb, past tense took
VBG verb, gerund/present participle taking
VBN verb, past participle taken
VBP verb, sing. present, non-3d take
VBZ verb, 3rd person sing. present takes
WDT wh-determiner which
WP wh-pronoun who, what
WP$ possessive wh-pronoun whose
WRB wh-abverb where, when
'''


def parse(sentence):
    taglist = []
    wordlist = []
    question = ''
    sentenceblob = TextBlob(sentence)
    sentenceblobtags = sentenceblob.tags
    for xyz in sentenceblobtags:
        a, b = xyz
        taglist.append(b)
        wordlist.append(a)
    if taglist[0] == 'NNP' and wordlist[1] == 'is':
        question = 'Who ' + wordlist[1]+' '+wordlist[0]+' '+'?             '
    if taglist[0] == 'NNP' and wordlist[1] == 'is' and taglist[2] == 'JJ':
        question += 'What is quality of ' + wordlist[0]+' '+'?             '
    if taglist[0] == 'NN' and wordlist[1] == 'is':
        question += 'What' + taglist[1] + taglist[0]
    if taglist[0] == 'WRB':
        question = ''
    return question


def loaddata(parag):
    questionlist = []
    para = TextBlob(parag)
    for senty in para.sentences:
        questionlist.append(parse(str(senty)))
    return questionlist


parag = input("Enter a paragraph:\n")
print(loaddata(parag))
