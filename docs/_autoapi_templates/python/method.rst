.. SPDX-FileCopyrightText: © 2015 Read the Docs, Inc
.. SPDX-FileCopyrightText: © 2025 Romain Brault <mail@romainbrault.com>
..
.. SPDX-License-Identifier: MIT

{% if obj.display %}
   {% if is_own_page %}
{{ obj.id }}
{{ "=" * obj.id | length }}

   {% endif %}
.. py:method:: {% if is_own_page %}{{ obj.id }}{% else %}{{ obj.short_name }}{% endif %}({{ obj.args }}){% if obj.return_annotation is not none %} -> {{ obj.return_annotation }}{% endif %}
   {% for (args, return_annotation) in obj.overloads %}

               {%+ if is_own_page %}{{ obj.id }}{% else %}{{ obj.short_name }}{% endif %}({{ args }}){% if return_annotation is not none %} -> {{ return_annotation }}{% endif %}
   {% endfor %}
   {% for property in obj.properties %}

   :{{ property }}:
   {% endfor %}

   {% if obj.docstring %}

   {{ obj.docstring|indent(3) }}
   {% endif %}
{% endif %}
