import cherrypy


class WebServiceRoot(object):

    @cherrypy.expose()
    # @cherrypy.tools.json_out()
    @cherrypy.tools.render(template_name='index.html')
    def index(self):
        return {
            'title': 'WebService Jinja Test',
            'content': 'Hi, It\'s WebService Jinja Test'
        }
