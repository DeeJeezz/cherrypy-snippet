import cherrypy
from tools.jinjatool import JinjaTool


def main():

    jinja_tool = JinjaTool('./templates')

    cherrypy.tools.render = cherrypy.Tool('before_finalize', jinja_tool.render)

    from api.root import ApiRoot
    from webservice.root import WebServiceRoot

    cherrypy.tree.mount(ApiRoot(), '/api', {
        '/': {

        }
    })

    cherrypy.tree.mount(WebServiceRoot(), '/', {
        '/': {
            'tools.encode.on': False,
        }
    })

    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == '__main__':
    main()
