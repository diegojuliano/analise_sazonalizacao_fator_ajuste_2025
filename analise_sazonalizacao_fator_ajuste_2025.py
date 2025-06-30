# %% Importações
import pandas as pd
import matplotlib.pyplot as plt
import os

# %% Caminhos absolutos
caminho_csv = r'F:\10 - Projetos\14 - Analises de Dados\01 - Setor eletrico\analise_sazonalizacao_fator_ajuste_2025\dados\sazonalizacao_mre_gf_fator_ajuste_2025.csv'
caminho_imagens = r'F:\10 - Projetos\14 - Analises de Dados\01 - Setor eletrico\analise_sazonalizacao_fator_ajuste_2025\imagens\\'

# %% Criar pasta imagens se não existir
if not os.path.exists(caminho_imagens):
    os.makedirs(caminho_imagens)

# %% Leitura do CSV
df = pd.read_csv(caminho_csv, delimiter=';', encoding='utf-8')

# %% Pré-processamento
df['MES_REFERENCIA'] = pd.to_datetime(df['MES_REFERENCIA'].astype(str), format='%Y%m')

# %% Gráfico 1: Evolução da Garantia Física Sazonalizada
plt.figure(figsize=(10, 6))
plt.plot(df['MES_REFERENCIA'], df['GARANTIA_FISICA_SAZONALIZADA'], marker='o', color='darkblue')
plt.title('Evolução da Garantia Física Sazonalizada - 2025', fontsize=14)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('MW médios', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig(caminho_imagens + 'evolucao_gf_sazonalizada.png', dpi=300)
plt.close()

# %% Gráfico 2: Lastro MRE vs Fora do MRE
plt.figure(figsize=(10, 6))
plt.plot(df['MES_REFERENCIA'], df['GARANTIA_FISICA_LASTRO_USINA_MRE'], label='Lastro MRE', marker='o', color='green')
plt.plot(df['MES_REFERENCIA'], df['GARANTIA_FISICA_LASTRO_USINA_FORA_MRE'], label='Lastro Fora do MRE', marker='s', color='orange')
plt.title('Lastro MRE vs Fora do MRE - 2025', fontsize=14)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('MW médios', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig(caminho_imagens + 'lastro_mre_vs_fora_mre.png', dpi=300)
plt.close()

# %% Gráfico 3: Percentual MRE e Fora do MRE sobre Sazonalizada
df['perc_mre'] = (df['GARANTIA_FISICA_LASTRO_USINA_MRE'] / df['GARANTIA_FISICA_SAZONALIZADA']) * 100
df['perc_fora_mre'] = (df['GARANTIA_FISICA_LASTRO_USINA_FORA_MRE'] / df['GARANTIA_FISICA_SAZONALIZADA']) * 100

plt.figure(figsize=(10, 6))
plt.stackplot(df['MES_REFERENCIA'], df['perc_mre'], df['perc_fora_mre'],
              labels=['MRE (%)', 'Fora MRE (%)'],
              colors=['green', 'orange'],
              alpha=0.7)
plt.title('Percentual do Lastro MRE e Fora do MRE sobre a Garantia Física Sazonalizada - 2025', fontsize=14)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Percentual (%)', fontsize=12)
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig(caminho_imagens + 'percentual_mre_vs_fora_mre.png', dpi=300)
plt.close()

print("✅ Gráficos gerados com sucesso em:", caminho_imagens)
