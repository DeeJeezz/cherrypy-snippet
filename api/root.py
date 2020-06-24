import cherrypy


class ApiRoot(object):

    @cherrypy.expose()
    @cherrypy.tools.json_out()
    def index(self):

        return {'error': None, 'result': 'This is index endpoint!'}
