import zipfile
import os

def create_simple_epub(output_path, target_url):
    with zipfile.ZipFile(output_path, 'w') as epub:
        # 1. mimetype (MUST be first and uncompressed)
        epub.writestr('mimetype', 'application/epub+zip', compress_type=zipfile.ZIP_STORED)
        
        # 2. META-INF/container.xml
        epub.writestr('META-INF/container.xml', """<?xml version="1.0"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>""")
        
        # 3. content.opf
        epub.writestr('content.opf', f"""<?xml version="1.0"?><package xmlns="http://www.idpf.org/2007/opf" version="2.0" unique-identifier="id"><metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:title>DASHBOARD</dc:title><dc:language>ko</dc:language><dc:identifier id="id">vibe01</dc:identifier></metadata><manifest><item id="main" href="main.xhtml" media-type="application/xhtml+xml"/></manifest><spine><itemref id="main"/></spine></package>""")
        
        # 4. main.xhtml
        epub.writestr('main.xhtml', f"""<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head><title>GO</title></head>
<body style="text-align:center; padding-top:50px;">
    <h2>VIBE OPS</h2>
    <p>아래 링크를 터치하세요:</p>
    <br/>
    <a href="{target_url}" style="font-size:24px; font-weight:bold; color:black; text-decoration:underline;">[ 대시보드 접속하기 ]</a>
</body>
</html>""")

if __name__ == "__main__":
    path = "VibeDashboard.epub"
    url = "http://your-server-ip/eink.html"
    create_simple_epub(path, url)
    print(f"EPUB created successfully at {path}")

