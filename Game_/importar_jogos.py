import requests
from meu_app.models import Jogo
from django.core.files.base import ContentFile
from deep_translator import GoogleTranslator
import time

API_KEY = "999eb1ffbcd2467d9415e1b980dd9bb8"

def importar_jogos(pagina=2):
    print(f"Começando a importação da página {pagina}...")
    url_lista = f"https://api.rawg.io/api/games?key={API_KEY}&page_size=40&page={pagina}"
    response_lista = requests.get(url_lista)
    print(f"Status da API (lista): {response_lista.status_code}")
    
    if response_lista.status_code == 200:
        jogos = response_lista.json()['results']
        print(f"Total de jogos encontrados: {len(jogos)}")
        
        for jogo in jogos:
            url_detalhes = f"https://api.rawg.io/api/games/{jogo['id']}?key={API_KEY}"
            response_detalhes = requests.get(url_detalhes)
            print(f"Buscando detalhes de {jogo['name']} - Status: {response_detalhes.status_code}")
            
            descricao = "Sem descrição disponível"
            if response_detalhes.status_code == 200:
                detalhes = response_detalhes.json()
                descricao_en = detalhes.get('description_raw', 'Sem descrição disponível')
                if descricao_en != "Sem descrição disponível":
                    try:
                        # Traduz do inglês pro português
                        descricao = GoogleTranslator(source='en', target='pt').translate(descricao_en)
                    except Exception as e:
                        print(f"Erro ao traduzir {jogo['name']}: {e}")
                        descricao = descricao_en  # Mantém em inglês se falhar
            
            imagem_url = jogo.get('background_image', '')
            imagem_nome = None
            if imagem_url:
                imagem_response = requests.get(imagem_url)
                if imagem_response.status_code == 200:
                    imagem_nome = f"{jogo['name'].replace(' ', '_')}.jpg"
                    novo_jogo = Jogo(
                        titulo=jogo['name'],
                        descricao=descricao,
                    )
                    novo_jogo.imagem.save(imagem_nome, ContentFile(imagem_response.content), save=True)
                    print(f"Adicionado: {jogo['name']} com imagem")
                else:
                    novo_jogo = Jogo.objects.create(
                        titulo=jogo['name'],
                        descricao=descricao,
                    )
                    print(f"Adicionado: {jogo['name']} sem imagem")
            else:
                novo_jogo = Jogo.objects.create(
                    titulo=jogo['name'],
                    descricao=descricao,
                )
                print(f"Adicionado: {jogo['name']} sem imagem")
            time.sleep(0.5)
    else:
        print(f"Erro na API (lista): {response_lista.status_code}")
    print("Importação concluída!")

if __name__ == "__main__":
    importar_jogos()