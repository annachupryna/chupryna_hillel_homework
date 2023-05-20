import re

# 4
markup = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My super star task</title>
</head>
<body>
    <div id="block-with-links">
        <div id="google">
            <a href="www.google.com">
                Google
            </a>
        </div>
        <div id="facebook">
            <a href="http://facebook.com/dign-in">
                Facebook
            </a>
        </div>
        <div id="amazon">
            <a href="amazon.com">
                Amazon
            </a>
        </div>
    </div>
</body>
</html>
"""

pattern = r'<div id="(\w+)">\s*<a href="([^"]+)">\s*([^<]+)\s*</a>\s*</div>'
matches = re.findall(pattern, markup)

result = [(name, link, text.strip()) for name, link, text in matches]
print(result)
