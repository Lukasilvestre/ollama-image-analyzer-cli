# analyze_image.py

import ollama
import os
import yaml
import json
import argparse
from datetime import datetime

def main():

    # --- Configuração dos Argumentos da Linha de Comando ---
    parser = argparse.ArgumentParser(
        description="Analisa uma imagem local usando um modelo VLM do Ollama e salva a descrição em um arquivo JSON."
    )
    parser.add_argument("image_path", help="O caminho para o arquivo de imagem a ser analisado.")
    parser.add_argument("-p", "--prompt", help="O prompt ou pergunta a ser feita sobre a imagem.")
    parser.add_argument("-m", "--model", help="O nome do modelo VLM a ser usado (ex: llava:7b). Usa o padrão do config.yaml se não for especificado.")
    args = parser.parse_args()

    # --- Carrega a Configuração Padrão ---
    try:
        with open('config.yaml', 'r') as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        print("Aviso: 'config.yaml' não encontrado. Usando valores padrão.")
        config = {'default_vlm_model': 'gemma3:4b'}

    # --- Valida a Imagem de Entrada ---
    if not os.path.exists(args.image_path):
        print(f"Erro: Arquivo de imagem não encontrado em '{args.image_path}'")
        exit()

    # --- Define o Modelo e o Prompt a Serem Usados ---
    # Usa o modelo do argumento, ou o padrão do config
    model_to_use = args.model if args.model else config.get('default_vlm_model', 'gemma3:4b')
    # Usa o prompt do argumento, ou um prompt genérico
    prompt_to_use = args.prompt if args.prompt else "Descreva esta imagem em detalhes."
    
    # --- Execução da Análise ---
    print(f"🤖 Analisando '{args.image_path}' com o modelo '{model_to_use}'...")
    print(f"🗣️ Pergunta: {prompt_to_use}\n")

    try:
        response = ollama.chat(
            model=model_to_use,
            messages=[{
                'role': 'user',
                'content': prompt_to_use,
                'images': [args.image_path]
            }]
        )
        
        description = response['message']['content']
        print("💡 Resposta do modelo:")
        print(description)

        # --- Salva o Resultado em um Arquivo Estruturado ---
        output_data = {
            'timestamp': datetime.now().isoformat(),
            'image_path': args.image_path,
            'model_used': model_to_use,
            'prompt': prompt_to_use,
            'description': description,
            'full_response': response 
        }

        output_folder = "outputs"
        os.makedirs(output_folder, exist_ok=True)
        
        # Cria um nome de arquivo de saída único
        base_filename = os.path.splitext(os.path.basename(args.image_path))[0]
        timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = os.path.join(output_folder, f"{base_filename}_analysis_{timestamp_str}.json")

        with open(output_filename, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=4)
        
        print(f"\n✅ Análise concluída e resultado salvo em: {output_filename}")

    except Exception as e:
        print(f"\nOcorreu um erro ao se comunicar com o Ollama: {e}")
        print("Verifique se o Ollama está rodando e se o modelo foi baixado corretamente (ex: 'ollama pull gemma').")

if __name__ == "__main__":
    main()
