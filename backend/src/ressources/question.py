from ast import literal_eval
import json

from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse

from common import db
from models.Question import Question, Procedure, Input, Output


class QuestionView(Resource):
    def get(self, dataset):
        return jsonify(Question.query.all())
        #return jsonify([i.serialize for i in User.query.all()])

    def post(self, dataset):
        parser = reqparse.RequestParser()
        parser.add_argument("id")
        parser.add_argument("question")
        parser.add_argument("procedure")
        args = parser.parse_args()
        args["procedure"] = literal_eval(args["procedure"])

        if not args["id"]:
            question = Question(dataset=dataset, question=args["question"])
            db.db.getDB().session.add(question)
            db.db.getDB().session.commit()
        else:
            question = Question.query.filter_by(id=args["id"]).first()


        if args["procedure"]:
            if not "id" in args["procedure"].keys():
                procedure = Procedure(question=question.id, status="open")
                db.db.getDB().session.add(procedure)
                db.db.getDB().session.commit()
            else:
                procedure = Procedure.query.filter_by(id=args["procedure"]["id"]).first()
                inputs = Input.query.filter_by(procedure=procedure.id)
                inputs.delete()

                outputs = Ouput.query.filter_by(procedure=procedure.id)
                outputs.delete()

            for input in args["procedure"]["input"]:
                new_input = Input(procedure=procedure.id, name=input)
                db.db.getDB().session.add(new_input)

            for output in args["procedure"]["output"]:
                new_output = Output(procedure=procedure.id, name=output)
                db.db.getDB().session.add(new_output)
        db.db.getDB().session.commit()

        return jsonify(procedure)

    def put(self, dataset):
        pass

    def delete(self, dataset):
        pass
