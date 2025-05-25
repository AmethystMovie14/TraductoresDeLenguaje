ACP=99
ERR=-1
idx=0
NFuncion = '' #Guardar el nombre de la funcion actual
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
    
    toke, lexe = lexico()  # ✅ CONSUMIR "inicio"
    
    if lexe != 'fin':
        estatutos()
        
    if lexe != 'fin':
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba fin llego ' + lexe)
        
    toke, lexe = lexico()  # Consumir "fin"

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
                erra(renC, colC, 'Error de Semántico', 'Se esperaba una constante para la dimensión: ' + nIde)
        else:
            erra(renC, colC, 'Error de Semántico', 'Identificador no declarado: ' + nIde)
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
    global toke, lexe, renC, colC, bImp, conCod, NFuncion
    
    print("DEBUG: eRegresa() llamado")  # ← AGREGAR ESTA LÍNEA
    toke, lexe = lexico()
    expr()  # Evaluar la expresión de retorno (deja valor en pila)
    insCodigo(['STO', '0', NFuncion])  # Guardar el valor de retorno en la posición 0
    insCodigo(['OPR', '0', '1'])  # Instrucción de retorno
    print(f"DEBUG: Generé OPR 0,1 en posición {conCod-1}")  # ← Y ESTA
    
def eContinua():
    global toke, lexe, renC, colC, bImp, conCod

    toke, lexe = lexico()

def eSi():
    global toke, lexe, renC, colC, bImp, conCod
    
    toke, lexe = lexico()
    expr()  # Evalúa la condición, deja resultado en pila
    
    # Verificar tipos en la pila
    if len(pilaTipos) > 0:
        tipo = pilaTipos.pop()
        if tipo != 'L':
            erra(renC, colC, 'Error de Tipos', 'Se esperaba expresión lógica en if')
    
    # Exigir "hacer"
    if lexe != 'hacer':
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba hacer y llego ' + lexe)
    
    toke, lexe = lexico()  # Consumir "hacer"
    
    # Crear etiquetas únicas
    etiSino = nomEti()  # Genera algo como "_E1"
    etiFin = nomEti()   # Genera algo como "_E2"
    
    # Guardar posición para salto condicional
    insCodigo(['JMC', 'F', etiSino])  # Salta al sino si falso
    
    # Bloque del "si"
    if lexe == 'inicio':
        bloque()
    else:
        comando()
        
    # Salto incondicional al final
    insCodigo(['JMP', '0', etiFin])
    
    # Registrar la etiqueta del sino en la tabla de símbolos
    insTabSim(etiSino, ['E', 'I', str(conCod), '0'])
    
    # Verificar si hay "sino"
    if lexe == 'sino':
        toke, lexe = lexico()
        
        if lexe == 'inicio':
            block()
        else:
            comando()
    
    # Registrar la etiqueta del fin en la tabla de símbolos
    insTabSim(etiFin, ['E', 'I', str(conCod), '0'])

