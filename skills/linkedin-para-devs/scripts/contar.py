#!/usr/bin/env python3
"""Conta os caracteres de um texto para o LinkedIn.

Uso:
  python3 contar.py [--limite titulo|sobre|convite|posicao|projeto|mensagem|N] [arquivo]
  python3 contar.py --limite convite <<'EOF'
  texto do convite
  EOF
  python3 contar.py --teste

Conta com len() do Python: a quebra de linha vale 1 e a letra acentuada vale 1.
A quebra de linha no fim do arquivo não conta, porque não vai para o campo.
Formulários web costumam contar em UTF-16 (o .length do JavaScript), em que um
emoji vale 2. Quando as duas contagens diferem, o script mostra as duas e
decide pela maior, por segurança.

Saída: caracteres, limite, folga e se passou. Sai com código 1 se estourar.
Só usa a biblioteca padrão.
"""
import argparse
import contextlib
import io
import sys
import tempfile
from pathlib import Path

# "mensagem" é o teto desta skill para mensagem direta (validação, recomendação,
# depois do aceite) ser lida até o fim; o limite do LinkedIn é bem maior.
LIMITES = {"titulo": 220, "sobre": 2600, "convite": 200, "posicao": 2000, "projeto": 2000,
           "mensagem": 500}


def normalizar(dados):
    """Bytes do arquivo ou da entrada padrão -> texto como vai para o campo."""
    return dados.decode("utf-8-sig").replace("\r\n", "\n").rstrip("\n")


def contar(texto):
    """(len() do Python, unidades UTF-16 como o .length do JavaScript)."""
    return len(texto), len(texto.encode("utf-16-le")) // 2


def main(argv=None):
    p = argparse.ArgumentParser(description="Conta caracteres para os campos do LinkedIn.")
    p.add_argument("--limite", help=f"{', '.join(f'{k}={v}' for k, v in LIMITES.items())} ou um número")
    p.add_argument("arquivo", nargs="?", help="arquivo de texto; sem ele, lê a entrada padrão")
    p.add_argument("--teste", action="store_true", help="roda o auto-teste")
    a = p.parse_args(argv)

    if a.teste:
        _teste()
        return 0

    limite = None
    if a.limite is not None:
        limite = LIMITES.get(a.limite) or (int(a.limite) if a.limite.isdecimal() else 0)
        if not limite:
            p.error(f"--limite aceita {', '.join(LIMITES)} ou um número inteiro positivo")

    if a.arquivo is None and sys.stdin.isatty():
        p.error("passe um arquivo ou envie o texto pela entrada padrão")
    try:
        texto = normalizar(Path(a.arquivo).read_bytes() if a.arquivo else sys.stdin.buffer.read())
    except (OSError, UnicodeDecodeError) as e:
        p.error(str(e))

    n, u = contar(texto)
    partes = [f"{n} caracteres"]
    if u != n:
        partes.append(f"{u} em UTF-16, em que emoji vale 2")
    if limite is None:
        print(" · ".join(partes))
        return 0

    folga = limite - max(n, u)
    nome = f" ({a.limite})" if a.limite in LIMITES else ""
    partes += [f"limite {limite}{nome}", f"folga {folga}", "passou" if folga >= 0 else "estourou"]
    print(" · ".join(partes))
    return 0 if folga >= 0 else 1


def _teste():
    assert normalizar(b"oi\r\n") == "oi"
    assert normalizar("\ufeffa\r\nb\n\n".encode()) == "a\nb"
    assert contar("a\nb") == (3, 3)
    assert contar("ção") == (3, 3)
    assert contar("📩 oi") == (4, 5)

    def rodar(*args):
        saida = io.StringIO()
        with contextlib.redirect_stdout(saida), contextlib.redirect_stderr(io.StringIO()):
            try:
                codigo = main(list(args))
            except SystemExit as e:
                codigo = e.code
        return codigo, saida.getvalue().strip()

    with tempfile.TemporaryDirectory() as d:
        arq = Path(d, "t.txt")
        arq.write_text("x" * 220 + "\n", encoding="utf-8")
        assert rodar("--limite", "titulo", str(arq)) == (0, "220 caracteres · limite 220 (titulo) · folga 0 · passou")
        arq.write_text("x" * 221, encoding="utf-8")
        assert rodar("--limite", "titulo", str(arq)) == (1, "221 caracteres · limite 220 (titulo) · folga -1 · estourou")
        arq.write_text("x" * 199 + "📩", encoding="utf-8")  # 200 por len(), 201 em UTF-16
        codigo, saida = rodar("--limite", "convite", str(arq))
        assert codigo == 1 and "201 em UTF-16" in saida and "folga -1" in saida
        assert rodar("--limite", "300", str(arq))[0] == 0
        assert rodar("--limite", "mensagem", str(arq)) == (0, "200 caracteres · 201 em UTF-16, em que emoji vale 2 · limite 500 (mensagem) · folga 299 · passou")
        assert rodar(str(arq)) == (0, "200 caracteres · 201 em UTF-16, em que emoji vale 2")
        assert rodar("--limite", "abc", str(arq))[0] == 2
        assert rodar("--limite", "0", str(arq))[0] == 2
        assert rodar("--limite", "²", str(arq))[0] == 2
        assert rodar("--limite", "titulo", str(Path(d, "nao-existe.txt")))[0] == 2
    print("ok: auto-teste passou")


if __name__ == "__main__":
    sys.exit(main())
