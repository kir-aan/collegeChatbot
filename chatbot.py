from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

college_Bot = ChatBot('College Enquiry Bot',
                      filters=["chatterbot.filters.RepetitiveResponseFilter"],
                      preprocessors=['chatterbot.preprocessors.unescape_html'],
                      logic_adapters=[{
                          'import_path': 'chatterbot.logic.BestMatch'
                      },
                          {
                          'import_path': 'chatterbot.logic.BestMatch',
                          'maximum_similarity_threshold': 0.65,
                          'default_response': 'I am sorry, but I do not understand.'
                      }])


# college_Bot.set_trainer(ChatterBotCorpusTrainer)
trainer = ChatterBotCorpusTrainer(college_Bot)
trainer.train(
    "chatterbot.corpus.english.collegebotresponse"
)


@app.route("/")
@app.route("/home")
def home():
  return render_template("index.html")


@app.route("/about")
def about():
  return render_template('about.html')


@app.route("/get")
def get_bot_response():
  userText = request.args.get('msg')
  return str(college_Bot.get_response(userText))


if __name__ == "__main__":
  app.run()
