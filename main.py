
sentences = []
ignore_characters = ["?", "!", ".", ","]

#test
class Lemmitizer():
    #words > numbers > most common numbers
    def __init__(self, input:str):
        self.Tokenized = self.word_splitter(input)
        

    def Comma_counter(self, input_text:str, character_location=int, word_setting="spacer"):
        if word_setting=="spacer":
            return input_text[:character_location] + " " + input_text[character_location:]
        
        if word_setting == "manual_split":
            return input_text[:character_location] + input_text[character_location-1:]
            
        
    def word_splitter(self, input_text) -> list:
        punctuation = [".", ";", "!", "?"]

        for characters in input_text:
            if characters == ",":
                if input_text.count(characters) >=2:
                    commas_loc = []
                    for i, word in enumerate(input_text):
                        if word == ",":
                            commas_loc.append(i)

                    for num, string in enumerate(commas_loc):
                        try:
                            if commas_loc[num+1]-string <= 15:
                                input_text = self.Comma_counter(input_text, string, word_setting="manual_split")
                        except IndexError:
                            if string-commas_loc[num-1] <= 15:
                                input_text = self.Comma_counter(input_text, string, word_setting="manual_split")

        input_text = input_text.split(",")
        new_sentence=[]
        for words in input_text:
            for punc in punctuation:
                if words.count(punc) >= 1:
                    words = str(words).replace(punc, "")
                new_sentence.append(list(words.split()))
        return new_sentence



    
    

if __name__=='__main__':
    stink = input("What would you like to say?\n\nYou >")
    # print(Lemmitizer(stink).Tokenized)
    print(Lemmitizer(stink).Tokenized)