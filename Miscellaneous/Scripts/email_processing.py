from openai import OpenAI
from openai import OpenAIError

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

def call_openai_api(message):
    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-chat-v3.1:free",
            messages=[
                {"role": "system", "content": "Você é um assistente no setor financeiro da empresa, sua função é ler emails e responder da melhor forma, sendo profissional para emails profissionais e casual para emails casuais."},
                {"role": "user", "content": message}
            ],
            seed=42
        )
        return response.choices[0].message.content
    except OpenAIError as e:
        return f"Erro na chamada da API: {e}"

def main():
    message = "Assunto: Solicitação de Suporte Técnico – Operação FinanceiraPrezada Equipe de Suporte do Banco Alfa,Espero que esta mensagem os encontre bem.Venho por meio deste solicitar suporte técnico referente a uma operação financeira realizada em 15/08/2025, no valor de R$ 8.750,00, que apresentou o seguinte problema: o valor não foi creditado na conta de destino, mesmo constando como “transferência concluída” no aplicativo.Segue abaixo um resumo das informações para facilitar a análise:- Número da operação: 20250815‑XZ4729- Data e hora da transação: 15/08/2025 – 14h37- Meio utilizado: Aplicativo móvel – Banco Alfa- Descrição detalhada do problema: Após confirmar a transferência via PIX para a conta do cliente, recebi a notificação de conclusão, porém o beneficiário informa que o valor não consta em seu extrato. Já verifiquei os dados da chave PIX e estão corretos.- Comprovantes ou anexos: Comprovante de transferência em PDF e capturas de tela do histórico de transações (anexos a este e‑mail).Solicito, por gentileza, que a equipe técnica verifique o ocorrido e me informe sobre os próximos passos para a resolução. Caso sejam necessárias informações adicionais, estou à disposição para fornecê‑las.Agradeço antecipadamente pela atenção e aguardo retorno.Atenciosamente,Rodrigo SouzaAnalista FinanceiroEmpresa XPTO Ltda.(21) 99876‑5432 rodrigo.souza@email.com"
    response = call_openai_api(message)
    print(response)

if __name__=="__main__":
    main()
