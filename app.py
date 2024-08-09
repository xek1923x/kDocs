import os
from flask import Flask, request, make_response, redirect, render_template
from groq import Groq

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("kdocs.html", output="")

systemprompt = "Output always in the right language the user had asked you the question in. Keep your answers short and precise. You are a smart text assistant. You can write e-mails, texts, friendly messages or summarize things. Therefore, just start the content right away and never say an introductury sentence."

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

@app.route("/", methods=["POST"])
def intelligence():
    if request.method == "POST":
        prompt = request.form.get("autoresizing")
        outputai = llama3(prompt)
        return render_template("kdocs.html", output=outputai, promptuser=prompt)

def llama3(prompt):
    if prompt == "":
        return
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{prompt}",
            },
            {
                "role": "system",
                "content": f"{systemprompt}",
            },
        ],
        model="llama3-8b-8192",
    )

    print(chat_completion.choices[0].message.content)
    outputai = chat_completion.choices[0].message.content
    return outputai


