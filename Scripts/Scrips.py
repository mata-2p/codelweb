# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
########## LIBRERÍAS A UTILIZAR ##########

#Se importan la librerias a utilizar
import numpy as np
import pandas as pd
from datetime import date
import tkinter as tk
from tkinter import filedialog


#from sklearn.model_selection import train_test_split
#from sklearn.linear_model import LogisticRegression
#from sklearn.svm import SVC
#from sklearn.neighbors import KNeighborsClassifier

#Se importa los datos a utilizar

root = tk.Tk()

root.withdraw()
file_path = filedialog.askopenfilename()

print(file_path)


url_rsso = r'file:///C:/Users/Mata/Desktop/RSSO.xlsx'

df_rsso = pd.read_excel(url_rsso)


#Se guardan los datos en un archivo para siempre tenerlos disponibles

dir_rsso = r'C:\Users\Mata\Documents/RSSO.csv'

df_rsso.to_csv(dir_rsso)

#Importar los datos de los archivos .csv almacenados

df_rsso = pd.read_csv(dir_rsso)

#print(df_rsso.head())




#####ENTENDIMIENTO DE LA DATA####

#Verifica la cantidad de datos que hay en el dataset

#print('Cantidad de datos:')
#print(df_rsso.shape)


#Verifica el tipo de datos que hay en el Dataset

#print('Tipos de datos:')
#print(df_rsso.info())


#Verifica datos faltantes que hay en el dataset

#print('Datos faltantes:')
#print(pd.isnull(df_rsso).sum())



##########PREPROCESAMIENTO DE LA DATA##########


#Cambio de nombres de columnas a numero para uso en formulas
#df_rsso.columns = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

#print(df_rsso.columns)



#Cambio los datos de Estandar en numeros
#df_rsso['Estandar'].replace(['EC1-Aislación y bloqueo',
#       'EC2-Trabajo en altura física',
#       'EC3-Maquinaria Industrial',
#       'EC4-Vehículos livianos',
#       'EC5-Equipos y herramientas portátiles y manuales',
#       'EC6-Materiales fundidos',
#       'EC7-Izaje mecánico de cargas',
#       'EC8-Guardas y protecciones de equipos',
#       'EC9-Manejo de sustancias peligrosas',
#       'EC10-Explosivos y tronaduras',
#       'EC11-Control de terreno',
#       'EC12-Incendio',
#       'EC13-Operaciones Ferroviarias',
#       'EC15-Bombeo agua barro',
#       'EC16-Estallido de roca',
#       'EC17-Control de Oxígeno y gases en Minería Subterránea',
#       'EC20-Puntos de vaciado y chimeneas',
#       'EC21-Vehículos de Transporte de cargas y Personas',
#       'EC22-Instalaciones Industriales y sus estructuras'],
#       [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], inplace=True)


#Cambio los datos de Estandar en Texto
#df_rsso['Estandar'].replace([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],['EC1-Aislación y bloqueo',
#       'EC2-Trabajo en altura física',
#       'EC3-Maquinaria Industrial',
#       'EC4-Vehículos livianos',
#       'EC5-Equipos y herramientas portátiles y manuales',
#       'EC6-Materiales fundidos',
#       'EC7-Izaje mecánico de cargas',
#       'EC8-Guardas y protecciones de equipos',
#       'EC9-Manejo de sustancias peligrosas',
#       'EC10-Explosivos y tronaduras',
#       'EC11-Control de terreno',
#       'EC12-Incendio',
#       'EC13-Operaciones Ferroviarias',
#       'EC15-Bombeo agua barro',
#       'EC16-Estallido de roca',
#       'EC17-Control de Oxígeno y gases en Minería Subterránea',
#      'EC20-Puntos de vaciado y chimeneas',
#      'EC21-Vehículos de Transporte de cargas y Personas',
#      'EC22-Instalaciones Industriales y sus estructuras'], inplace=True)



