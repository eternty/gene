import nltk.data
import sys
from string import ascii_lowercase
from evolution import evolution, print_evolution, print_genes


#nltk.download('punkt')
def split_sentences(text):
  sentence_detector = nltk.data.load('tokenizers/punkt/english.pickle')
  sentences = sentence_detector.tokenize(text.strip())
  print(sentences)
  return sentences

def filter_sentence(sentence):
  sentence = sentence.lower()
  sentence = [x for x in sentence if x in ascii_lowercase+" "]
  sentence = "".join(sentence)
  print("What have we receives after filtering:", sentence)
  return sentence

def process_text(filename):
  text = open(filename,"r").read()
  #text = input("Input please the sentence(s): ")
  sentences = split_sentences(text)
  sentences = [filter_sentence(x) for x in sentences]
  sentences = [x for x in sentences if len(x) > 10]
  return sentences

sentences = process_text("text_data/little.txt")
#sentences = process_text("lf")
for sentence in sentences:
  #print_evolution(sentence)
  print_genes(sentence)
  sys.stdout.flush()


