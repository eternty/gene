from __future__ import print_function
from string import ascii_lowercase
from random import choice, randint

def get_sentence():
    sentence = input("Input the sentence:")
    sentence = sentence.lower()
    sentence = [x for x in sentence if x in ascii_lowercase + " "]
    sentence = "".join(sentence)
    # print("What have we received after filtering:", sentence)
    return sentence

def random_str(str_len):
    out_str = []
    for i in range(0, str_len):
        out_str.append(choice(ascii_lowercase + " "))
    out_str = "".join(out_str)
    return out_str

def create_population(max_population,sentence,generation):
    for i in range(max_population):
        random = random_str(len(sentence))
        # print(random)
        generation.append(random)
    return generation

def print_list(list_to_print):
    for x in list_to_print: print(x)

def isPresent(sentence, generation):
  selection_word = sentence
  if selection_word in generation:
    return True
  else:
    return False

def crossingover( max_population, generation):

   my_length = len(my_sentence)
   if my_length >3:
       for k in range(0, len(generation)-2, 3):
            parent1 = generation[k]
            parent2 = generation[k + 1]

            #print('my_length ', my_length)
            break_index1 = choice(range(1, my_length - 2))
            break_index2 = choice(range(break_index1+1, my_length - 1))

            '''print('break1: %s break2: %s', break_index1, break_index2)
            print('1:%s 2:%s', parent1[:break_index1+1], parent2[break_index1:break_index2])
            print(' 2:%s',parent2[break_index1:break_index2])'''

            child1 = parent1[:break_index1+1] + parent2[break_index1+1:break_index2+1] + parent1[break_index2+1:]
            child2 = parent2[:break_index1+1] + parent1[break_index1+1:break_index2+1] + parent2[break_index2+1:]
            #print(child1)
            generation.append(child1)
            #print(child2)
            generation.append(child2)
       else:
           for i in range(0, max_population, 2):
                mother = generation[i]
                father = generation[i + 1]
                break_index = choice(range(1, len(my_sentence) - 1))
                child1 = mother[:break_index]
                child2 = father[:break_index]
                child1 = child1 + father[break_index:]
                child2 = child2 + mother[break_index:]
                generation.append(child1)
                generation.append(child2)


def mutation(generation, probability, my_sentence):
    mutated_count = 0
    for entity in generation:
        if (randint(0, 100) < probability):
            #print("before mutation ", entity)
            mutated_index = choice(range(0, len(my_sentence)))
            mutation_char = str(choice(ascii_lowercase + " "))
            output_str = entity[:mutated_index]
            output_str = output_str + mutation_char + entity[mutated_index+1:]
            #entity = output_str
            generation.remove(entity)
            generation.append(output_str)
            #print("after : ",output_str )
            mutated_count+=1
    return mutated_count

def mutate(gene):
     mutated_index = choice(range(0, len(my_sentence)))
     mutation_char = str(choice(ascii_lowercase + " "))
     output_str = gene[:mutated_index]
     output_str = output_str + mutation_char + gene[mutated_index+1:]
     return output_str

def mismatch(str1):
    mismatch = 0
    for c1,c2 in zip(str1,my_sentence):
        if c1 != c2:
            #print("mismatch" , c1 )
             mismatch += 1
    '''if mismatch == 1:               #direct mutation
        for c1,c2 in zip(str1,sentence):
            if c1 != c2:
                #print("mismatch" , c1 )
                c1 = choice(ascii_lowercase + " ")'''
    return mismatch

def selection():
  filtering()
  print("After filtering: ", generation)
  generation.sort(key = mismatch)
  print("After sorting: ", generation)
  del generation[max_population::]

def filtering():
    a=generation
    for i in range( len( a ) ):
        c=a[i]
        for j in range( len( a ) ):
            if a[j]==c and i<j:  a[j]= mutate(a[j])
            else: pass

my_sentence = get_sentence()
max_population = 50 # max members in first population
generation = []
generation_count = 0
max_num_generations = 6000
probability = 20
create_population(max_population, my_sentence, generation )
for i in range(max_num_generations):
    if (isPresent(my_sentence, generation)):
        print("found")
        # print(generation)
        break
    else:
        generation_count =i+1
        print("Generation  ", generation_count)
        print("Created ", generation)
        crossingover( max_population, generation)

        print("Crossing ", generation)

        mutated_count = mutation(generation, probability, my_sentence)    #amount of mutations
        print("Mutate ", generation)
        selection()
        print("Select ", generation)
        if generation_count > max_num_generations:
            raise Exception("Not reached in the maximal number of generations")
print(generation_count, generation[0])


