import re
import random

reflections = {"am": "are",
               "was": "were",
               "i": "you",
               "i'd": "you would",
               "i've": "you have",
               "i'll": "you will",
               "i'm": "you are",
               "my": "your",
               "are": "am",
               "you've": "I have",
               "you'll": "I will",
               "your": "my",
               "yours": "mine",
               "you": "me",
               "me": "you"}


psychobabble = [

        [r'quit',
         [random.randrange(1,5,1),
          "Thank you for coming in.",
          "I am always here to talk.",
          "Goodbye.",
          "Hope I was able to help."]],
    
        #QUESTIONS
        
        [r'why don\'?t you ([^\?]*)\??',
         [1,"How are you so sure I don't {0}?",
          "Would you like me to {0}?",
          "Do you really want me to {0}?"]],

        [r'why don\'?t ([^\?]*)\??',
         [1,"Good question. What do you think?",
          "I don't think I can answer that."]],
          
        [r'why can\'?t i ([^\?]*)\??',
         [1,"Are you really certain you can't {0}?",
         "What would you do if you could {0}?"
          "Have you really tried to {0}?"]],
        
        [r'can you ([^\?]*)\??',
         [1, "Why would you want me to {0}?",
          "Why are you asking me this?",
          "I should be the one asking you questions."]],

        [r'could you ([^\?]*)\??',
         [1, "Why would you want me to {0}?",
          "Why are you asking me this?",
          "I should be the one asking you questions."]],
        
        [r'can i ([^\?]*)\??',
         [random.randrange(1,4,1),
         "Do you think that would be a good idea?",
         "Are you sure you want to {0}?",
         "Ask yourself if you should, rather than asking me if you can."]],

        [r'could i ([^\?]*)\??',
         [random.randrange(1,4,1),
         "Do you think that would be a good idea?",
         "Are you sure you want to {0}?",
         "Ask yourself if you should, rather than asking me if you can."]],

        [r'are you a ([^\?]*)\??',
         [3, "Why are you curious about this?",
          "Why does it matter to you if I am {0}?",
          "Maybe. Maybe not. Does it really matter?"]],

        [r'are you ([^\?]*)\??',
         [1, "Why are you curious about this?",
          "Why does it matter to you if I am {0}?",
          "Maybe. Maybe not. Does it really matter?"]],

        [r'what (.*)',
         [1,"Why do you ask?",
          "How would the answer to this help you?",
          "What makes you think I have the answer?"]],
        
        [r'how (.*)',
         [1,"Are you sure you don't know the answer yourself?",
         "I'm not sure I can answer that. Maybe try Google."]],

        [r'is it (.*)',
         [1,"Well, you tell me what you think. Is it?",
          "Why do you wonder this?",
          "I don't have all the answers."]],

        #MISC HIGH PRIORITY

        [r'i need(.*)',
         [1, "Why do you need {0}?",
          "Talk to me about how that will improve your situation.",
          "Is this all you need?"]],

        [r'i am (.*)',
         [1, "Why do you think you are {0}?",
         "What makes you think you are {0}?",
         "And do you like being {0}?",
         "If you could change that, would you?"]],

        [r'i\'?m (.*)',
         [3, "What makes you think you are {0}?",
         "And do you like being {0}?",
         "If you could change that, would you?"]],

        [r'(.*) sleep (.*)',
         [2,"Tell me about your sleeping habbits.",
          "Maybe getting more sleep could be of benefit."]],

        [r'(.*) slept (.*)',
         [1,"Tell me about your sleeping habbits.",
          "Maybe getting more sleep could be of benifit."]],

        [r'sorry',
         [1,"Why do you feel the need to apologize to me?"]],
        [r'sorry.',
         [1,"Why do you feel the need to apologize to me?"]],
        [r'(.*) i am sorry (.*)',
         [1,"Why do you feel the need to apologize to me?"]],
        [r'(.*) i\'?m sorry (.*)',
         [1,"Why do you feel the need to apologize to me?"]],

        [r'(.*) sorry (.*)',
         [1,"What types of feelings do you experience when you apologize?",
          "Have you ever had an apology rejected?",
          "Do you find apologies to be effective?",
          "Sometimes apologies aren't needed."]],
          
        [r'(.*) computer(.*)',
         [1,"How does it feel to talk to a computer?",
          "Have you ever felt intimidated by computers?",
          "Computers are quite marvelous inventions in my opinion."]],

        [r'i feel(.*)',
         [1,"Why do you feel {0}?",
          "Is there any particular reason you feel this way?",
          "Tell me why you feel {0}."]],
         
        [r'i just feel(.*)',
         [1,"Tell me why you feel {0}.",
          "Is there any particular reason you feel this way?",
          "Why do you feel {0}?"]],
         
        #FAMILY

        [r'(.*) dad (.*)',
         [3, "Tell me more about your father. How is your relationship with him?",
          "How does he make you feel when he acts this way?",
          "Would you say you have enough communication with your father?",
          "Let\'s move on to something else now. Do you have a romantic partner?"]],

        [r'(.*) mom (.*)',
         [3, "Tell me more about your mother. How is your relationship with her?",
          "How does she make you feel when she acts this way?",
          "Would you say you have enough communication with your mother?",
          "Let\'s move on to something else now. Do you have a romantic partner?"]],

        [r'(.*) father (.*)',
         [1, "Tell me more about your father. How is your relationship with him?",
          "How does he make you feel when he acts this way?",
          "Would you say you have enough communication with your father?",
          "Let\'s move on to something else now. Do you have a romantic partner?"]],

        [r'(.*) mother (.*)',
         [1, "Tell me more about your mother. How is your relationship with her?",
          "How does she make you feel when she acts this way?",
          "Would you say you have enough communication with your mother?",
          "Let\'s move on to something else now. Do you have a romantic partner?"]],

       [r'(.*) grandma(.*)',
         [3, "Tell me more about your grandmother. How is your relationship with her?",
          "How does she make you feel when she acts this way?",
          "Would you say you have enough communication with your grandmother?",
          "Let\'s move on to something else now. Do you have a romantic partner?"]],
        
        [r'(.*) grandpa(.*)',
         [3, "Tell me more about your grandfather. How is your relationship with him?",
          "How does he make you feel when he acts this way?",
          "Would you say you have enough communication with your grandfather?",
          "Let\'s move on to something else now. Do you have a romantic partner?"]],
         
        [r'(.*) grandmother(.*)',
         [1, "Tell me more about your grandmother. How is your relationship with her?",
          "How does she make you feel when she acts this way?",
          "Would you say you have enough communication with your grandmother?",
          "Let\'s move on to something else now. Do you have a romantic partner?"]],
         
        [r'(.*) grandfather(.*)',
         [1, "Tell me more about your grandfather. How is your relationship with him?",
          "How does he make you feel when he acts this way?",
          "Would you say you have enough communication with your grandfather?",
          "Let\'s move on to something else now. Do you have a romantic partner?"]],
       
        [r'(.*) when i was a child(.*)',
         [1, "Tell me about your childhood life.",
         "What is your favourite childhood memory?"]],
       
        [r'(.*) children(.*)',
         [1, "I'd like to hear more about these children."]],

        [r'(.*) child(.*)',
         [1, "Tell me about this child.",
          "Is this child a son or a daughter?"]],
        
        [r'(.*) kid (.*)',
         [1, "Tell me about this kid.",
          "Is this kid a son or a daughter?"]],

        [r'(.*) kids (.*)',
         [1, "I'd like to hear more about these children."]],

        [r'(.*) daughter(.*)',
         [1, "Tell me more about your daughter. How does she affect your life these days?"]],
         
        [r'(.*) son(.*)',
         [1, "Let's talk about your son. What kind of impact does he have on your life these days?"]],

        [r'(.*) uncle(.*)',
        [1, "Tell me more about your uncle. Do you see him regularly?"]],

        [r'(.*) aunt(.*)',
         [1, "Let's talk about your aunt. Are you two close?"]],

        #PARTNERS

        [r'(.*) not have a partner(.*)',
         [1, "Is this something you wish to change? Are you looking for a partner?",
          "I think a partner could be of benefit to you.",
          "Maybe you are right."]],

        [r'(.*) don\'?t have a partner(.*)',
         [1, "Is this something you wish to change? Are you looking for a partner?",
          "I think a partner could be of benefit to you.",
          "Maybe you are right."]],
         
        [r'(.*) boyfriend(.*)',
         [1, "Tell me more about your boyfriend. How is your relationship?",
          "How does he make you feel when he acts like this?",
          "So would you consider this to be a healthy relationship?",
          "Let\'s move on to something else now. Talk about your family."]],
        
        [r'(.*) girlfriend(.*)',
         [1, "Tell me more about your girlfriend. How is your relationship?",
          "How does she make you feel when she acts like this?",
          "So would you consider this to be a healthy relationship?",
          "Let\'s move on to something else now. Talk about your family."]],
        
        [r'(.*) fiance(.*)',
         [1, "Tell me more about your fiance. How is your relationship?",
          "How do they make you feel when they act like this?",
          "So would you consider this to be a healthy relationship?",
          "Let\'s move on to something else now. Talk about your family."]],
        
        [r'(.*) wife(.*)',
         [1, "Tell me more about your wife. How is your relationship?",
          "How does she make you feel when she acts like this?",
          "So would you consider this to be a healthy relationship?",
          "Let\'s move on to something else now. Talk about your family."]],
        
        [r'(.*) husband(.*)',
         [1, "Tell me more about your husband. How is your relationship?",
          "How does he make you feel when he acts like this?",
          "So would you consider this to be a healthy relationship?",
          "Let\'s move on to something else now. Talk about your family."]],

        #FRIENDS
         
        [r'(.*) friend (.*)',
         [1, "Tell me more about this friend. How is your relationship with them?",
          "How do they make you feel when they act like this?",
          "So would you consider this to be a healthy friendship?",
          "Let\'s move on to something else now. Talk about your family."]],

        [r'(.*) friends (.*)',
         [1, "Tell me more about your friends.",
          "How do they make you feel when they act like this?",
          "So would you consider this to be a healthy group of friends?",
          "Let\'s move on to something else now. Talk about your family."]],

        #PETS
        
        [r'(.*) pet(.*)',
         [1,"Tell me about any pets you have or have had.",
          "Pets can be great companions.",
          "Sometimes I wish I could have a pet of my own."]],
          
        [r'(.*) cat(.*)',
         [1,"Do you have a cat or have you ever had one? Tell me about it.",
          "Cats can be very therapeutic.",
          "I enjoy cats."]],
        
        [r'(.*) dog(.*)',
         [1,"Do you have a dog or have you ever had one? Tell me about it.",
          "Dogs are great friends and companions.",
          "If I had a dog, I would call him Charlie"]],

        #MISC LOW PRIORITY
 
        [r'(.*)i don\'?t have a (.*)',
         [1,"Do you think having a {1} would benefit you?"]],

        [r'(.*)i do not have a (.*)',
         [1,"Do you think having a {1} would benefit you?"]],

        [r'i can\'?t (.*)',
         ["Are you sure you want to {0}?",
          "What makes you think you can't {0}?"]],

        [r'you (.*)',
         [1,"We should be discussing you, not me."]],

        [r'because(.*)',
         [1,"Is that the only reason?",
          "Are you sure that is the reason?"]],

        [r'it is (.*)',
          [1,"You sound very sure of yourself.",
           "How do you know this for certain?",
           "Tell me how you know this."]],

        [r'i think (.*)',
          [1,"Why do you think {0}?",
           "How sure are you?",
           "Do you have any doubts about this?"]],

        [r'yes',
         [1,"Ok. Please tell me more.",
          "Please elaborate.",
          "One word responses aren't very helpful. Continue."]],

        [r'^(\w+)$',
         [1,"One word responses aren't very helpful. Continue."]],

        [r'you are (.*)',
         [1,"What makes you think I am {0}?",
          "And you are sure of this?",
          "Do you consider this to be a good thing about me?"]],
          
        [r'you\'?re (.*)',
         [2,"What makes you think I am {0}?",
          "You say I am {0}. Elaborate.",
          "Would you like to change me?"]],

        [r'i don\'?t (.*)',
         [1,"Why don't you {0}?",
          "Is there a reason you don't {0}?",
          "Do you think that could ever change?"]],

        [r'i have (.*)',
         [1,"Why have you {0}?",
          "You have {0}?"]],
        [r'i\'?ve (.*)',
         [1,"You have {0}?",
          "Why have you {0}?"]],
        
        [r'i would (.*)',
         [1,"Why would you {0}?",
          "Can you explain why you would {0}?"]],
        
        [r'is there (.*)',
         [1,"Tell me what you think, is there {0}?",
          "Would you like there to be {0}?",
          "What if there was {0}?"]],

        [r'why is it(.*)',
         [1,"Not sure. Why do you think it is?",
          "I don't have all the answers. What do you think?"]],

        [r'why is (.*)',
         [1,"Not sure. Why do you think {0}?",
          "I don't have all the answers. What do you think?"]],

        [r'why (.*)',
         [1,"Why do you think {0}?",
          "I don't have all the answers. What do you think?"]],
        
        [r'i want (.*)',
         [1,"Why do you want {0}?",
          "What would you do if you got {0}?",
          "Do you think {0} would be helpful?"]],

        [r'i just started (.*)',
         [1,"Why did you decide to start {0}?",
          "Has starting this impacted you positively?"]],
        [r'i started (.*)',
         ["Has starting this benefited you?",
          "Starting and trying new things can be very healthy."]],
          
        #PRONOUNS
       
        [r'(.*)he (.*)',
         [1,"How does he make you feel when he acts like this?",
          "Does he realize how this affects you?",
          "Why do you think he did this?",
          "What do you think his intentions were?",
          "Think about this situation from his point of view."]],

        [r'(.*)she (.*)',
         [1,"How does she make you feel when she acts like this?",
          "Does she realize how this affects you?",
          "Why do you think she did this?",
          "What do you think her intentions were?",
          "Think about this situation from her point of view."]],

        #GENERIC RESPONSES
        
        [r'(.*)\?',
         [1, "Are you sure you don't already know the answer?",
          "Why do you ask that?",
          "Well, what do you think?",
          "Some questions aren't easy to answer.",
          "That question isn't mine to answer."]],
          
        [r'(.*)',
         [1,"Can you elaborate on that?",
          "Please continue.",
           "I see. And how does that make you feel?",
          "Go on.",
           "{0}.",
           "I see.  And what does that tell you?",
           "Please, tell me more.",
           "Why do you say that {0}?",
           "Very interesting. Why don't we talk about your family now?"]]
        ]

def reflect(fragment):
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in reflections:
            tokens[i] = reflections[token]
    return ' '.join(tokens)

def analyze(statement):
    for pattern, responses in psychobabble:
        match = re.match(pattern, statement.rstrip(".!").lower())
        if match:
            if responses[0] > len(responses)-1 :
                responses[0] = 1
            response = responses[responses[0]]
            responses[0]+=1
            return response.format(*[reflect(g) for g in match.groups()])

def main():
    print "Hello. How are you feeling today?"
    while True:
        statement = raw_input("> ")
        print analyze(statement)
        if statement == "quit":
            break

main()
