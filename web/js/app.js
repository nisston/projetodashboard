document.addEventListener("DOMContentLoaded", () => {
    fetch("dados.json")
        .then(response => {
            if (!response.ok) throw new Error("Erro ao carregar dados.json");
            return response.json();
        })
        .then(data => {
            // 1. Preenche os Cards
            document.getElementById("card-modulos").textContent = data.resumo.total_modulos;
            document.getElementById("card-acessos").textContent = data.resumo.total_acessos.toLocaleString("pt-BR");
            document.getElementById("card-aprovacao").textContent = data.resumo.media_aprovacao + "%";

            // 2. Preenche a Tabela
            const corpo = document.getElementById("tabela-corpo");
            corpo.innerHTML = "";

            data.detalhes.forEach(item => {
                const tr = document.createElement("tr");
                tr.innerHTML = "
                    <td><strong>${item.modulo}</strong></td>
                    <td>${item.tempo_ms} ms</td>
                    <td>${item.acessos.toLocaleString("pt-BR")}</td>
                    <td><span style="color: #4ade80; font-weight: bold;">${item.aprovacao}%</span></td>
                ";
                corpo.appendChild(tr);
            });
        })
        .catch(err => {
            console.error("Falha ao inicializar dashboard:", err);
            document.getElementById("tabela-corpo").innerHTML = 
                '<tr><td colspan="4" style="color: #f87171;">Erro ao carregar os dados consolidados.</td></tr>';
        });
});