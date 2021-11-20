def ok(message, payload):
    return {'message': message, 'payload': payload}, 200


def created(message, payload):
    return {'message': message, 'payload': payload}, 201


def not_found(message, payload):
    return {'message': message, 'payload': payload}, 404


def unauthorized(message, payload):
    return {'message': message, 'payload': payload}, 401


def unprocessable_entity(message, payload):
    return {'message': message, 'payload': payload}, 422
