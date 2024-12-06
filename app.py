from flask import Flask, render_template, redirect, url_for, flash
from flask_mail import Mail, Message
from app.forms import RuleProposalForm
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Email configuration
app.config['MAIL_SERVER'] = os.getenv("MAIL_SERVER")
app.config['MAIL_PORT'] = int(os.getenv("MAIL_PORT"))
app.config['MAIL_USE_TLS'] = os.getenv("MAIL_USE_TLS") == "True"
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")

mail = Mail(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/propose-rule", methods=["GET", "POST"])
def propose_rule():
    form = RuleProposalForm()
    if form.validate_on_submit():
        # Capture form data
        name = form.name.data
        title = form.title.data
        description = form.description.data

        # Send email
        msg = Message(
            subject=f"New Rule Proposal: {title}",
            sender=app.config['MAIL_USERNAME'],
            recipients=[os.getenv("MAIL_RECIPIENT")],  # Load recipient from env
            body=f"Proposed by: {name}\n\nTitle: {title}\n\nDescription:\n{description}"
        )
        mail.send(msg)

        flash("Your proposal has been submitted and emailed to the league admin!", "success")
        return redirect(url_for("propose_rule"))

    return render_template("propose_rule.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