#Cambio los datos de Riesgo Critico en numeros
#df_rsso['Riesgo_Critico'].replace(['RC1: Contacto con energía eléctrica en Intervención de Equipo Eléctrico',
#'RC2: Caída de distinto nivel por trabajos en altura física.',
#'RC3: Aplastamiento por movimiento de carga suspendida/maniobras de izaje',
#'RC4: Contacto con energías peligrosas por liberación descontrolada (neumática, hidráulica,',
#'RC5: Caída de rocas,derrumbes, colapso de talud, falla de pilas mina rajo, botadero, pilas',
#'RC6: Incendio (mina subterránea) plantas SX',
#'RC7: Contacto con Ácido Sulfúrico concentrado',
#'RC8: Explosión por manejo, transporte, uso (tronadura) o almacenamiento de explosivos',
#'RC9: Atrapamiento en equipos con piezas o partes móviles',
#'RC10: Choques, colisiones, atropellos y volcamientos por conducción de vehículos o equipos',
#'RC11: Exposición a atmósferas peligrosas/falta de oxígeno/asfixia/intoxicaciones/gases y v',
#'RC12: Contacto o radiación con material fundido/temperaturas extremas',
#'RC13: Caída de objeto desde distinto nivel (herramientas/trabajos simultáneos)',
#'RC14: Operación ferroviaria',
#'RC15: Avalanchas/aludes',
#'RC16: Caída a pique',
#'RC17: Bombeo Agua Barro',
#'RC18: Atrapamiento por caída de roca/planchoneo (control de terreno)',
#'RC19: Estallido de roca',
#'RC20: Exposición a polvo con contenido de Sílice sobre límite permisible',
#'RC21: Exposición a Arsénico Inorgánico(generado en tostación y fundición)',
#'RC22: Caída a distinto nivel por colapso de estructura de piso, escaleras y barandas'],
#       [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],inplace=True)



#Cambio los datos de Riesgo Critico a Texto
#df_rsso['Riesgo Critico'].replace([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],
#['RC1: Contacto con energía eléctrica en Intervención de Equipo Eléctrico',
#'RC2: Caída de distinto nivel por trabajos en altura física.',
#'RC3: Aplastamiento por movimiento de carga suspendida/maniobras de izaje',
#'RC4: Contacto con energías peligrosas por liberación descontrolada (neumática, hidráulica,',
#'RC5: Caída de rocas,derrumbes, colapso de talud, falla de pilas mina rajo, botadero, pilas',
#'RC6: Incendio (mina subterránea) plantas SX',
#'RC7: Contacto con Ácido Sulfúrico concentrado',
#'RC8: Explosión por manejo, transporte, uso (tronadura) o almacenamiento de explosivos',
#'R#C9: Atrapamiento en equipos con piezas o partes móviles',
#'RC10: Choques, colisiones, atropellos y volcamientos por conducción de vehículos o equipos',
#'RC11: Exposición a atmósferas peligrosas/falta de oxígeno/asfixia/intoxicaciones/gases y v',
#'RC12: Contacto o radiación con material fundido/temperaturas extremas',
#'RC13: Caída de objeto desde distinto nivel (herramientas/trabajos simultáneos)',
#'RC14: Operación ferroviaria',
#'RC15: Avalanchas/aludes',
#'RC16: Caída a pique',
#'RC17: Bombeo Agua Barro',
#'RC18: Atrapamiento por caída de roca/planchoneo (control de terreno)',
#'RC19: Estallido de roca',
#'RC20: Exposición a polvo con contenido de Sílice sobre límite permisible',
#'RC21: Exposición a Arsénico Inorgánico(generado en tostación y fundición)',
#'RC22: Caída a distinto nivel por colapso de estructura de piso, escaleras y barandas'],inplace=True)





#Cambio los datos de Nivel RSSO  en números
#df_rsso['Nivel_RSSO'].replace(['Nivel 1'],[0],inplace=True)


#Cambio los datos de Tipo_RSSO  en números
df_rsso['Tipo RSSO'].replace(['Medio Ambiental','Seguridad','Salud'],[0,1,2],inplace=True)


#df_rsso['Tipo_RSSO'].replace([0,1,2],['Medio Ambiental','Seguridad','Salud'],inplace=True)

#eliminar todas las filas cuyo valor sea Medio Ambiental y Salud
df_rsso = df_rsso.drop(df_rsso[df_rsso['Tipo RSSO']==0].index)
df_rsso = df_rsso.drop(df_rsso[df_rsso['Tipo RSSO']==2].index)

#Se transforma las filas con los datos de Seguridad a Texto
df_rsso['Tipo RSSO'].replace([1],['Seguridad'],inplace=True)

#Se elimina la Columna con los datos que no aplican en Estandar
df_rsso = df_rsso.drop(['Unnamed: 0'], axis=1)

