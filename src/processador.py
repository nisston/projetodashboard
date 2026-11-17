import csv
import json
import os

def processar_dados_csv(caminho_csv):
    if not os.path.exists(caminho_csv):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_csv}")

    modulos = []
    total_acessos = 0
    soma_aprovacao = 0

    with open(caminho_csv, mode="r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        for linha in leitor:
            acessos = int(linha["acessos"])
            taxa = float(linha["taxa_aprovacao"])
            
            modulos.append({
                "modulo": linha["modulo"],
                "tempo_ms": int(linha["tempo_carregamento_ms"]),
                "acessos": acessos,
                "aprovacao": taxa
            })
            total_acessos += acessos
            soma_aprovacao += taxa

    media_aprovacao = round(soma_aprovacao / len(modulos), 2) if modulos else 0

    return {
        "resumo": {
            "total_modulos": len(modulos),
            "total_acessos": total_acessos,
            "media_aprovacao": media_aprovacao
        },
        "detalhes": modulos
    }

def main():
    origem = os.path.join("data", "metricas.csv")
    destino = os.path.join("web", "dados.json")

    resultado = processar_dados_csv(origem)

    with open(destino, mode="w", encoding="utf-8") as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)

    print(f"Sucesso: {origem} processado e exportado para {destino}!")

if __name__ == "__main__":
    main()