import telegram
import openai

openai.api_key = "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"
bot = telegram.Bot(token='5737745294:AAFHBgmpRnlTT0PdSwQPUpL2v6GyVQiOCOY')

def handle_message(message):
    text = message.text
    chat_id = message.chat.id
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt='What is your question?',
        temperature=0.5,
        max_tokens=30,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    bot.send_message(chat_id=chat_id, text=response.choices[0].text)

bot.message_loop(handle_message)