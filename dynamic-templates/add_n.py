#C:\_my\Netology\Django\dj_hw\dynamic-templates\materialize_css.css

import os.path

path = 'C:\\_my\\Netology\\Django\\dj_hw\\dynamic-templates'
file = os.path.join(path, 'materialize_css.css')
new_file = os.path.join(path, 'materialize_css_formated.css')

with open(file) as f:
    text = f.read()
    with open(new_file, 'w') as nf:
        nf.write( text.replace('}', '}\n') )
