⚙️ Instalação das Dependências
1. Criar ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows

2. Instalar bibliotecas necessárias
pip install numpy soundfile kokoro-tts openai


🔹 Observação: O kokoro-tts pode ter dependências adicionais dependendo do sistema.

🚀 Como Executar

Salve o código em um arquivo, por exemplo:

main.py


Execute o script:

python main.py


O arquivo audio_completo.wav será gerado no diretório atual.

🎧 Resultado Esperado

Após a execução, você terá um arquivo de áudio com a fala sintetizada do texto informado, utilizando a voz escolhida.