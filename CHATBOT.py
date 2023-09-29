from tkinter import Entry, Button, Text, Scrollbar, StringVar, Frame, Tk
import re

class RecommendationChatBot:
    def __init__(self):
        self.quit = False
    responses = {
        r'hi|hey|hello': 'Hello! How can I assist you today?',
        r'bye|quit|exit': '_quit_',
        r'thanks?': 'You are welcome.',
        r'what\'?s? up|how\'?s? it going': 'I\'m here ready to help you!',
        r'how are you': 'As a bot, I don\'t have feelings, but thanks for asking! How can I help?',
        r'i am (.*)': 'Nice to meet you, {0!s}. How may I assist you today?',
        r'recommend a movie': 'Sure! How about the movie "Inception"? It\'s a great mix of science fiction and thriller.',
        r'recommend a song': 'Of course! I suggest listening to "Bohemian Rhapsody" by Queen. It\'s a classic.',
        r'recommend a series': 'Sure, why not watch "Breaking Bad"? It is highly rated and appreciated by many.',
        r'.*': 'I didn\'t quite get that. Could you repeat it, please?'
    }

    def match_rule(self, rules, message):
        for pattern, response in rules.items():
            match = re.search(pattern, message)
            if match is not None:
                resp = response
                var = match.group(1) if '{0}' in response else None
                return resp, var
        return "I didn't understand that, could you try again?", None

    def preprocess_text(self, message):
        cleaned = re.sub(r'\n', '', message).lower()
        return cleaned

    def respond(self, message):
        clean_message = self.preprocess_text(message)
        best_response, var = self.match_rule(self.responses, clean_message)
        if var is not None:
            best_response = best_response.format(var)

        if best_response == '_quit_':
            self.quit = True
            return 'Goodbye! Have a beautiful day.'

        return 'Bot: ' + best_response + '\n'

def send(bot, messages, message_var):
    message = message_var.get()
    bot_response = bot.respond(message)
    messages.insert('end', f'User: {message}\n{bot_response}')
    message_var.set('')

window = Tk()
window.title("ChatBot")
frame = Frame(window)

scrollbar = Scrollbar(frame)
scrollbar.pack(side='right', fill='y')

messages = Text(frame, wrap='word', yscrollcommand=scrollbar.set)
messages.pack(side='left', fill='both', expand=True)

frame.pack(fill='both', expand=True)

message_var = StringVar()
message_entry = Entry(window, textvariable=message_var)
message_entry.pack(fill='x', padx=5)

send_button = Button(window, text='Send', command = lambda: send(RecommendationChatBot(), messages, message_var))
send_button.pack(side='right', fill='y')

window.mainloop()