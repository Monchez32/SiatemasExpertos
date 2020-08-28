import pandas as pd

df = pd.read_csv('winequality-red.csv', sep=';')
df.head()

def clasificar(parametro1, parametro2, parametro3):
    for i, n in enumerate(parametro2):
        if n >= parametro1:
            df.loc[i, parametro3] = 'alto'
        else:
            df.loc[i, parametro3] = 'bajo'
    return print (df.groupby(parametro3).quality.mean())

#Se envian las variables a la funcion clasificar 
Resultado_Alcohol = clasificar(df.alcohol.median(), df.alcohol, 'alcohol')
Resultado_Ph = clasificar(df.pH.median(), df.pH, 'ph')
Resultado_Residual_sugar = clasificar(df.residual_sugar.median(),
                                     df.residual_sugar, 'residualSugar')
Rresultado_Citric_acid = clasificar(df.citric_acid.median(), df.citric_acid,
                                   'citricAcid')


