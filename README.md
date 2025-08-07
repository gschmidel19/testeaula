# Projetos do Bootcamp de Análise de Dados — TripleTen

Repositório com os projetos desenvolvidos durante o curso de formação em Análise de Dados da [TripleTen](https://tripleten.com).

## 📌 Lista de Projetos

| Sprint | Nome do Projeto                                    | Link |
|--------|----------------------------------------------------|------|
| 1      | Quiz: Avaliação e Correção de Dados de Usuário     | [Ver projeto](https://github.com/gschmidel19/sprint-01-quiz-qualidade-dados/tree/main/sprint-01-quiz-qualidade-dados) |
| 2      | Teste de Hipótese: Preferências Musicais por Cidade | [Ver projeto](https://github.com/gschmidel19/sprint-02-preferencias-musicais-cidades/tree/main/sprint-02-preferencias-musicais-cidades) |
| 3      | Análise de Teste A/B em Loja Online                | [Ver projeto](https://github.com/gschmidel19/sprint-3-ab-test-analysis/tree/main/sprint-3-ab-test-analysis) |
| 4      | Análise Estatística de Dados: Plano Megaline       | [Ver projeto](https://github.com/gschmidel19/Sprint_4_Megaline/tree/main/Sprint_4_Megaline) |
| 5      | Dashboard Interativo com Streamlit                 | [Ver projeto](https://github.com/gschmidel19/sprint-05-dashboard-streamlit) |

## 🧰 Tecnologias

- **Linguagens e Ferramentas**  
  - Python  
  - Jupyter Notebook  
  - Streamlit  
  - Git / GitHub  
  - Render (deploy)  

- **Bibliotecas Principais**  
  - Pandas  
  - NumPy  
  - Matplotlib, Seaborn, Plotly, Plotly Express  
  - SciPy  

- **Práticas Aplicadas**  
  - Análise exploratória de dados  
  - Testes de hipóteses  
  - Visualização interativa  
  - Desenvolvimento de dashboards  
  - Deploy de aplicações web

# Dashboard de Anúncios de Carros Usados

Este projeto é um aplicativo web interativo desenvolvido com Streamlit. Ele permite visualizar e explorar um conjunto de dados de anúncios de carros usados.

## Funcionalidades

- Visualização de histograma da quilometragem dos veículos (`odometer`)
- Gráfico de dispersão entre quilometragem e preço (`odometer` x `price`)
- Interface interativa com caixas de seleção

## Como executar

1. Instale as dependências:
    ```
    pip install streamlit pandas plotly
    ```

2. Execute o aplicativo:
    ```
    streamlit run app.py
    ```

## Deploy no Render

O arquivo `streamlit/config.toml` foi incluído para tornar o projeto compatível com o Render.

O link para acessar o app criado é https://projeto-sprint-5-carros-streamlit.onrender.com
https://github.com/gschmidel19
