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
    'E*E': 'E', 'E*D': 'D', 'D*E':'D', 'D*D': 'D',     # ← AGREGAR ESTAS
    'E/E': 'D', 'E/D': 'D', 'D/E':'D', 'D/D': 'D',
    'E%E': 'E',     
    'E^E': 'D', 'E^D': 'D', 'D^E':'D', 'D^D': 'D',
     '-E': 'E', '-D': 'D',     
    'E<E': 'L', 'E<D': 'L', 'D<E':'L', 'D<D': 'L', 'A<A': 'L',
    'E<=E': 'L', 'E<=D':'L', 'D<=E': 'L', 'D<=D': 'L', 'A<=A':'L',
    'E>E' : 'L', 'E>D' :'L', 'D>E' : 'L', 'D>D' : 'L', 'A>A' :'L',
    'E>=E': 'L', 'E>=D':'L', 'D>=E': 'L', 'D>=D': 'L', 'A>=A':'L',
    'E<>E': 'L', 'E<>D':'L', 'D<>E': 'L', 'D<>D': 'L', 'A<>A':'L', 'L<>L':'L',
    'E==E': 'L', 'E==D':'L', 'D==E': 'L', 'D==D': 'L', 'A==A':'L', 'L==L':'L',
    'noL' : 'L', 'LyL' :'L', 'LoL' : 'L'
    }
#A es alfabefica, E es entera, D es decimal, L es logica, 

pilaTipos=[]

def tipoResul(key):
    global renC, colC, pilaTipos
    print(f"[DEBUG_TIPOS] Entrada: key='{key}', pilaTipos={pilaTipos}")  # ← AGREGAR
    try:
        tip = mapTipos[key]
        if tip != '':
            pilaTipos.append(tip)
        print(f"[DEBUG_TIPOS] Salida: tip='{tip}', pilaTipos={pilaTipos}")  # ← AGREGAR
    except KeyError:
        erra(renC, colC, 'Error Semantico', 'Conflicto en tipos NO opera '+key)
        if '=' not in key:
            pilaTipos.append('I')
        print(f"[DEBUG_TIPOS] ERROR: key='{key}' no encontrada, pilaTipos={pilaTipos}")  # ← AGREGAR

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
    global toke, lexe, renC, colC, bImp, conCod, NFuncion, pilaTipos
    
    print("DEBUG: eRegresa() llamado")
    
    # LIMPIAR la pila antes de evaluar la expresión de retorno
    pilaTipos.clear()  # ← AGREGAR ESTA LÍNEA
    
    toke, lexe = lexico()
    expr()  # Evaluar la expresión de retorno
    
    insCodigo(['STO', '0', NFuncion])
    insCodigo(['OPR', '0', '1'])
    print(f"DEBUG: Generé OPR 0,1 en posición {conCod-1}")
    
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
        # Quitar esta línea: toke, lexe = lexico()
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
    global toke, lexe, renC, colC, bImp, conCod, pilaTipos
    
    # LIMPIAR la pila al inicio de cada asignación
    pilaTipos.clear()  # ← AGREGAR ESTA LÍNEA
    
    if lexe == '[':
        udim()
        arreglo()  # ← LLAMADA AGREGADA AQUÍ
    if lexe != '=':
        erra(renC, colC, 'Error de Sintaxis', 'Se esperaba "=" en la asignación, pero llegó: ' + lexe)
    toke, lexe = lexico()
    expr()  # Evaluar la expresión
    insCodigo(['STO', '0', NomIde])  # Guardar el resultado

  
def cfunc(nombreFunc):
    global toke, lexe, renC, colC, bImp, conCod, tabSim, pilaTipos
    print(f"[DEBUG_CFUNC] Llamando función '{nombreFunc}', pilaTipos antes={pilaTipos}")
    
    # GUARDAR el estado de la pila antes de procesar parámetros
    pila_backup = pilaTipos.copy()
    
    toke, lexe = lexico()  # Consumir el (
    
    if lexe == ')':
        toke, lexe = lexico()
    else:
        # Procesar parámetros (esto puede contaminar la pila)
        params_funcion = []
        for nombre, info in tabSim.items():
            if info[0] == 'P' and len(info) > 2 and info[2] == nombreFunc:
                params_funcion.append(nombre)
        
        param_index = 0
        while True:
            expr()  # Evalúa parámetro
            
            if param_index < len(params_funcion):
                insCodigo(['STO', '0', params_funcion[param_index]])
                param_index += 1
            
            if lexe == ',':
                toke, lexe = lexico()
            elif lexe == ')':
                toke, lexe = lexico()
                break
            else:
                erra(renC, colC, 'Error de Sintaxis', 'se esperaba , o )')
                return
    
    # RESTAURAR la pila original
    pilaTipos = pila_backup
    
    direccion_retorno = conCod + 2
    insCodigo(['LIT', str(direccion_retorno), '0'])
    insCodigo(['CAL', nombreFunc, '0'])
    
    # Agregar solo el tipo de retorno
    if nombreFunc in tabSim:
        tipo_retorno = tabSim[nombreFunc][1]
        pilaTipos.append(tipo_retorno)
        print(f"[DEBUG_CFUNC] Función '{nombreFunc}' retorna tipo '{tipo_retorno}', pilaTipos después={pilaTipos}")
    


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
            # CORRECCIÓN: Quitar el tipo que agregó buscaInsTipo() 
            # porque cfunc() agregará el tipo de retorno correcto
            if len(pilaTipos) > 0:
                pilaTipos.pop()  # ← LÍNEA AGREGADA
            cfunc(nIde)  # Genera CAL y agrega tipo de retorno
            # NO agregar tipo_original aquí porque cfunc() ya lo hizo
        elif lexe == '[': 
            udim()
            arreglo()  # ← LLAMADA AGREGADA AQUÍ
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