def eMientras():
    global toke, lexe, renC, colC, conCod, codProg, pilaTipos
    
    toke, lexe = lexico()
    
    # Crear etiqueta para el inicio
    etiInicio = nomEti()  # Por ejemplo "_E1"
    posInicio = conCod
    
    # Registrar la etiqueta del inicio
    insTabSim(etiInicio, ['E', 'I', str(conCod), '0'])
    
    expr()  # Evaluar la expresión lógica
    
    if len(pilaTipos) > 0:
        tipo = pilaTipos.pop()
        if tipo != 'L':
            erra(renC, colC, 'Error de Tipos', 'Se esperaba una expresión lógica')
    
    #if lexe != 'hacer':
    #   erra(renC, colC, 'Error de Sintaxis', 'Se esperaba "hacer"')
    
    toke, lexe = lexico()
    
    # Crear etiqueta para el final
    etiFin = nomEti()  # Por ejemplo "_E2"
    
    # Salto condicional al final
    insCodigo(['JMC', 'F', etiFin])
    
    # Procesar el bloque
    if lexe == 'inicio':
        bloque()
    else:
        comando()
    
    # Salto al inicio usando la etiqueta
    insCodigo(['JMP', '0', etiInicio])
    
    # Registrar etiqueta del final
    insTabSim(etiFin, ['E', 'I', str(conCod), '0'])

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
    global toke, lexe, renC, colC, conCod, codProg, pilaTipos
    
    toke, lexe = lexico()  # Leer variable de control
    varControl = lexe
    
    if toke != 'Ide':
        erra(renC, colC, 'Error de Sintaxis', 'Se esperaba un Identificador y llegó: ' + lexe)
    
    toke, lexe = lexico()
    if lexe != '=':
        erra(renC, colC, 'Error de Sintaxis', 'Se esperaba "=" en la inicialización del ciclo "desde"')
    
    # Inicializar la variable de control
    toke, lexe = lexico()
    expr()  # Evaluar la expresión inicial
    insCodigo(['STO', '0', varControl])  # variable = valor_inicial
    
    # Validar "hasta"
    if lexe != 'hasta':
        erra(renC, colC, 'Error de Sintaxis', 'Se esperaba "hasta" y llegó: ' + lexe)
    
    toke, lexe = lexico()
    
    # Guardar el límite Y su tipo
    limite = lexe
    tipoLimite = toke  # ← GUARDAR EL TIPO AQUÍ
    
    if toke == 'Ent':
        pass
    elif toke == 'Ide':
        pass
    else:
        erra(renC, colC, 'Error de Sintaxis', 'Se esperaba un número o variable para el límite')
    
    toke, lexe = lexico()
    
    # Saltar "incr 1" si existe
    if lexe == 'incr':
        toke, lexe = lexico()  # saltar "incr"
        toke, lexe = lexico()  # saltar el número de incremento
    
    # Crear etiquetas
    etiInicio = nomEti()
    etiFin = nomEti()
    
    # Registrar inicio del ciclo
    insTabSim(etiInicio, ['E', 'I', str(conCod), '0'])
    
    # INICIO DEL CICLO: Evaluar condición variable <= limite
    insCodigo(['LOD', varControl, '0'])    # Cargar variable de control
    
    if tipoLimite == 'Ent':  # ← USAR EL TIPO GUARDADO
        insCodigo(['LIT', limite, '0'])    # Cargar límite literal
    else:
        insCodigo(['LOD', limite, '0'])    # Cargar límite desde variable
    
    insCodigo(['OPR', '0', '10'])          # Operación >
    insCodigo(['JMC', 'V', etiFin])        # Si variable > limite, salir del ciclo
    
    # Procesar bloque del ciclo
    if lexe == 'inicio':
        bloque()
    else:
        comando()
    
    # Incrementar variable: variable = variable + 1
    insCodigo(['LOD', varControl, '0'])
    insCodigo(['LIT', '1', '0'])
    insCodigo(['OPR', '0', '2'])           # Sumar
    insCodigo(['STO', '0', varControl])    # Guardar resultado
    
    # Saltar al inicio del ciclo
    insCodigo(['JMP', '0', etiInicio])
    
    # Registrar final del ciclo
    insTabSim(etiFin, ['E', 'I', str(conCod), '0'])

def asigna(NomIde):
    global toke, lexe, renC, colC, bImp, conCod
    if lexe == '[':
        udim()
    if lexe != '=':
        erra(renC, colC, 'Error de Sintaxis', 'Se esperaba "=" en la asignación, pero llegó: ' + lexe)
    toke, lexe = lexico()
    expr()  # Evaluar la expresión
    insCodigo(['STO', '0', NomIde])  # Guardar el resultado
  
