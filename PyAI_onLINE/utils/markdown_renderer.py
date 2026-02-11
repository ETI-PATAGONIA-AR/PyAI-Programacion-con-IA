#==================================================================
# PyAI_v1\utils\markdown_renderer.py - ETI Patagonia
#==================================================================

import markdown
import html
import re

CODE_BLOCK_RE = re.compile(r"```(.*?)```", re.DOTALL)

def render_markdown(md_text: str) -> str:
    """
    Convierte Markdown a HTML y envuelve bloques de código
    con estilo + botón copiar
    """

    def repl(match):
        code = html.escape(match.group(1).strip())
        return f"""
        <div style="background:#1e1e1e; border-radius:6px; padding:8px; margin:8px 0;">
            <button onclick="navigator.clipboard.writeText(`{code}`)"
                style="float:right; background:#444; color:white;
                border:none; padding:4px 8px; cursor:pointer;">
                Copiar
            </button>
            <pre style="color:#dcdcdc; font-family:Consolas, monospace;">
{code}
            </pre>
        </div>
        """

    md_text = CODE_BLOCK_RE.sub(repl, md_text)

    html_body = markdown.markdown(
        md_text,
        extensions=["fenced_code", "tables"]
    )

    return f"""
    <html>
    <head>
    <meta charset="utf-8">
    </head>
    <body style="font-family:Segoe UI; font-size:13px;">
        {html_body}
    </body>
    </html>
    """
