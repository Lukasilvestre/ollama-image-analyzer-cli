# 🤖 Analisador de Imagens com VLM (CLI)

![Status](https://img.shields.io/badge/status-funcional-green)
![Python](https://img.shields.io/badge/python-3.8+-blue?logo=python)
![Ollama](https://img.shields.io/badge/Ollama-1.0-lightgrey)

Esta é uma ferramenta de linha de comando (CLI) em Python que utiliza um Modelo de Linguagem e Visão (VLM) local, servido pelo [Ollama](https://ollama.com/), para analisar e descrever qualquer imagem fornecida pelo usuário.

## 📜 Sobre a Ferramenta

O objetivo deste projeto é fornecer uma interface simples e reutilizável para interagir com modelos multimodais. Em vez de um script fixo, esta ferramenta permite que o usuário especifique dinamicamente a imagem e a pergunta (prompt) a ser feita, salvando a análise completa em um arquivo JSON estruturado para referência futura.

## 🚀 Como Usar

1.  **Pré-requisitos:**
    * Tenha o [Ollama instalado](https://ollama.com/) e um modelo VLM baixado (ex: `ollama pull llava:7b`).

2.  **Clone o repositório e instale as dependências:**
    ```bash
    git clone [https://github.com/Lukasilvestre/ollama-image-analyzer-cli.git](https://github.com/Lukasilvestre/ollama-image-analyzer-cli.git)
    cd ollama-image-analyzer-cli
    pip install -r requirements.txt
    ```

3.  **Execute a Análise:**
    O uso básico é fornecer o caminho para a imagem que você deseja analisar.

    ```bash
    python analyze_image.py /caminho/para/sua/imagem.jpg
    ```

4.  **Uso com um Prompt Personalizado:**
    Você pode fazer uma pergunta específica sobre a imagem usando a flag `-p` ou `--prompt`.

    ```bash
    python analyze_image.py minha_foto.png --prompt "Quantas pessoas estão nesta imagem?"
    ```

5.  **Especificando um Modelo Diferente:**
    Use a flag `-m` ou `--model` para usar outro modelo VLM que você tenha baixado.
    ```bash
    python analyze_image.py foto_carro.jpg -m phi3 -p "Qual a cor deste carro?"
    ```

## 📄 Saída do Programa

Para cada análise, a ferramenta imprime a resposta do modelo no terminal e também salva um arquivo `.json` detalhado na pasta `outputs/`.

**Exemplo de arquivo `outputs/minha_foto_analysis_20250811_153000.json`:**
```json
{
    "timestamp": "2025-08-11T15:30:00.123456",
    "image_path": "minha_foto.png",
    "model_used": "llava:7b",
    "prompt": "Quantas pessoas estão nesta imagem?",
    "description": "Existem duas pessoas visíveis nesta imagem, ambas sentadas em um banco de praça."
}
```
---
