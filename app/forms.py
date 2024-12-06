from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class RuleProposalForm(FlaskForm):
    name = StringField("Your Name", validators=[DataRequired()])
    title = StringField("Rule Title", validators=[DataRequired()])
    description = TextAreaField("Rule Description", validators=[DataRequired()])
    submit = SubmitField("Submit Proposal")
