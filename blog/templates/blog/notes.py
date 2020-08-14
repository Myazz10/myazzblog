# The paragraph
{% for item in posts % }
<li > <a href = "#" > {{item.category_tags}} < span > ({{item.category_count.count}}) < /span > </a > </li >
{% endfor % }

{% for item in posts % }
<li > <a href = "#" > {{item.category_tags}} < span > ({{item.category_count.count}}) < /span > </a > </li >
{% endfor % }

# view to template ctx:
example_dictionary = {'a': [1, 2]}

# template:
{ % for key, value_list  in example_dictionary.items % }
The key is {{key}}
    { % for value in value_list % }
    The key is {{key}} and the value is {{value}}
    { % endfor % }
{ % endfor % }
