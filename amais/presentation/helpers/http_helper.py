from flask import render_template, make_response


def ok(message, payload):
    return {'message': message, 'payload': payload}, 200


def created(message, payload):
    return {'message': message, 'payload': payload}, 201


def not_found(message, payload):
    return {'message': message, 'payload': payload}, 404


def bad_request(message, payload):
    return {'message': message, 'payload': payload}, 400


def unauthorized(message, payload):
    return {'message': message, 'payload': payload}, 401


def unprocessable_entity(message, payload):
    return {'message': message, 'payload': payload}, 422


def render(template: str, **variables):
    headers = {'Content-Type': 'text/html'}
    return make_response(render_template(template, **variables), 200, headers)
