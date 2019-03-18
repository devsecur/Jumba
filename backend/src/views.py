from models.Question import Question, Procedure, Input, Output

from ressources.user import UserView
from ressources.question import QuestionView

def views(api):
    api.add_resource(UserView, '/<string:name>')
    api.add_resource(QuestionView, '/question/<string:dataset>')
