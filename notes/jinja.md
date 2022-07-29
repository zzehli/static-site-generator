<!-- https://jinja.palletsprojects.com/en/3.1.x/templates/ -->
* syntax
    * statements: `{% ... %}` control structures: for, if, macros, etc
    * expressions: `{{ ... }}` objects, methods defined on objects, logic, math, etc
    * comments: `{# ... #}`
* template inheritance: base template with blocks that child templates can override
    * base: html skeleton, define blocks with `{% block %}` and `{% endblock %}`, they are placeholders that a child can override
    * child: define blocks to fill the base html 
