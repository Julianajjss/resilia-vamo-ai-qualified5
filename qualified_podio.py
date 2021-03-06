def podio_olimpico (tempo_chegada1, tempo_chegada2, tempo_chegada3):

  if tempo_chegada1 > tempo_chegada2 > tempo_chegada3:
    primeiro_lugar = tempo_chegada3
    segundo_lugar = tempo_chegada2
    terceiro_lugar = tempo_chegada1
  
  elif tempo_chegada1 > tempo_chegada3 > tempo_chegada2:
    primeiro_lugar = tempo_chegada2
    segundo_lugar = tempo_chegada3
    terceiro_lugar = tempo_chegada1

  elif tempo_chegada2 > tempo_chegada3 > tempo_chegada1:
    primeiro_lugar = tempo_chegada1
    segundo_lugar = tempo_chegada3 
    terceiro_lugar = tempo_chegada2 

  elif tempo_chegada2 > tempo_chegada1 > tempo_chegada3:
    primeiro_lugar = tempo_chegada3
    segundo_lugar = tempo_chegada1
    terceiro_lugar = tempo_chegada2

  elif tempo_chegada3 > tempo_chegada1 > tempo_chegada2:
    primeiro_lugar = tempo_chegada2
    segundo_lugar = tempo_chegada1
    terceiro_lugar = tempo_chegada3

  elif tempo_chegada3 > tempo_chegada2 > tempo_chegada1:
    primeiro_lugar = tempo_chegada1
    segundo_lugar = tempo_chegada2
    terceiro_lugar = tempo_chegada3

  ordem = f'1 - {primeiro_lugar} minutos\n2 - {segundo_lugar} minutos\n3 - {terceiro_lugar} minutos\n'

  return ordem 
