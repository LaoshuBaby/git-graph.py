import subprocess
import re

ansi_escape_codes = [
    (r'\x1B\[31m', '<span style="color:red;">'),
    (r'\x1B\[32m', '<span style="color:green;">'),
    (r'\x1B\[0m', '</span>'),
]

def ansi_to_html(ansi_text):
    for code, replacement in ansi_escape_codes:
        ansi_text = re.sub(code, replacement, ansi_text)
    return ansi_text

log_output = subprocess.check_output([
    'git', 'log', '--graph', '--full-history', '--all',
    '--color', '--pretty=format:"%x1b[31m%h%x09%x1b[32m%d%x1b[0m %s"'
]).decode('utf-8')

html_output = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Git Log Output</title>
<style>
pre {{
    font-family: monospace;
    white-space: pre-wrap;
}}
</style>
</head>
<body>
<pre>{}</pre>
</body>
</html>
""".format(ansi_to_html(log_output))

with open("git_log_output.html", "w") as f:
    f.write(html_output)