def arreglo():
    """
    Maneja la generación de código para acceso a arreglos.
    Se llama después de encontrar un '[' en:
    - asigna() - para guardar en arreglo
    - termino() - para cargar valor de arreglo
    - lee() - para leer en arreglo
    """
    global toke, lexe, conCod, tabSim, pilaTipos

    # Ya se procesó el '[' y la expresión del índice está en la pila
    # Verificar que la expresión del índice sea entera
    if len(pilaTipos) > 0:
        tipo_indice = pilaTipos.pop()
        if tipo_indice != 'E':
            erra(renC, colC, 'Error de Tipos', 'El índice debe ser entera')
    
    # Generar código para calcular la dirección del elemento
    #insCodigo(['OPR', '0', '30'])  # Operación especial para calcular desplazamiento
    
    # El resultado en la pila ahora es la dirección del elemento
    # Las instrucciones LOD y STO usarán esta dirección
    # No necesitamos hacer más aquí porque:
    # - asigna() generará el STO con la dirección calculada
    # - termino() generará el LOD con la dirección calculada
    # - lee() generará el OPR para leer con la dirección calculada
def multi():
    global toke, lexe, renC, colC, bImp, pilaTipos
    paso = False
    operador = '*'
    while operador in ['*', '/', '%']:
        print(f"[DEBUG_MULTI] Antes de expo(), pilaTipos={pilaTipos}")  # ← AGREGAR
        expo()
        print(f"[DEBUG_MULTI] Después de expo(), pilaTipos={pilaTipos}")  # ← AGREGAR
        if paso: 
            dim2 = '4'
            vd = pilaTipos.pop()
            op = pilaTipos.pop()
            vi = pilaTipos.pop()
            tipKey = vi + op + vd
            print(f"[DEBUG_MULTI] Operación: {vi} {op} {vd} = {tipKey}")  # ← AGREGAR
            tipoResul(tipKey)
            print(f"[DEBUG_MULTI] Después de tipoResul(), pilaTipos={pilaTipos}")  # ← AGREGAR
            if op == '/':
                dim2 = '5'
            elif op == '%':
                dim2 = '6'
            insCodigo(['OPR', '0', dim2]) 
            paso = False
        operador = lexe
        if operador in ['*', '/', '%']:
            print(f"[DEBUG_MULTI] Agregando operador '{operador}' a pila")  # ← AGREGAR
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
    opy()
    while lexe == 'o':
        pilaTipos.append('o')
        toke, lexe = lexico()  # ← AVANZA EL TOKEN
        opy()
        # Aquí debes hacer el pop y push de tipos, y generar el código OPR correspondiente si lo necesitas
        tipD = pilaTipos.pop()
        op = pilaTipos.pop()
        tipI = pilaTipos.pop()
        tipKey = tipI + op + tipD
        tipoResul(tipKey)
        insCodigo(['OPR', '0', '16'])# OPR para 'o'  

def imprimir():
    global toke, lexe, renC, colC, bImp

    pilaTipos.clear()  # Limpiar la pila de tipos antes de imprimir

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
    if lexe == '[': 
        udim()
        arreglo()  # ← LLAMADA AGREGADA AQUÍ
    if lexe != ')':
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba ) ' + lexe)
    insCodigo(['OPR', nIde, '19'])
    toke, lexe = lexico()
     
