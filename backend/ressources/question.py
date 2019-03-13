from ast import literal_eval

from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse

from common import db

def dict_from_row(row):
    return dict(zip(row.keys(), row))


class Question(Resource):
    def getQuestion(self, question):
        query = "SELECT * FROM procedure WHERE questionid = ?"
        args = [question["questionid"]]
        cur = db.query_db(query, args)
        procedures = [dict(row) for row in cur.fetchall()]
        question["procedures"] = procedures

        for procedure in question["procedures"]:
            query = "SELECT * FROM input WHERE procedureid = ?"
            args = [procedure["procedureid"]]
            cur = db.query_db(query, args)
            inputs = [dict(row) for row in cur.fetchall()]
            procedure["input"] = inputs

            query = "SELECT * FROM output WHERE procedureid = ?"
            args = [procedure["procedureid"]]
            cur = db.query_db(query, args)
            outputs = [dict(row) for row in cur.fetchall()]
            procedure["output"] = outputs

    def get(self, dataset):
        query = "SELECT * FROM question WHERE dataset = ?"
        args = [dataset]
        cur = db.query_db(query, args)
        questions = [dict(row) for row in cur.fetchall()]

        for question in questions:
            self.getQuestion(question)

        return questions

    def post(self, dataset):
        parser = reqparse.RequestParser()
        parser.add_argument("questionid")
        parser.add_argument("question")
        parser.add_argument("procedure")
        args = parser.parse_args()
        args["procedure"] = literal_eval(args["procedure"])

        if not args["questionid"]:
            query = "INSERT INTO question ( question, dataset ) VALUES ( ?, ? )"
            arguments = (args["question"], dataset)
            cur = db.query_db(query, arguments)
            questionid = cur.lastrowid
        else:
            query = "UPDATE question SET question = ?, dataset = ? WHERE questionid = ?"
            arguments = (args["question"], dataset, args["questionid"])
            cur = db.query_db(query, arguments)
            questionid = args["questionid"]



        if args["procedure"]:
            if not "procedureid" in args["procedure"].keys():
                query = "INSERT INTO procedure ( questionid, status ) VALUES ( ?, ? )"
                arguments = (questionid, "open")
                cur = db.query_db(query=query, arguments=arguments)
                procedureid = cur.lastrowid
            else:
                procedureid = args["procedure"]["procedureid"]
                query = "DELETE FROM input WHERE procedureid = ?"
                arguments = [procedureid]
                db.query_db(query=query, arguments=arguments)

                query = "DELETE FROM output WHERE procedureid = ?"
                arguments = [procedureid]
                db.query_db(query=query, arguments=arguments)

            for input in args["procedure"]["input"]:
                query = "INSERT INTO input ( procedureid, name ) VALUES ( ?, ? )"
                arguments = (procedureid, input)
                cur = db.query_db(query=query, arguments=arguments)

            for output in args["procedure"]["output"]:
                query = "INSERT INTO output ( procedureid, name ) VALUES ( ?, ? )"
                arguments = (procedureid, output)
                cur = db.query_db(query=query, arguments=arguments)

        query = "SELECT * FROM question WHERE questionid = ?"
        arguments = [str(questionid)]
        cur = db.query_db(query=query, arguments=arguments)
        questions = [dict(row) for row in cur.fetchall()]

        for question in questions:
            self.getQuestion(question)

        return questions, 201

    def put(self, dataset):
        self.post(dataset)

    def delete(self, dataset):
        questionid = dataset
        query = "DELETE FROM question WHERE questionid = ?"
        arguments = [questionid]
        db.query_db(query=query, arguments=arguments)

        query = "SELECT * FROM procedure WHERE questionid = ?"
        args = [questionid]
        cur = db.query_db(query, args)
        procedures = [dict(row) for row in cur.fetchall()]

        for procedure in procedures:
            query = "DELETE FROM input WHERE procedureid = ?"
            arguments = [procedure["procedureid"]]
            db.query_db(query=query, arguments=arguments)

            query = "DELETE FROM output WHERE procedureid = ?"
            arguments = [procedure["procedureid"]]
            db.query_db(query=query, arguments=arguments)

        query = "DELETE FROM procedure WHERE questionid = ?"
        arguments = [questionid]
        db.query_db(query=query, arguments=arguments)

        return '', 204
