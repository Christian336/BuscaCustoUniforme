#Mapa/Grafo

mapa = {
    'Brasília': [('Belo Horizonte' , 600) , ('Fortaleza' , 1600)],
    'Belo Horizonte' : [('Brasília' , 600), ('Cuiabá' , 1373) , ('Rio de Janeiro' , 340) , ('São Paulo' , 490)],
    'Cuiabá' : [('Belo Horizonte' , 1373) , ('Manaus' , 1453) , ('Rio de Janeiro' , 1576)],
    'Curitiba' : [('Florianópolis' , 251) , ('Rio de Janeiro' , 676) , ('São Paulo' , 339)],
    'Florianópolis' : [('Curitiba' , 251) , ('Porto Alegre' , 376)],
    'Fortaleza' : [('Brasília' , 1600) , ('Manaus' , 2384) , ('Salvador' , 1028)],
    'Manaus': [('Cuiabá' , 1453) , ('Fortaleza' , 2384)],
    'Porto Alegre' : [('Florianópolis' , 376) , ('São Paulo' , 852)],
    'Rio de Janeiro' : [('Belo Horizonte' , 340) , ('Cuiabá' , 1576) , ('Curitiba' , 676)],
    'Salvador' : [('Fortaleza' , 1028) , ('São Paulo' , 1454)],
    'São Paulo' : [('Belo Horizonte' , 490) , ('Curitiba' , 339) , ('Porto Alegre' , 852) , ('Salvador' , 1454)]
}

cidades = ['Brasília', 'Belo Horizonte', 'Cuiabá', 'Curitiba', 'Florianópolis', 'Fortaleza', 'Manaus', 'Porto Alegre', 'Rio de Janeiro', 'Salvador', 'São Paulo']