def cfunc(nombreFunc):
    global toke, lexe, renC, colC, bImp, conCod, tabSim
    toke, lexe = lexico()  # Consumir el (
    
    parametros = []
    
    if lexe == ')':
        toke, lexe = lexico()
    else:
        # Obtener lista de parámetros de esta función específica
        params_funcion = []
        for nombre, info in tabSim.items():
            if info[0] == 'P' and info[2] == nombreFunc:  # Parámetro de esta función
                params_funcion.append(nombre)
        
        param_index = 0
        while True:
            expr()  # Evalúa parámetro (valor queda en pila)
            
            if param_index < len(params_funcion):
                parametros.append(params_funcion[param_index])
                param_index += 1
            
            if lexe == ',':
                toke, lexe = lexico()
            elif lexe == ')':
                toke, lexe = lexico()
                break
            else:
                erra(renC, colC, 'Error de Sintaxis', 'se esperaba , o )')
                return
    
    # Asignar parámetros (en orden inverso porque están en la pila)
    for i in range(len(parametros)-1, -1, -1):
        insCodigo(['STO', '0', parametros[i]])
    
    # NUEVO: Poner dirección de retorno en la pila
    insCodigo(['LIT', str(conCod + 2), '0'])  # Dirección después del CAL
    
    # Llamada a la función
    insCodigo(['CAL', nombreFunc, '0'])
    


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
            tipo_original = tabSim[nIde][1]  
            buscaInsTipo(nIde)
        toke, lexe = lexico()
        if lexe == '(' :
            cfunc(nIde)  # Genera CAL
            if nIde in tabSim and tabSim[nIde][0] == 'F':
                pilaTipos.append(tipo_original)
        elif lexe == '[': 
            udim()
        # Solo generar LOD si NO es una función con parámetros
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
            cfunc(SaIde)  # ← CAMBIO AQUÍ: pasar SaIde
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
    global toke, lexe, renC, colC, tabSim, tData, NFuncion
    deli2 = ';'
    while deli2 == ';':
        tipo()  
        deli = ','
        while deli == ',':
            if toke != 'Ide':
                erra(renC, colC, 'Error de Sintaxis', 'Se esperaba un identificador y llegó ' + lexe)
            else:
                # Inserción del parámetro con referencia a la función
                insTabSim(lexe, ['P', tData, NFuncion, '0'])  # ← CAMBIO: usar NFuncion en lugar de None
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
    global toke, lexe, conCod, tabSim, tData, renC, colC, NFuncion

    toke, lexe = lexico()  

    if toke == 'Ide' or lexe == 'principal':
        nomF = lexe  
        NFuncion = nomF
        print(f"[DEBUG] Función: {NFuncion}")  # ← AGREGAR ESTA LÍNEA

        if lexe == 'principal':
            insTabSim('_P', ['E', 'I', str(conCod), '0'])
            insTabSim('principal', ['F', 'I', str(conCod), '0'])
        else:
            insTabSim(nomF, ['F', 'I', str(conCod), '0'])

        toke, lexe = lexico()  
    else:
        tipo()  
        nomF = lexe
        NFuncion = nomF
        if toke != 'Ide':
            erra(renC, colC, 'Error de Sintaxis', 'se esperaba nombre de función y llegó ' + lexe)

        insTabSim(nomF, ['F', tData, str(conCod), '0'])
        toke, lexe = lexico()  

    # Procesar parámetros
    if lexe != '(':
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba ( y llegó ' + lexe)

    toke, lexe = lexico()  

    if lexe != ')':
        params()  

    if lexe != ')':
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba ) y llegó ' + lexe)

    toke, lexe = lexico()  

    block()
    insCodigo(['OPR', '0', '1'])  # Retorno de función

    # SIMPLIFICAR - sin saltos complejos
    if nomF == 'principal':
        print("DEBUG: Generando OPR 0,0 para principal")  # ← AGREGAR
        insCodigo(['OPR', '0', '0'])  # Terminar programa
    else:
        print(f"DEBUG: NO generando OPR automático para función {nomF}")  # ← AGREGAR
        #insCodigo(['OPR', '0', '1'])  # Retorno de función

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
    
    # Arreglar _P para que apunte al inicio real de principal
    if 'principal' in tabSim:
        pos_principal = tabSim['principal'][2]
        tabSim['_P'][2] = pos_principal
        print(f"DEBUG: Actualizando _P para apuntar a línea {pos_principal}")
    # Solo para programas con principal y llamada a otra función desde principal
    """if 'principal' in tabSim:
        principal_pos = int(tabSim['principal'][2])
        fin_principal = None
        # Buscar el final de principal (OPR 0, 0)
        for k in range(principal_pos, conCod):
            if codProg.get(k, [None, None, None])[0] == 'OPR' and codProg[k][2] == '0':
                fin_principal = k
                break
        # Buscar si hay una llamada a otra función (CAL ...) dentro de principal
        hay_cal = False
        cal_func = None
        for k in range(principal_pos, fin_principal):
            if codProg.get(k, [None, None, None])[0] == 'CAL':
                hay_cal = True
                cal_func = codProg[k][1]
                break
        if hay_cal:
            # Agregar _E2 a la tabla de símbolos si no existe
            if '_E2' not in tabSim:
                tabSim['_E2'] = ['E', 'I', str(fin_principal+2), '0']
            # Mueve las instrucciones después del fin_principal para hacer espacio
            for move_k in range(conCod-1, fin_principal-1, -1):
                codProg[move_k+3] = codProg[move_k]
            codProg[fin_principal] = ['LOD', '_E2', '0']
            codProg[fin_principal+1] = ['CAL', cal_func, '0']
            codProg[fin_principal+2] = ['OPR', '0', '0']
            conCod += 3"""

