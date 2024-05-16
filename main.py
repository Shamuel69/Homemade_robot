import json

sentences = []
ignore_characters = ["?", "!", ".", ","]

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
    # stink = input("What would you like to say?\n\nYou >")
    # print(Lemmitizer(stink).Tokenized)
    listed = """Hate
Pain
Sorrow
Grief
Misery
Sadness
Anguish
Despair
Agony
Loneliness
Isolation
Rejection
Abandonment
Heartbreak
Disappointment
Frustration
Annoyance
Irritation
Resentment
Bitterness
Hostility
Animosity
Enmity
Hatred
Contempt
Disgust
Revulsion
Aversion
Dislike
Disdain
Scorn
Ridicule
Mockery
Derision
Insult
Offense
Injury
Harm
Hurt
Pain
Suffering
Torment
Affliction
Misfortune
Hardship
Difficulty
Trouble
Struggle
Adversity
Crisis
Disaster
Catastrophe
Tragedy
Calamity
Ruin
Destruction
Devastation
Ruination
Collapse
Failure
Defeat
Loss
Ruin
Decline
Deterioration
Degradation
Decay
Disintegration
Decomposition
Dissolution
Breakdown
Demise
Death
Departure
End
Finale
Conclusion
Termination
Closure
Exit
Withdrawal
Abandonment
Rejection
Neglect
Desertion
Betrayal
Deception
Fraud
Cheating
Lies
Deceit
Dishonesty
Betrayal
Treachery
Infidelity
Unfaithfulness
Fraudulence
Corruption
Manipulation
Exploitation
Abuse
Violence
Aggression
Hostility
Conflict
Confrontation
Argument
Quarrel
Dispute
Feud
Battle
War
Strife
Contest
Rivalry
Competition
Hatred
Enmity
Contention
Jealousy
Envy
Covetousness
Greed
Avarice
Gluttony
Lust
Desire
Craving
Addiction
Obsession
Compulsion
Dependency
Attachment
Possession
Clinginess
Dependency
Neediness
Desperation
Begging
Pleading
Imploring
Supplication
Beseeching
Begging
Pleading
Imploring
Supplication
Beseeching
Dependency
Neediness
Desperation
Futility
Hopelessness
Despair
Helplessness
Powerlessness
Vulnerability
Fragility
Weakness
Insecurity
Uncertainty
Doubt
Skepticism
Cynicism
Pessimism
Negativity
Defeatism
Resignation
Apathy
Indifference
Passivity
Lethargy
Laziness
Sloth
Inactivity
Stagnation
Stalemate
Impasse
Deadlock
Standstill
Hesitation
Delay
Procrastination
Distraction
Preoccupation
Dilemma
Predicament
Quandary
Conundrum
Puzzle
Mystery
Confusion
Bewilderment
Perplexity
Frustration
Irritation
Annoyance
Anger
Rage
Fury
Wrath
Outrage
Hostility
Hatred
Bitterness
Resentment
Animosity
Spite
Malice
Vengeance
Retaliation
Revenge
Grudge
Antagonism
Conflict
Strife
Discord
Disharmony
Division
Alienation
Estrangement
Separation
Isolation
Loneliness
Solitude
Abandonment
Rejection
Neglect
Betrayal
Deception
Fraud
Cheating
Lies
Deceit
Dishonesty
Betrayal
Treachery
Infidelity
Unfaithfulness
Fraudulence
Corruption
Manipulation
Exploitation
Abuse
Violence
Aggression
Hostility
Conflict
Confrontation
Argument
Quarrel
Dispute
Feud
Battle
War
Strife
Contest
Rivalry
Competition
Hatred
Enmity
Contention
Jealousy
Envy
Covetousness
Greed
Avarice
Gluttony
Lust
Desire
Craving
Addiction
Obsession
Compulsion
Dependency
Attachment
Possession
Clinginess
Dependency
Neediness
Desperation
Begging
Pleading
Imploring
Supplication
Beseeching
Begging
Pleading
Imploring
Supplication
Beseeching
Dependency
Neediness
Desperation
Futility
Hopelessness
Despair
Helplessness
Powerlessness
Vulnerability
Fragility
Weakness
Insecurity
Uncertainty
Doubt
Skepticism
Cynicism
Pessimism
Negativity
Defeatism
Resignation
Apathy
Indifference
Passivity
Lethargy
Laziness
Sloth
Inactivity
Stagnation
Stalemate
Impasse
Deadlock
Standstill
Hesitation
Delay
Procrastination
Distraction
Preoccupation
Dilemma
Predicament
Quandary
Conundrum
Puzzle
Mystery
Confusion
Bewilderment
Perplexity
Frustration
Irritation
Annoyance
Anger
Rage
Fury
Wrath
Outrage
Hostility
Hatred
Bitterness
Resentment
Animosity
Spite
Malice
Vengeance
Retaliation
Revenge
Grudge
Antagonism
Conflict
Strife
Discord
Disharmony
Division
Alienation
Estrangement
Separation
Isolation
Loneliness
Solitude
Abandonment
Rejection
Neglect
Betrayal
Deception
Fraud
Cheating
Lies
Deceit
Dishonesty
Betrayal
Treachery
Infidelity
Unfaithfulness
Fraudulence
Corruption
Manipulation
Exploitation
Abuse
Violence
Aggression
Hostility
Conflict
Confrontation
Argument
Quarrel
Dispute
Feud
Battle
War
Strife
Contest
Rivalry
Competition
Hatred
Enmity
Contention
Jealousy
Envy
Covetousness
Greed
Avarice
Gluttony
Lust
Desire
Craving
Addiction
Obsession
Compulsion
Dependency
Attachment
Possession
Clinginess
Dependency
Neediness
Desperation
Begging
Pleading
Imploring
Supplication
Beseeching
Begging
Pleading
Imploring
Supplication
Beseeching
Dependency
Neediness
Desperation
Futility
Hopelessness
Despair
Helplessness
Powerlessness
Vulnerability
Fragility
Weakness
Insecurity
Uncertainty
Doubt
Skepticism
Cynicism
Pessimism
Negativity
Defeatism
Resignation
Apathy
Indifference
Passivity
Lethargy
Laziness
Sloth
Inactivity
Stagnation
Stalemate
Impasse
Deadlock
Standstill
Hesitation
Delay
Procrastination
Distraction
Preoccupation
Dilemma
Predicament
Quandary
Conundrum
Puzzle
Mystery
Confusion
Bewilderment
Perplexity
Frustration
Irritation
Annoyance
Anger
Rage
Fury
Wrath
Outrage
Hostility
Hatred
Bitterness
Resentment
Animosity
Spite
Malice
Vengeance
Retaliation
Revenge
Grudge
Antagonism"""
msg = ({
    "positive": list[str],
    "negative": list[str]  
})

with open("Datasets/posneg.json", "r") as file:
    json_data = json.load(file)

data = msgspec.json.schema(json_data)

print(data)
