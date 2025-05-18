ACP=99
ERR=-1
idx=0
renC = 1
colC = 0
entrada = ''
tData = ''
errB = False
bImp = False
conCod = 1
tabSim  = {}
codProg = {}
IdEti = 0
matran=[
    #           tab  +,-
    #           sp   *                        ==        
    #_,let  dig nl   /     %   .    "   del  ops   >    <,   #    Sym
    [1,     2,   0,   5,   6, ERR,   9,  11,  16,  14,  15,  12,  18],  # #0
    [1,     1, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # #1
    [ACP,   2, ACP, ACP, ACP,   3, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # #2
    [ERR,   4, ERR, ERR, ERR, ERR, ERR, ERR, ERR, ACP, ACP, ACP, ACP],  # #3
    [ACP,   4, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # #4
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # #5
    [ACP, ACP, ACP, ACP,   7, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # #6
    [7,     7,   7,   7,   7,   7,   7,   7,   7,   7,   7, ACP,   7],  # #7
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # #8
    [9,     9,   9,   9,   9,   9,  10,   9,   9,   9,   9, ACP,   9],  # #9
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # #10
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # #11
    [ 12,  12,  12,  12,  12,  12,  12,  12,  12,  12,  12,  13,  12],  # #12
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # #13
    [1,     2, ACP,   5, ACP, ERR, ACP, ERR,  17, ACP, ACP, ACP, ACP],  # #14
    [1,     2, ACP,   5, ACP, ERR, ACP, ERR,  17, 17,  ACP, ACP, ACP],  # #15
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP,  17, ACP, ACP, ACP, ACP],  # #16
    [ACP, ACP, ACP, ERR, ACP, ERR, ACP, ERR, ACP, ACP, ACP, ACP, ACP],  # #17
    [ACP, ACP, ACP, ACP, ACP, ERR, ACP, ERR, ACP, ACP, ACP, ACP, ACP]   # #18
]

opLog=['y', 'no', 'o']
cteLog=['falso', 'verdadero']
palRes=['interrumpe', 'si',  'sino',   'funcion',  
        'entera', 'decimal', 'lógica', 'alfabetica',
        'constante', 'hasta', 'hacer', 'incr', 
        'inicio', 'fin','continua', 'desde',
        'regresa', 'variable', 'que', 'mientras', 
        'lmp', 'imprime', 'lee', 'imprimeln', 'principal']

mapTipos={
    'E=E': '', 'A=A': '', 'D=D':'', 'D=E':'', 'L=L': '',
    'A+A': 'A', 'E+E': 'E', 'E+D': 'D', 'D+E':'D', 'D+D': 'D', 
    'E-E': 'E', 'E-D': 'D', 'D-E':'D', 'D-D': 'D',
    'E*E': 'E', 'E*D': 'D', 'D*E':'D', 'D*D': 'D',     
    'E/E': 'D', 'E/D': 'D', 'D/E':'D', 'D/D': 'D',
    'E%E': 'E',     
    'E^E': 'D', 'E^D': 'D', 'D^E':'D', 'D^D': 'D',
     '-E': 'E', '-D': 'D',     
    'E<E': 'L', 'E<D': 'L', 'D<E':'L', 'D<D': 'L', 'A<A': 'L',
    'E<=E': 'L', 'E<=D':'L', 'D<=E': 'L', 'D<=D': 'L', 'A<=A':'L',
    'E>E' : 'L', 'E>D' :'L', 'D>E' : 'L', 'D>D' : 'L', 'A>A' :'L',
    'E>=E': 'L', 'E>=D':'L', 'D>=E': 'L', 'D>=D': 'L', 'A>=A':'L',
    'E<>E': 'L', 'E<>D':'L', 'D<>E': 'L', 'D<>D': 'L', 'A<>A':'L',
    'E==E': 'L', 'E==D':'L', 'D==E': 'L', 'D==D': 'L', 'A==A':'L',
    'noL' : 'L', 'LyL' :'L', 'LoL' : 'L'
    }
#A es alfabefica, E es entera, D es decimal, L es logica, 

pilaTipos=[]

def tipoResul(key):
    global renC, colC
    try:
        tip = mapTipos[key]
        if tip != '':
            pilaTipos.append(tip)
    except KeyError:
        erra(renC, colC, 'Error Semantico', 'Conflicto en tipos NO opera '+key)
        #if not (key in ['A=A', 'L=L', 'E=E', 'D=D', 'D=E']):
        if key[1] != '=':
            pilaTipos.append('I')

def buscaInsTipo(ide):
    global tabSim, renC, colC
    try:
       o = tabSim[ide]
       pilaTipos.append(o[1])
    except KeyError:
        erra(renC,colC,'Error de Semantica', 'Identificador '+ide+' No declarado')
    

def insTabSim(key, data):
    global tabSim
    tabSim[key] = data

def insCodigo(code):
    global codProg, conCod
    codProg[conCod] = code  
    conCod += 1 

def nomEti():
    global IdEti
    IdEti +=1
    return '_E' + str(IdEti) 

def colCar( c ):
    if c == '_' or c.isalpha(): return 0
    if c.isdigit()            : return 1
    if c in ['\n', ' ', '\t'] : return 2
    if c in ['+', '-', '*', 
                     '/', '^']: return 3
    if c == '%'               : return 4
    if c == '.'               : return 5
    if c == '"'               : return 6
    if c in ['[', ']', '{', 
             '}', ',', ';', ':', 
             '(', ')']        : return 7
    if c == '='               : return 8
    if c == '>'               : return 9
    if c == '<'               : return 10
    if c == '#'               : return 11 
    if c == ['$', '¿', '¡',
     '?', '!']                : return 12 
    return ERR

def erra(ren, col, tipE, desE):
    global errB
    print("["+str(ren)+"]["+str(col)+"]", tipE, desE)
    errB = True

def lexical():
    global idx, entrada, renC, colC
    estado = 0
    estAnt = 0
    col = 0
    lex = ''
    tok = ''
    while idx < len(entrada) and estado != ERR and estado != ACP:
        x = entrada[idx]
        if x == '\n' and estado in [0, 7, 9, 12]:
            renC += 1
            colC = 0
        elif x == '\t' and estado == 0: 
            colC += 3
        else:
            colC += 1 
        idx += 1
        col = colCar(x)
        if col >= 0 and col <= 12:
            if estado == 7:
                lex = ''
                if x == '\n':
                    estado = 8
            else:
                estado = matran[estado][col]
            if estado not in [ERR, ACP]:
                estAnt = estado
                if estado == 9 or (estado not in [7, 9, 12] and x not in [' ', '\t', '\n']):
                    lex += x

    #Clasificacion de Tokens, Lexemas
    if estado in [ACP, ERR]:
        idx -= 1
    else: estAnt = estado
    if estAnt == 3:
        tok = 'Dec'
        erra(renC, colC, "Error Lexico", "constante DECIMAL sin cerrar " + lex)
    elif estAnt == 9:
        tok = 'CtA'
        erra(renC, colC, "Error Lexico", "constante Alfabetica sin cerrar ")
    if estAnt == 12:
        tok = 'Cml' 
        erra (renC, colC, "Error Lexico", "Comentario de multiple linea sin cerrar")
    if estAnt == 1:
        tok='Ide'
        if   lex in cteLog: tok = 'CtL'
        elif lex in opLog : tok = 'OpL'
        elif lex in palRes: tok = 'Res'
    elif estAnt == 2:
        tok = 'Ent'
    elif estAnt == 4:
        tok = 'Dec'
    elif estAnt in [5, 6]:
        tok = 'OpA'
    elif estAnt == 7:
        tok = 'CdL'
    elif estAnt == 8:
        tok = 'Com'
    elif estAnt == 10:
        tok = 'CtA'
    elif estAnt == 11:
        tok = 'Del'
    elif estAnt == 13:
        tok = 'Cml'
    elif estAnt in [14, 15, 17]:
        tok = 'OpR'
    elif estAnt == 16:
        tok = 'OpS'
    elif estAnt == 18:
        tok = 'Sys'

    return tok, lex

def lexico():
    tok, lex = lexical()
    while tok in ['Com', 'Cml']:
        tok, lex = lexical()
    
    return tok, lex

def bloque():
    global toke, lexe, renC, colC
    
    if lexe != 'inicio':
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba inicio llego ' + lexe)
    
    if lexe != 'fin':
        estatutos()
        
    if lexe != 'fin':
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba fin llego ' + lexe)
        
    toke, lexe = lexico()  

# Dimensiones de arreglos o variables o constantes xd alv 
def dimen(): 
    global toke, lexe, renC, colC, tabSim
    dime = '0'
    toke, lexe = lexico()
    
    if toke == 'Ent':
        # Si es un entero literal, usarlo directamente
        dime = lexe
    elif toke == 'Ide':
        # Si es un identificador, verificar si es una constante y obtener su valor
        nIde = lexe
        if nIde in tabSim:
            info = tabSim[nIde]
            if info[0] == 'C':  # Es una constante
                dime = info[2]  # Obtener el valor
            else:
                erra(renC, colC, 'Error Semántico', 'Se esperaba una constante para la dimensión: ' + nIde)
        else:
            erra(renC, colC, 'Error Semántico', 'Identificador no declarado: ' + nIde)
    else:
        erra(renC, colC, 'Error de Sintaxis', 'Se esperaba una constante entera o identificador y llegó ' + lexe)
    
    toke, lexe = lexico()
    if lexe != ']':
        erra(renC, colC, 'Error de Sintaxis', 'Se esperaba una ] y llegó ' + lexe)
    
    toke, lexe = lexico()
    return dime

def ctes(): 
    global toke, lexe, renC, colC, tData

    # 📌 Validación de constantes según su tipo
    if tData == 'A':  # Alfabética debe estar entre comillas
        if toke != 'CtA':
            erra(renC, colC, 'Error de Sintaxis', 'Se esperaba una constante alfabetica entre comillas y llegó ' + lexe)
            return ''
    elif tData == 'L':  # Lógica debe ser "verdadero" o "falso"
        if toke != 'CtL':
            erra(renC, colC, 'Error de Sintaxis', 'Se esperaba una constante lógica (verdadero/falso) y llegó ' + lexe)
            return 'falso'  # Por defecto falso si hay error
    elif tData == 'E':  # Entero debe ser un número
        if toke != 'Ent':
            erra(renC, colC, 'Error de Sintaxis', 'Se esperaba una constante entera y llegó ' + lexe)
            return '0'
    elif tData == 'D':  # Decimal debe ser un número con punto flotante
        if toke != 'Dec':
            erra(renC, colC, 'Error de Sintaxis', 'Se esperaba una constante decimal y llegó ' + lexe)
            return '0.0'

    valor = lexe  # Guarda el valor de la constante
    toke, lexe = lexico()  # Avanza al siguiente token
    return valor  # Devuelve el valor de la constante

""" global toke, lexe, renC, colC, bImp, conCod, tData
    
    valores = []
    deli = ','
    while deli == ',':
        toke, lexe = lexico()
        print(f'Toke: {toke}  Lexe: {lexe}')

        # Verificar que sea un tipo valido (Entera, Decimal, Alfabetica o Logica)
        if toke not in ['Ent', 'Dec', 'CtA', 'CtL']:
            erra(renC, colC, 'Error de sintaxis,', 'se esperaba una constante válida y llegó ' + lexe)
            return  # Termina la función en caso de error
        
        valores.append(lexe)
        toke, lexe = lexico()

        if lexe == ',':
            #deli = lexe
            #toke, lexe = lexico()
            deli = lexe
        else:
            deli = ''

    return valores """
def ctess():
    global toke, lexe, renC, colC, tabSim, tData

    deli = ','
    while deli == ',':
        ctes()
        deli = lexe
        if deli == ',':
            toke, lexe = lexico()
    #toke, lexe = lexico()

def const():
    global toke, lexe, renC, colC, tabSim, tData
    toke, lexe = lexico()  # Avanza al siguiente token
    tipo()  # Obtiene el tipo de la constante (entera, decimal, lógica, alfabetica)
    deli = ','  # Para manejar múltiples constantes en una línea
    while deli == ',':
        deli = ';'
        nIde = lexe  
        if toke != 'Ide':
            erra(renC, colC, 'Error de Sintaxis', 'Se esperaba un Identificador y llegó ' + lexe)
        toke, lexe = lexico()  
        if lexe != '=':
            erra(renC, colC, 'Error de Sintaxis', 'Se esperaba "=" en la declaración de la constante ' + nIde)
        toke, lexe = lexico()  
        valor = ctes()

        tabSim[nIde] = ['C', tData, valor, '0']  
        if lexe == ',':
            deli = lexe
            toke, lexe = lexico() 
    if lexe != ';':
        erra(renC, colC, 'Error de Sintaxis', 'Se esperaba ";" y llegó ' + lexe)
    toke, lexe = lexico() 

def vars(): 
    global toke, lexe, renC, colC, bImp, conCod, tData
    toke, lexe = lexico()
    tipo()
    deli = ','
    while deli == ',':
        dim1 = '0'
        deli = ';'
        nIde = lexe
        if toke != 'Ide':
            erra(renC, colC, 'Error de Sintaxis', 'se esperaba Identificador y llego ' + lexe)
        toke, lexe = lexico()
        if lexe == '[': 
            dim1=dimen()
            #print('Vars' +lexe)
            #print(dim1)
        if lexe == '=': 
            toke, lexe = lexico()
            if lexe == '{':
                toke, lexe = lexico()
                ctess() 
                if lexe != '}':
                    erra(renC, colC, 'Error de Sintaxis', 'se esperaba } y llego ' + lexe)
                toke, lexe = lexico()
            else:
                if not( toke in ['Ent', 'Dec', 'CtA', 'CtL']):
                    erra(renC, colC, 'Error de Sintaxis', 'se esperaba Constante y llego ' + lexe)
                toke, lexe = lexico()
        insTabSim(nIde,['V', tData, dim1, '0'])
        if lexe == ',': 
            deli = lexe
            toke, lexe = lexico()

    if lexe != ';':
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba ; y llego ' + lexe)
    toke, lexe = lexico()

def varconst(): 
    global toke, lexe, renC, colC, bImp, conCod
    if lexe == 'constante': const()
    elif lexe == 'variable': vars()

def eInterrumpe():
    global toke, lexe, renC, colC, bImp, conCod
    
    toke, lexe = lexico()

def eRegresa():
    global toke, lexe, renC, colC, bImp, conCod
    
    toke, lexe = lexico()
    expr()  # Evaluar la expresión de retorno
    

def eContinua():
    global toke, lexe, renC, colC, bImp, conCod

    toke, lexe = lexico()


def eSi():
    global toke, lexe, renC, colC, bImp, conCod
    
    toke, lexe = lexico()
    expr()  

    # Exigir "hacer"
    if lexe != 'hacer':
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba hacer y llego ' + lexe)
    
    if lexe == 'inicio':
        bloque()

    toke, lexe = lexico()

    # Guardar posición para salto condicional
    pos_jmc = conCod
    insCodigo(['JMC', 'F', '0'])  # Salta si falso
    
    # Guardar posición para salto incondicional (saltar el "sino")
    pos_jmp = conCod
    insCodigo(['JMP', '0', '0'])
    
    # Actualizar el destino del salto condicional
    codProg[pos_jmc][2] = str(conCod)
    
    # Verificar si hay "sino"
    if lexe == 'sino':
        toke, lexe = lexico()
        
        if lexe == 'inicio':
            bloque()

    toke, lexe = lexico()
    
    # Actualizar el destino del salto incondicional
    codProg[pos_jmp][2] = str(conCod)
    
def eMientras():
    global toke, lexe, renC, colC, conCod, codProg, IdEti
    ItiFin = nomEti()
    # Leer la condición del ciclo
    toke, lexe = lexico()
    posInicio = conCod
    expr()  # Evaluar la expresión lógica
    tipo = pilaTipos.pop()  # Validar el tipo lógico
    if tipo != 'L':
        erra(renC, colC, 'Error de Tipos', 'Se esperaba una expresión lógica, pero se obtuvo: ' + tipo)
    # Marcar inicio del ciclo
    #posInicio = conCod
    #insCodigo(['NOP', '0', '0'])  # Etiqueta inicial del ciclo
    # Generar salto condicional al final del ciclo
    posJMC = conCod
    insCodigo(['JMC', 'F', '_E1'])  # Salto si la condición es falsa
    # Validar bloque de "mientras"
    if lexe != 'inicio':
        erra(renC, colC, 'Error de Sintaxis', 'Se esperaba "inicio", pero se encontró: ' + lexe)
    toke, lexe = lexico()
    
    while lexe != 'fin':
        comando()
        toke, lexe = lexico()
    # Generar salto al inicio del ciclo
    insCodigo(['JMP', '0', str(posInicio)])   
    posJMC = conCod #Posicion Final 
    # Etiqueta final del ciclo
    # insCodigo(['NOP', '_E1', '0'])
    # Avanzar después de "fin"
    toke, lexe = lexico()
    insTabSim(ItiFin,['E', 'I', str(posJMC), '0'])

def eRepite():
    global toke, lexe, renC, colC, conCod, codProg, pilaTipos, tabSim
    ItiFin = nomEti()
    posInicio = conCod
    # No generar NOP, solo guardar la posición de inicio
    if lexe != 'repite':
        erra(renC, colC, 'Error de Sintaxis', 'Se esperaba "repite" y llegó: ' + lexe)
        return
    toke, lexe = lexico()
    if lexe == 'inicio':
        block()
        toke, lexe = lexico()
    else:
        while lexe not in ['hasta', 'fin']:
            comando()
            if lexe == ';':
                toke, lexe = lexico()
    if lexe != 'hasta':
        erra(renC, colC, 'Error de Sintaxis', 'Se esperaba "hasta" y llegó: ' + lexe)
        return
    toke, lexe = lexico()
    if lexe != 'que':
        erra(renC, colC, 'Error de Sintaxis', 'Se esperaba "que" y llegó: ' + lexe)
        return
    toke, lexe = lexico()
    expr()
    if len(pilaTipos) == 0:
        erra(renC, colC, 'Error de Tipos', 'Falta tipo lógico en pila.')
        return
    tipoCond = pilaTipos.pop()
    if tipoCond != 'L':
        erra(renC, colC, 'Error de Tipos', 'Se esperaba una expresión lógica, pero se obtuvo: ' + tipoCond)
        return
    # Generar el salto condicional al inicio si la condición es falsa
    insCodigo(['JMC', 'F', str(posInicio)])
    # Avanzar después de "hasta"
    toke, lexe = lexico()
    # Registrar la etiqueta en la tabla de símbolos con la posición actual
    insTabSim(ItiFin, ['E', 'I', str(conCod), '0'])

def eDesde():
    global toke, lexe, renC, colC, conCod, codProg
    # Leer variable inicial del ciclo
    toke, lexe = lexico()
    varControl = lexe  # Identificador de la variable de control
    if toke != 'Ide':
        erra(renC, colC, 'Error de Sintaxis', 'Se esperaba un Identificador y llegó: ' + lexe)
    toke, lexe = lexico()
    if lexe != '=':
        erra(renC, colC, 'Error de Sintaxis', 'Se esperaba "=" en la inicialización del ciclo "desde"')
    # Inicializar el valor de la variable de control
    toke, lexe = lexico()
    expr()  # Evaluar la expresión inicial
    insCodigo(['STO', varControl, '0'])  # Guardar el valor inicial
    # Validar el límite superior del ciclo
    if lexe != 'hasta':
        erra(renC, colC, 'Error de Sintaxis', 'Se esperaba "hasta" y llegó: ' + lexe)
    toke, lexe = lexico()
    expr()  # Evaluar la expresión límite
    tipo = pilaTipos.pop()
    # if tipo != 'E':
    #     erra(renC, colC, 'Error de Tipos', 'Se esperaba un valor entero para el límite superior, pero se obtuvo: ' + tipo)
    # Marcar el inicio del ciclo
    posInicio = conCod
    insCodigo(['NOP', '0', '0'])
    # Evaluar condición para continuar
    insCodigo(['LOD', varControl, '0'])  # Cargar valor de la variable de control
    insCodigo(['SUB', '0', lexe])  # Comparar con el límite superior
    posJMC = conCod
    insCodigo(['JMC', 'F', '_ETIQ1'])  # Salto si la condición es falsa
    
    if lexe == 'incr':
        toke, lexe = lexico()
        expr()
    else:
        toke, lexe = lexico()
    #toke, lexe = lexico()
    if lexe == 'inicio':
        block()
    
    # Incrementar el valor de la variable de control
    insCodigo(['LOD', varControl, '0'])
    insCodigo(['ADD', '1', '0'])  # Incrementar en 1
    insCodigo(['STO', varControl, '0'])

    # Salto al inicio
    insCodigo(['JMP', '0', str(posInicio)])

    # Etiqueta de salida
    codProg[posJMC][2] = str(conCod)
    insCodigo(['NOP', '_ETIQ1', '0'])
    toke, lexe = lexico()

def asigna(NomIde):
    global toke, lexe, renC, colC, bImp, conCod
    if lexe == '[':
        udim()
    if lexe != '=':
        erra(renC, colC, 'Error de Sintaxis', 'Se esperaba "=" en la asignación, pero llegó: ' + lexe)
    toke, lexe = lexico()
    expr()  # Evaluar la expresión
    insCodigo(['STO', '0', NomIde])  # Guardar el resultado
  
def cfunc():
    global toke, lexe, renC, colC, bImp, conCod
    toke, lexe = lexico()  # Consumir el (
    if lexe == ')':
        toke, lexe = lexico()
        return
    
    while True:
        expr()
        if lexe == ',':
            toke, lexe = lexico()
        elif lexe == ')':
            toke, lexe = lexico()
            return
        else:
            erra(renC, colC, 'Error de Sintaxis', 'se esperaba , o ) y llego ' + lexe)
            return

def udim():
    global toke, lexe, renC, colC, bImp, conCod
    toke, lexe = lexico()
    expr()
    if lexe != ']' :
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba ] y llego'  + lexe)
    toke, lexe = lexico()

def termino():
    global toke, lexe, renC, colC, bImp, conCod, tabSim
    if lexe == '(':
        toke, lexe = lexico()
        expr()
        if lexe != ')':
           erra(renC, colC, 'Error de Sintaxis', 'se esperaba ) y llego' + lexe)
        toke, lexe = lexico()
    elif toke == 'Ide': 
        nIde = lexe
        if nIde in tabSim:
            tipo_original = tabSim[nIde][1]  # Guardar tipo original
            buscaInsTipo(nIde)
        toke, lexe = lexico()
        if lexe == '(' :
            cfunc()
            if nIde in tabSim and tabSim[nIde][0] == 'F':
                # Restaurar el tipo de retorno de la función
                pilaTipos.append(tipo_original)
        elif lexe == '[': 
            udim()
        #validar udimen o llamada a llamada funcion
        insCodigo(['LOD', nIde, '0'])

    elif toke in ['Ent', 'Dec', 'CtA', 'CtL']:
        cte = lexe
        if toke in ['Ent', 'Dec']:
            pilaTipos.append(toke[0])
        elif toke in ['CtA', 'CtL']:
            pilaTipos.append(toke[2])
        if   lexe == 'verdadero': cte = 'V'
        elif lexe == 'falso'    : cte = 'F'
        insCodigo(['LIT', cte, '0'])
        toke, lexe = lexico()


def signo():
    global toke, lexe, renC, colC, bImp 
    if lexe == '-':
        pilaTipos.append('-')
        toke, lexe = lexico()
    termino()

def expo():
    global toke, lexe, renC, colC, bImp
    banY = True
    op = ''
    while banY:
        banY = False
        signo()
        if op == '^':
            tipD   = pilaTipos.pop()
            op     = pilaTipos.pop()
            tipI   = pilaTipos.pop()
            tipKey = tipI + op + tipD 
            tipoResul(tipKey)
            print('La pila es', pilaTipos)
            print('Las llaves xd', tipKey, tipoResul)
            op = ''
            insCodigo(['OPR','0', '7'])
        if lexe == '^': 
            op = lexe
            banY = True
            pilaTipos.append('^')  
            toke, lexe = lexico()

def multi():
    global toke, lexe, renC, colC, bImp
    paso = False
    operador = '*'
    while operador in ['*', '/', '%']:
        expo()
        if paso: 
            dim2 = '4'
            vd = pilaTipos.pop()
            op = pilaTipos.pop()
            vi = pilaTipos.pop()
            tipKey = vi + op + vd
            tipoResul(tipKey)
            print(tipKey)
            if op == '/':
                dim2 = '5'
            elif op == '%':
                dim2 = '6'
            insCodigo(['OPR', '0', dim2]) 
            paso = False
            print(paso)
        operador = lexe
        if operador in ['*', '/', '%']:
            pilaTipos.append(operador)
            paso = True
            toke, lexe = lexico()

def oprel():
    global toke, lexe, renC, colC, bImp
    operador = '<'
    paso = False
    while operador in ['<', '>', '<=', '>=', '<>', '==']:
        suma()
        if paso: 
            dim2 = '9'
            vd = pilaTipos.pop()
            op = pilaTipos.pop()
            vi = pilaTipos.pop()
            tipKey = vi + op + vd
            tipoResul(tipKey)
            print(tipKey)
            if op == '>':
                dim2 = '10'
            elif op == '<=':
                dim2 = '11'
            elif op == '>=':
                dim2 = '12'
            elif op == '<>':
                dim2 = '13'
            elif op == '==':
                dim2 = '14'   
            insCodigo(['OPR', '0', dim2]) 
            paso = False
            print(paso)
        operador = lexe
        if operador in ['<', '>', '<=', '>=', '<>', '==']:
            pilaTipos.append(operador)
            paso = True
            toke, lexe = lexico()

def suma():
    global toke, lexe, renC, colC, bImp
    operador = '+'
    paso = False
    while operador in ['+', '-']:
        multi()
        if paso: 
            dim2 = '2'
            vd = pilaTipos.pop()
            op = pilaTipos.pop()
            vi = pilaTipos.pop()
            tipKey = vi + op + vd
            tipoResul(tipKey)
            print(tipKey)
            print('SUMA TR', tipoResul)
            if op == '-':
                dim2 = '3'
            insCodigo(['OPR', '0', dim2]) 
            paso = False
            print(paso)
        operador = lexe
        if operador in ['+', '-']:
            pilaTipos.append(operador)
            paso = True
            toke, lexe = lexico()

#CHINGA TU MADRE MAQUINA PL0
def opy():
    global toke, lexe, renC, colC, bImp
    banY = True
    op = ''
    while banY:
        banY = False
        opno()
        if op == 'y':
            tipD   = pilaTipos.pop()
            op     = pilaTipos.pop()
            tipI   = pilaTipos.pop()
            tipKey = tipI + op + tipD 
            tipoResul(tipKey)
            print('La pila es', pilaTipos)
            print('Las llaves xd', tipKey, tipoResul)
            op = ''
            insCodigo(['OPR','0', '15'])
        if lexe == 'y': 
            op = lexe
            banY = True
            pilaTipos.append('y')  
            toke, lexe = lexico()

def opno():
    global toke, lexe, renC, colC, bImp 
    op = ''
    if lexe == 'no':
        op = 'no'
        pilaTipos.append('no')
        toke, lexe = lexico()
    oprel()
    if op == 'no':
        tipKey = ''
        tp = pilaTipos.pop()
        op = pilaTipos.pop()
        tipKey = op + tp
        tipoResul(tipKey)
        op = ''
        insCodigo(['OPR', '0', '17'])


def expr():
    global toke, lexe, renC, colC, bImp
    op = 'o'
    while op == 'o':
        opy()
        op = lexe    

def imprimir():
    global toke, lexe, renC, colC, bImp
    if lexe != '(':
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba ( y llego ' + lexe)  
    deli = ',' 
    while deli == ',':
        toke, lexe = lexico()
        expr()
        if lexe == ',':
            if len(pilaTipos) > 0:
                x = pilaTipos.pop()
            insCodigo(['OPR', '0', '20'])
            deli = ','
        else:
            deli = ''
    if lexe != ')':
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba ) y llego ' + lexe)
    else:
        if len(pilaTipos) > 0:
            x = pilaTipos.pop()
        if bImp:
            insCodigo(['OPR', '0', '21'])
        else:
            insCodigo(['OPR', '0', '20'])
    toke, lexe = lexico()

def lee():
    global toke, lexe, renC, colC, conCod
    toke, lexe = lexico()
    nIde = ''
    if lexe != '(':
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba ( ' + lexe)
    toke, lexe = lexico()
    if toke != "Ide":
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba Identificador ' + lexe)
    else: 
        nIde = lexe
    toke, lexe = lexico()
    if lexe == '[': udim()
    if lexe != ')':
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba ) ' + lexe)
    insCodigo(['OPR', nIde, '19'])
    toke, lexe = lexico()
     
def comando():
    global toke, lexe, renC, colC, bImp, conCod
    if lexe in ['imprime', 'imprimeln']:
        if lexe == 'imprimeln': bImp = True
        toke, lexe = lexico()
        imprimir()
    elif lexe == 'si': eSi()
    elif lexe == 'mientras': eMientras()
    elif lexe == 'repite': eRepite()
    elif lexe == 'desde':eDesde()
    elif lexe == 'interrumpe': eInterrumpe()
    elif lexe == 'continua': eContinua()
    elif lexe == 'regresa': eRegresa()
    elif lexe == 'lmp':
        insCodigo(['OPR', '0', '18'])
        toke, lexe = lexico()
    elif lexe == 'lee': lee()
    elif toke == 'Ide':
        SaIde=lexe
        toke, lexe = lexico()
        if lexe == '(': 
            cfunc()
        else: 
            asigna(SaIde)


def estatutos(): 
    global toke, lexe, renC, colC
    delim = ';'
    while (delim == ';'):
        if lexe == ';':
            toke, lexe = lexico()
        if lexe != ';':
            comando()
        delim = lexe


def tipo():
    global toke, lexe, renC, colC, tData
    if not (lexe in ['alfabetica','decimal','entera', 'logica']): 
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba tipo: alfabetica, decimal, entera o logica y llego '+lexe)
    tData = lexe.upper()
    tData = tData[0]
    toke, lexe = lexico()

def block():
    global lexe, toke, renC, colC
    # Verificar que se tenga el token 'inicio'
    if lexe != 'inicio':
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba inicio, llegó ' + lexe)
    # Consumir el token 'inicio'
    toke, lexe = lexico()
    print(f"[DEBUG] Dentro del bloque 'inicio': toke={toke}, lexe={lexe}")
    
    # Procesar comandos dentro del bloque hasta encontrar el token 'fin'
    if lexe != 'fin':
        estatutos()
        print(f"[DEBUG] Dentro del bloque, después de comando: toke={toke}, lexe={lexe}")
        # Si estatutos() ya consume todos los comandos, el ciclo continuará hasta que se llegue a 'fin'
    
    # Ahora lexe es 'fin'; lo consumimos y mostramos el mensaje final
    toke, lexe = lexico()
    print(f"[DEBUG] Después de 'fin': toke={toke}, lexe={lexe}")


#Hola soy un easter egg
#Consejo, leer el diagrama de derecha a izquierda, es mas facil

def params():
    global toke, lexe, renC, colC, tabSim, tData
    deli2 = ';'
    while deli2 == ';':
        # Se asume que ya se leyó el tipo y se guarda en tData
        tipo()  
        deli = ','
        while deli == ',':
            if toke != 'Ide':
                erra(renC, colC, 'Error de Sintaxis', 'Se esperaba un identificador y llegó ' + lexe)
            else:
                # Inserción del parámetro en la tabla de símbolos
                insTabSim(lexe, ['P', tData, None, '0'])
            toke, lexe = lexico()
            deli = lexe
            if lexe == ',':
                toke, lexe = lexico()
        if lexe == ';':
            toke, lexe = lexico()
        deli2 = lexe


def uparams():
    global toke, lexe, renC, colC, tabSim, tData
    deli = ','
    while deli == ',':
        toke, lexe = lexico()
        expr()
        if lexe == ',':
            deli = lexe       
    toke, lexe = lexico()


#Checar el tipo OJO ESTE PUEDE SER OPCIONAL
def funciones():
    global toke, lexe, conCod, tabSim, tData, renC, colC

    toke, lexe = lexico()  

    if toke == 'Ide' or lexe == 'principal':
        nomF = lexe  

        if lexe == 'principal':
            # Agrega principal como funcion interna y etiqueta _E2
            insTabSim('_P', ['E', 'I', str(conCod), '0'])
            insTabSim('principal', ['F', 'I', str(conCod), '0'])
            # Etiqueta para principal
            global IdEti
            IdEti += 1
            insTabSim('_E2', ['E', 'I', str(conCod), '0'])
        else:
            # Si no hay tipo explícito, poner tipo I (interna)
            insTabSim(nomF, ['F', 'I', str(conCod), '0'])

        toke, lexe = lexico()  
    else:
        tipo()  

        nomF = lexe  # Ahora lee el nombre de la función
        if toke != 'Ide':
            erra(renC, colC, 'Error de Sintaxis', 'se esperaba nombre de función y llegó ' + lexe)

        insTabSim(nomF, ['F', tData, str(conCod), '0'])
        toke, lexe = lexico()  

    # Procesar parámetros
    if lexe != '(':
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba ( y llegó ' + lexe)

    toke, lexe = lexico()  

    # Procesar lista de parámetros si hay
    if lexe != ')':
        params()  

    if lexe != ')':
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba ) y llegó ' + lexe)

    toke, lexe = lexico()  

    block()

    if nomF == 'principal':
        insCodigo(['OPR', '0', '0'])  
    else:
        insCodigo(['OPR', '0', '1'])  

def programa():
    global toke, lexe, renC, colC, codProg, conCod, tabSim
    toke, lexe = lexico()
    while lexe in ['constante','variable']: 
        varconst()
    if lexe != 'funcion':
        erra(renC, colC,'Error de Sintaxis', 
             'Un programa en CPAS debe tener al menos una FUNCION' + lexe)
    else:
        while lexe == 'funcion':
            funciones()
    # Al finalizar, si existe principal, agregar LOD _E2, 0 y CAL cuenta, 0 antes de OPR 0, 0
    if 'principal' in tabSim:
        # Buscar la posición antes de OPR 0, 0 (fin de principal)
        fin_principal = None
        for k in codProg:
            if codProg[k][0] == 'OPR' and codProg[k][2] == '0':
                fin_principal = k
                break
        if fin_principal:
            # Insertar instrucciones antes de OPR 0, 0
            codProg[fin_principal] = ['LOD', '_E2', '0']
            codProg[fin_principal+1] = ['CAL', 'cuenta', '0']
            codProg[fin_principal+2] = ['OPR', '0', '0']
            conCod = fin_principal+3

def prgm():
    global entrada, idx, errB, tok, lex, \
           archE, renC, colC, tabSim, codProg
    archE = ''
    print(archE[len(archE)-3:])
    while (archE[len(archE)-3:] != 'icc'):
        renC = 1
        colC = 0
        archE = input('Archivo a compilar (*.icc) [.]=Salir: ')
        if archE == '.': exit(0)
        aEnt = None
        try:
            aEnt = open(archE, 'r+')
            break
        except FileNotFoundError:
            print(archE, 'No exite volver a intentar')
    
    if aEnt != None:
        while (linea := aEnt.readline()):
            entrada += linea
        aEnt.close()

    print('\n\n' + entrada + '\n\n')  

    idx = 0
    errB = False
    programa()
    
    
if __name__ == '__main__':
    prgm()
    programa
    if not(errB):
        print(archE, "COMPILO con Exito!!")
        archS = archE[0:len(archE)-3] + 'eje'
        try:
        # print(tabSim.items())
            with open(archS, 'w') as aSal:
                for x, y in tabSim.items():
                    # Eliminar MAX y vec de la salida
                    if x in ['MAX', 'vec']:
                        continue
                    # Agregar principal y _E2 si existen
                    aSal.write(x + ',')
                    aSal.write(y[0] + ',')
                    aSal.write(y[1] + ',')
                    aSal.write(str(y[2]) + ',')
                    aSal.write(str(y[3]) + ',')
                    aSal.write('#,\n')
                aSal.write('@\n')
                for x , y in codProg.items():
                    # Eliminar NOP _E1, 0 de la salida
                    if y[0] == 'NOP':
                        continue
                    aSal.write(str(x) + ' ')                    
                    aSal.write(y[0] + ' ')                    
                    aSal.write(y[1] + ', ')                    
                    aSal.write(y[2] + '\n')                    
                aSal.close()
        except FileNotFoundError:
            print(archE, 'No existe, vuelve a intentar')