def comando():
    global toke, lexe, renC, colC, bImp, conCod, pilaTipos
    
    # LIMPIAR la pila al inicio de cada comando
    pilaTipos.clear()  # ← AGREGAR ESTA LÍNEA
    
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
            cfunc(SaIde)
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
    
    while lexe != ')':  # Mientras no llegue al final
        tipo()  # Lee el tipo
        
        if toke != 'Ide':
            erra(renC, colC, 'Error de Sintaxis', 'Se esperaba un identificador y llegó ' + lexe)
            return
        
        # Insertar parámetro
        insTabSim(lexe, ['P', tData, NFuncion, '0'])
        toke, lexe = lexico()
        
        # Si hay ';' o ',', consumirlo y continuar
        if lexe in [';', ',']:
            toke, lexe = lexico()
        elif lexe == ')':
            break  # Terminó la lista de parámetros
        else:
            erra(renC, colC, 'Error de Sintaxis', 'Se esperaba ; o , o ) y llegó ' + lexe)
            return


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

    # Verificar si es la función principal (caso especial)
    if lexe == 'principal':
        nomF = lexe  
        NFuncion = nomF
        print(f"[DEBUG] Función principal: {NFuncion}")
        
        insTabSim('_P', ['E', 'I', str(conCod), '0'])
        insTabSim('principal', ['F', 'I', str(conCod), '0'])
        
        toke, lexe = lexico()  
        
    # Si no es principal, debe ser una función con tipo de retorno
    else:
        # Primero viene el tipo de retorno
        if lexe in ['alfabetica', 'decimal', 'entera', 'logica']:
            tipo()  # Esto actualiza tData con el tipo
            
            # Ahora debe venir el nombre de la función
            if toke != 'Ide':
                erra(renC, colC, 'Error de Sintaxis', 'se esperaba nombre de función y llegó ' + lexe)
            
            nomF = lexe
            NFuncion = nomF
            print(f"[DEBUG] Función con tipo {tData}: {NFuncion}")
            
            # Insertar la función en la tabla de símbolos con su tipo
            insTabSim(nomF, ['F', tData, str(conCod), '0'])
            toke, lexe = lexico()  
            
        else:
            erra(renC, colC, 'Error de Sintaxis', 'se esperaba tipo de retorno o principal y llegó ' + lexe)
            return

    # Procesar parámetros
    if lexe != '(':
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba ( y llegó ' + lexe)

    toke, lexe = lexico()  

    if lexe != ')':
        params()  

    if lexe != ')':
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba ) y llegó ' + lexe)

    toke, lexe = lexico()  

    # Procesar el bloque de la función
    block()
    
    # Generar código de retorno según el tipo de función
    if nomF == 'principal':
        print("DEBUG: Generando OPR 0,0 para principal")
        insCodigo(['OPR', '0', '0'])  # Terminar programa
    else:
        print(f"DEBUG: Generando OPR 0,1 para función {nomF}")
        insCodigo(['OPR', '0', '1'])  # Retorno de función

def programa():
    global toke, lexe, renC, colC, codProg, conCod, tabSim
    toke, lexe = lexico()
    print(f"[DEBUG] programa() inicio: lexe={lexe}")
    
    while lexe in ['constante','variable']: 
        varconst()
    
    if lexe != 'funcion':
        erra(renC, colC,'Error de Sintaxis', 
             'Un programa en CPAS debe tener al menos una FUNCION y llego ' + lexe)
    else:
        while lexe == 'funcion':
            print(f"[DEBUG] Procesando función, lexe={lexe}")
            funciones()
            print(f"[DEBUG] Después de funciones(), lexe={lexe}")
            
            # Consumir el punto y coma opcional entre funciones
            if lexe == ';':
                print(f"[DEBUG] Consumiendo ';' entre funciones")
                toke, lexe = lexico()
                print(f"[DEBUG] Después de consumir ';': lexe={lexe}")
    
    print(f"[DEBUG] programa() termina con lexe={lexe}")
    
    # Arreglar _P para que apunte al inicio real de principal
    if 'principal' in tabSim:
        pos_principal = tabSim['principal'][2]
        tabSim['_P'][2] = pos_principal
        print(f"DEBUG: Actualizando _P para apuntar a línea {pos_principal}")

def prgm():
    global entrada, idx, errB, tok, lex, \
           archE, renC, colC, tabSim, codProg
    archE = ''
    print("[DEBUG] Iniciando prgm()")
    
    while (archE[len(archE)-3:] != 'icc'):
        renC = 1
        colC = 0
        archE = input('Archivo a compilar (*.icc) [.]=Salir: ')
        if archE == '.': 
            exit(0)
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

    print('\n=== CONTENIDO COMPLETO DEL ARCHIVO ===')
    print(repr(entrada))  # ← Usar repr() para ver caracteres especiales
    print('=== FIN DEL ARCHIVO ===\n')
    
    # También mostrar línea por línea
    lineas = entrada.split('\n')
    for i, linea in enumerate(lineas, 1):
        print(f"Línea {i}: {repr(linea)}")
    print()

    idx = 0
    errB = False
    programa()
    
    
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
                    #if x in ['MAX', 'vec']:
                    #    print(f"[DEBUG] Saltando símbolo especial: {x}")
                    #    continue
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
