import funcoes 

if __name__ == "__main__":
    print("Digite 1 se deseja limpar seu computador")
    opcao = input().strip()
    if opcao == "1":
        funcoes.limpar_temp()
        funcoes.limpar_prefetch()
        funcoes.esvaziar_lixeira()
        print("Limpeza concluída!")
    else:
        print("Opção inválida. Encerrando o programa.")