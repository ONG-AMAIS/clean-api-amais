def ok(message, payload):
    payload_to_dict = [(dict(row)) for row in payload]
    return {'message': message, 'payload': payload_to_dict}, 200


def created(message, payload):
    payload_to_dict = [(dict(row)) for row in payload]
    return {'message': message, 'payload': payload_to_dict}, 201


def notFound(message, payload):
    payload_to_dict = [(dict(row)) for row in payload]
    return {'message': message, 'payload': payload_to_dict}, 404


def unauthorized(message, payload):
    payload_to_dict = [(dict(row)) for row in payload]
    return {'message': message, 'payload': payload_to_dict}, 401
