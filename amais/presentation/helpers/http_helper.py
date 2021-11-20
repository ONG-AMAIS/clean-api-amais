def ok(message, payload):
    return {'message': message, 'payload': payload}, 200


def created(message, payload):
    return {'message': message, 'payload': payload}, 201


def notFound(message, payload):
    return {'message': message, 'payload': payload}, 404


def unauthorized(message, payload):
    return {'message': message, 'payload': payload}, 401
