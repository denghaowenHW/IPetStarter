from flask_restplus import Namespace, Resource

ns = Namespace('user')


@ns.route('/<string:action>')
class User(Resource):
    def put(self, action):
        print action
        if action == 'delete':
            pass
        elif action == 'edit':
            pass
        elif action == 'add':
            pass

        return action
