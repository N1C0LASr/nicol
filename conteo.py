# conteo de votos

import Candidato
# inicializar 10 variables (contador)
v1=0; v2=0; v3=0; v4=0; v5=0; v6=0; v7=0; v8=0; v9=0; v10=0
# obtener todos los votos:
for i in range(1,10):
    # recuperar nro. del candidato
    nc= Candidato.getVotos(i)
    