def prgm():
    global entrada, idx, errB, tok, lex, \
           archE, renC, colC, tabSim, codProg
    archE = ''
    print("[DEBUG] Iniciando prgm()")
    print(archE[len(archE)-3:])
    while (archE[len(archE)-3:] != 'icc'):
        renC = 1
        colC = 0
        archE = input('Archivo a compilar (*.icc) [.]=Salir: ')
        print(f"[DEBUG] Usuario ingresó archivo: {archE}")
        if archE == '.': 
            print("[DEBUG] Salida solicitada por el usuario.")
            exit(0)
        aEnt = None
        try:
            print(f"[DEBUG] Intentando abrir archivo: {archE}")
            aEnt = open(archE, 'r+')
            print(f"[DEBUG] Archivo {archE} abierto correctamente.")
            break
        except FileNotFoundError:
            print(f"[DEBUG] Archivo {archE} no existe, volver a intentar.")
            print(archE, 'No exite volver a intentar')
    
    if aEnt != None:
        print(f"[DEBUG] Leyendo líneas del archivo {archE}")
        while (linea := aEnt.readline()):
            print(f"[DEBUG] Línea leída: {linea.strip()}")
            entrada += linea
        aEnt.close()
        print(f"[DEBUG] Archivo {archE} cerrado tras lectura.")

    print('\n\n' + entrada + '\n\n')  
    print("[DEBUG] Contenido completo del archivo cargado en 'entrada'.")

    idx = 0
    errB = False
    print("[DEBUG] Llamando a programa() para iniciar análisis.")
    programa()
    print("[DEBUG] Finalizó programa().")
    
    
if __name__ == '__main__':
    print("[DEBUG] Entrando al main.")
    prgm()
    print("[DEBUG] Retornando de prgm().")
    programa
    if not(errB):
        print(archE, "COMPILO con Exito!!")
        archS = archE[0:len(archE)-3] + 'eje'
        try:
            print(f"[DEBUG] Intentando abrir archivo de salida: {archS}")
            with open(archS, 'w') as aSal:
                print("[DEBUG] Escribiendo tabla de símbolos en archivo de salida.")
                for x, y in tabSim.items():
                    # Eliminar MAX y vec de la salida
                    if x in ['MAX', 'vec']:
                        print(f"[DEBUG] Saltando símbolo especial: {x}")
                        continue
                    # Agregar principal y _E2 si existen
                    print(f"[DEBUG] Escribiendo símbolo: {x}, datos: {y}")
                    aSal.write(x + ',')
                    aSal.write(y[0] + ',')
                    aSal.write(y[1] + ',')
                    aSal.write(str(y[2]) + ',')
                    aSal.write(str(y[3]) + ',')
                    aSal.write('#,\n')
                aSal.write('@\n')
                print("[DEBUG] Escribiendo código intermedio en archivo de salida.")
                for x , y in codProg.items():
                    # Eliminar NOP _E1, 0 de la salida
                    if y[0] == 'NOP':
                        print(f"[DEBUG] Saltando instrucción NOP en línea {x}")
                        continue
                    print(f"[DEBUG] Escribiendo instrucción: {x} {y}")
                    aSal.write(str(x) + ' ')                    
                    aSal.write(y[0] + ' ')                    
                    aSal.write(y[1] + ', ')                    
                    aSal.write(y[2] + '\n')                    
                aSal.close()
                print(f"[DEBUG] Archivo de salida {archS} escrito y cerrado correctamente.")
                print(archE, "COMPILO con Exito!!")
        except FileNotFoundError:
            print(f"[DEBUG] Error: archivo de salida {archS} no existe, vuelve a intentar")
            print(archE, 'No existe, vuelve a intentar')
