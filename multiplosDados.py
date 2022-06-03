import pandas as pd

def qsa(dict):
    responsaveis = [i['nome'] for i in dict['qsa']]
    cargos = [i['qual'] for i in dict['qsa']]
    df_responsaveisCargos = pd.DataFrame(list(zip(responsaveis,cargos)),columns=['Nome','Cargo'])
    return df_responsaveisCargos

def atividade(dict):
    atividadePrincipal = [i['code'] for i in dict['atividade_principal']]
    textoPrincipal = [i['text'] for i in dict['atividade_principal']]
    atividadeSecundaria = [i['code'] for i in dict['atividades_secundarias']]
    textoSecundario = [i['text'] for i in dict['atividades_secundarias']]
    df_tiposAtividades = pd.DataFrame(list(zip(atividadePrincipal,textoPrincipal,atividadeSecundaria,textoSecundario)),columns=['Atividade_Principal','Texto_Principal',
                                                                                                                  'Atividade_Secundária','Texto_Secundário'])
    return df_tiposAtividades






