# GOĐEYE - Advanced Security Research Tool

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

> **Educational Purpose Only** - Security research and learning tool for web application analysis.

## 🇺🇸 English

### Overview

GOĐEYE is a security research tool designed for educational purposes to help understand:
- HTTP header security analysis
- API endpoint discovery
- Streaming protocol detection
- Security misconfiguration identification

### Features

- 🔍 **Header Analysis**: Detect missing security headers (HSTS, CSP, etc.)
- 🔗 **API Discovery**: Automatically identify API endpoints
- 🎬 **Stream Detection**: Recognize HLS, DASH, and other streaming protocols
- 📝 **Command Generation**: Generate safe cURL and MPV commands for replication
- 📊 **Research Reporting**: Comprehensive JSON output for analysis

### Installation

```bash
# Clone repository
git clone https://github.com/Pedrohs1771/godeye
cd godeye

# Install dependencies
pip install playwright
playwright install chromium


------------------------------------------------------------------------------------------------------------------------------------------

🇧🇷 Português
Visão Geral
GOĐEYE é uma ferramenta de pesquisa em segurança cibernética desenvolvida para fins educacionais, ajudando a compreender:

Análise de headers HTTP

Descoberta de endpoints de API

Detecção de protocolos de streaming

Identificação de configurações de segurança inadequadas

Funcionalidades
🔍 Análise de Headers: Detecta headers de segurança ausentes (HSTS, CSP, etc.)

🔗 Descoberta de APIs: Identifica automaticamente endpoints de API

🎬 Detecção de Streams: Reconhece HLS, DASH e outros protocolos de streaming

📝 Geração de Comandos: Gera comandos cURL e MPV seguros para replicação

📊 Relatórios de Pesquisa: Saída JSON abrangente para análise

Instalação
bash
# Clone o repositório
git clone https://github.com/seuusuario/godeye
cd godeye

# Instale as dependências
pip install playwright
playwright install chromium
Uso
bash
python godeye.py
Siga as instruções para inserir a URL alvo para análise. A ferramenta irá:

Navegar até o alvo

Monitorar atividade de rede por 30 segundos

Gerar relatórios com as descobertas

Aviso Legal
IMPORTANTE: Esta ferramenta é para PROPÓSITOS EDUCACIONAIS. Use apenas em:

Sistemas que você possui

Sistemas com permissão explícita por escrito para teste

Ambientes autorizados de pesquisa em segurança

Acesso não autorizado a sistemas computacionais é ilegal. O autor não se responsabiliza pelo uso indevido desta ferramenta.

Contact
Discord: violeiro_bad

GitHub: Pedrohs1771/godeye

License
MIT License - See LICENSE for details
