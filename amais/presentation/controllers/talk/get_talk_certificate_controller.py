from flask_restful import Resource
from amais.presentation.helpers.http_helper import ok, not_found, render
from amais.utils.exceptions import Error
from flask_restful import Resource, reqparse
from amais.main.configs.constants import SERVER_BASE_URL
from amais.data.usecases.talk.get_talk_certificate import GetTalkCertificate


class GetTalkCertificateController(Resource):

    @classmethod
    def get(self, talk_id: int, cpf: str):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('output', type=str)

            args = parser.parse_args()

            talk_data = GetTalkCertificate().get(talk_id=talk_id, cpf=cpf)

            if not args['output'] or args['output'] == 'json':

                link = '{base_url}/talks/{talk_id}/entrants/{cpf}?output=html'.format(
                    talk_id=talk_id, cpf=cpf, base_url=SERVER_BASE_URL)

                return ok(message='Certificado gerado com sucesso!', payload={'link': link})

            return render(template=talk_data['file_name'], name=talk_data['entered']['name'], cpf=talk_data['entered']['cpf'])

        except Error as error:
            CASES = {
                'TALK_NOT_FOUND': not_found(message='Não foi possível encontrar a palestra solicitada.', payload={}),
                'SUBSCRIPTION_NOT_FOUND': not_found(message='Não foi possível encontrar a inscrição solicitada', payload={})
            }

            return CASES[error.title]