#Se elimina las filas con los datos que no aplican en Estandar
df_rsso = df_rsso.drop(df_rsso[df_rsso['Estandar']=='No aplica -'].index)

#Se elimina las filas con los datos de Riesgo Critico
df_rsso = df_rsso.drop(df_rsso[df_rsso['Riesgo Critico']=='EC16-Estallido de rocarty'].index)


#Se transforma las filas con los datos de Nivel RSSO a Texto
#df_rsso['Nivel_RSSO'].replace([0],['Nivel 1'],inplace=True)

#Se elimina las filas con los datos perdidos
#df_rsso.dropna(axis=0, how='any', inplace=True)


#print('Tipos de datos:')
#print(df_rsso.info())


########Preprocemaciento de las Columnas#######

#Cambio de nombres de columnas a texto para uso en formulas
df_rsso.columns = ['Codigo_RSSO',
 'Tipo_RSSO', 
 'Estado',
 'Causal',
 'Nivel_RSSO',
 'Fecha_Creacion',
 'Fecha_Hallazgo',
 'Division',
 'Gerencia',
 'SuperIntendencia',
 'Area',
 'SAP_Informante',
 'Informante',
 'SAP_Responsable',
 'Responsable',
 'Fecha_Cierre',
 'Descripcion_Incidente',
 'Accion_Realizada',
 'Estandar',
 'Riesgo_Critico']



#resetear el index del DataFrame
df_rsso = df_rsso.reset_index(drop=True)


######VERIFICO LOS DATOS######

#print(pd.isnull(df_rsso).sum())

#print(df_rsso.shape)

#print(df_rsso.head())





########Calificadores#########

#Calificar Datos Vacios
df_rsso['tiene datos vacios ?'] = np.where(df_rsso[pd.isnull(df_rsso).any(axis=1)] == True  , 'Si', 'No')



#Calificar largo Descripcion
df_rsso['Cumple largo de la Descripcion'] = np.where(df_rsso['Descripcion_Incidente'].str.len()>=200, 'Si', 'No')


#Calificar Fecha maximo 2 dias
df_rsso["Fecha_Hallazgo"] = pd.to_datetime(df_rsso["Fecha_Hallazgo"])
df_rsso["Fecha_Hallazgo"].dt.day


df_rsso["Fecha_Cierre"] = pd.to_datetime(df_rsso["Fecha_Cierre"])
df_rsso["Fecha_Cierre"].dt.day


f1=df_rsso["Fecha_Hallazgo"].dt.day
f2=df_rsso["Fecha_Cierre"].dt.day

diferencia= f2-f1

#print (diferencia)

df_rsso['Cumple los 2 dias de solucion ?'] = np.where(diferencia<=2, 'Si', 'No')



# Para seleccionar solamente las filas con valores NaN, podemos utilizar el método 'any()'
#df_rsso[pd.isnull(df_rsso).any(axis=1)]

# selecciona las columanas que tengan datos vacios
#empty_weights = surveys_df[pd.isnull(surveys_df['weight'])]['weight']


#print(empty_weights)

#Calificar Datos Vacios
#nan = df_rsso.rows.isnull()
#print (nan)






#####Calificar Reportes si Cumplen con todas las calificaciones #########

#Transformar valores a numeros
df_rsso['Cumple largo de la Descripcion'].replace(['No','Si'],[0,1],inplace=True)
df_rsso['Cumple los 2 dias de solucion ?'].replace(['No','Si'],[0,1],inplace=True)

#Operacion matematica
c1 = df_rsso['Cumple largo de la Descripcion']
c2 = df_rsso['Cumple los 2 dias de solucion ?']
s= c1+c2
#Algoritmo
df_rsso['El reporte es de calidad ?'] = np.where(s==2, 'Si', 'No')

#Transformar datos a texto para mejor entendimiento
df_rsso['Cumple largo de la Descripcion'].replace([0,1],['No','Si'],inplace=True)
df_rsso['Cumple los 2 dias de solucion ?'].replace([0,1],['No','Si'],inplace=True)





######Exportar archivo nuevo#######
#Nombre del nuevo archivo y ruta
dir_rsso = r'C:\Users\Mata\Downloads\RSSO.xlsx'
#exportar a tipo excel
df_rsso.to_excel(dir_rsso)












