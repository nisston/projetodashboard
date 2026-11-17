import pytest
from processador import processar_dados_csv

def test_processamento_csv_valido():
    resultado = processar_dados_csv("data/metricas.csv")
    assert "resumo" in resultado
    assert resultado["resumo"]["total_modulos"] > 0
    assert resultado["resumo"]["total_acessos"] > 0
    assert 0 <= resultado["resumo"]["media_aprovacao"] <= 100

def test_arquivo_inexistente():
    with pytest.raises(FileNotFoundError):
        processar_dados_csv("data/nao_existe.csv")