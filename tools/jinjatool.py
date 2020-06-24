from jinja2 import Environment, FileSystemLoader
import cherrypy


class JinjaTool:

    def __init__(self, templates_path: str):
        self.env = Environment(loader=FileSystemLoader(templates_path))

    def render(self, template_name):
        template = self.env.get_template(template_name)

        if cherrypy.response.status > 399:
            return

        data = cherrypy.response.body or {}
        if template and isinstance(data, dict):
            # Converting str output to bytes.
            cherrypy.response.body = str.encode(template.render(**data))
        else:
            return
