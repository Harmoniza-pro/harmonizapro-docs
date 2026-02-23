#!/bin/bash
# ============================================
# HarmonizaPRO - Setup Completo da Documentação
# ============================================
# Execute: chmod +x setup.sh && ./setup.sh

set -e

echo "🚀 Configurando HarmonizaPRO Docs..."

# 1) Criar estrutura de diretórios
echo "📁 Criando estrutura de diretórios..."
mkdir -p docs/workflows docs/playbooks docs/runbooks workflows/exports tools

# 2) Criar ambiente virtual e instalar dependências
echo "🐍 Criando ambiente virtual Python..."
python -m venv .venv

# Detectar OS para ativar venv
if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    source .venv/Scripts/activate
else
    source .venv/bin/activate
fi

echo "📦 Instalando MkDocs + Material theme..."
pip install mkdocs mkdocs-material

# 3) Inicializar Git (se não existir)
if [ ! -d ".git" ]; then
    echo "🔧 Inicializando Git..."
    git init
fi

echo ""
echo "✅ Setup completo!"
echo ""
echo "📋 Próximos passos:"
echo "   1. Coloque o JSON exportado do n8n em: workflows/exports/"
echo "   2. Rode: python tools/generate_docs.py"
echo "   3. Rode: mkdocs serve"
echo "   4. Abra no navegador o link que aparecer no terminal"
echo ""
