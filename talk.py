import random
import sys
args = sys.argv

word = ["have", "go", "make", "put", "take", "get", "good", "morning",
    "after", "before", "hello", "world", "night", "Hi", "Hey", "what",
    "where", "who", "when", "How", "to", "fine", "bad", "great", "Bye", "Uh",
    "Sorry", "?", "!", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
    "know", "absolutely", "take", "easy", "difficult", "can", "do", "that",
    "will", "going", "i", "my", "me", "mine", "you", "your", "yours",
    "he", "him", "his", "she", "her", "hers", "they", "their", "them",
    "we", "our", "us", "am", "was", "are", "were", "is", "be", "been",
    "better", "than", "the", "this", "most", "more", "2525", "niconico", "video", "ひろゆき",
    "Japan", "United", "Kingdom", "State", "test"]

if args[1] == "random":
    random_num = int(args[2])
    sentence = random.randint(1,random_num)

elif args[1] == "normal":
    sentence = int(args[2])

elif args[1] == "crazy":
    sentence = len(args[2])

else:
    sys.exit("this mode is not setting...")    

random_list = random.choices(word, k=sentence)
print("sentence",sentence)
print(random_list)    