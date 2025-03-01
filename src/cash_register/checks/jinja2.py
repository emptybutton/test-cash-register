import jinja2
from django.conf import settings


searchpath = (
    settings.BASE_DIR / "src" / "cash_register"
    / "checks" / "templates" / "checks" / "jinja2"
)
_loader = jinja2.FileSystemLoader(searchpath=searchpath)
jinja2_env = jinja2.Environment(loader=_loader, autoescape=True)

jinja2_check_tempate = jinja2_env.get_template("check.html")
