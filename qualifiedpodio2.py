def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3, nome_corredor1, nome_corredor2, nome_corredor3):
  
  if tempo_chegada1 <= tempo_chegada2 and tempo_chegada2 <=      tempo_chegada3:
    primeiro_tempo = tempo_chegada1
    segundo_tempo = tempo_chegada2
    terceiro_tempo = tempo_chegada3
    primeiro_nome = nome_corredor1
    segundo_nome = nome_corredor2
    terceiro_nome = nome_corredor3
  
  elif tempo_chegada2 <= tempo_chegada1 and tempo_chegada1 <=  tempo_chegada3:
    primeiro_tempo = tempo_chegada2
    segundo_tempo = tempo_chegada1
    terceiro_tempo = tempo_chegada3
    primeiro_nome = nome_corredor2
    segundo_nome = nome_corredor1
    terceiro_nome = nome_corredor3

  elif tempo_chegada3 <= tempo_chegada1 and  tempo_chegada1 <=  tempo_chegada2:
    primeiro_tempo = tempo_chegada3
    segundo_tempo = tempo_chegada1
    terceiro_tempo = tempo_chegada2
    primeiro_nome = nome_corredor3
    segundo_nome = nome_corredor1
    terceiro_nome = nome_corredor2

  elif tempo_chegada1 <= tempo_chegada3 and tempo_chegada3 <=  tempo_chegada2:
    primeiro_tempo = tempo_chegada1
    segundo_tempo = tempo_chegada3
    terceiro_tempo = tempo_chegada2
    primeiro_nome = nome_corredor1
    segundo_nome = nome_corredor3
    terceiro_nome = nome_corredor2

  elif tempo_chegada2 <= tempo_chegada3 and tempo_chegada3 <=  tempo_chegada1:
    primeiro_tempo = tempo_chegada2
    segundo_tempo = tempo_chegada3
    terceiro_tempo = tempo_chegada1
    primeiro_nome = nome_corredor2
    segundo_nome = nome_corredor3
    terceiro_nome = nome_corredor1
  
  else:
    primeiro_tempo = tempo_chegada3
    segundo_tempo = tempo_chegada2
    terceiro_tempo = tempo_chegada1
    primeiro_nome = nome_corredor3
    segundo_nome = nome_corredor2
    terceiro_nome = nome_corredor1
     
  return(f'1 - {primeiro_nome} - {primeiro_tempo} minutos\n'
         f'2 - {segundo_nome} - {segundo_tempo} minutos\n'
         f'3 - {terceiro_nome} - {terceiro_tempo} minutos\n')
      
print (podio_olimpico(300,110,120,'Wanderlei Cordeiro de Lima','Eliud Kipchog','Ronaldo'))