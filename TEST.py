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
matran=[
    #           tab +,-
    #           sp  *
    #_,let  dig nl  /   %   .   "   del =
    [1,     2,  0,  5,  6,  ERR,9,  11, 12 ], #0
    [1,     1,  ACP,ACP,ACP,ACP,ACP,ACP,ACP], #1
    [ACP,   2,  ACP,ACP,ACP,3  ,ACP,ACP,ACP], #2
    [ERR,   4,  ERR,ERR,ERR,ERR,ERR,ERR,ERR], #3
    [ACP,   4,  ACP,ACP,ACP,ACP,ACP,ACP,ACP], #4
    [ACP,   ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP], #5
    [ACP,   ACP,ACP,ACP,  7,ACP,ACP,ACP,ACP], #6
    [7,     7,  7,  7,  7,  7  ,7,  7,  7  ], #7
    [ACP,   ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP], #8
    [9,     9,  9,  9,  9,  9  ,10, 9,  9  ], #9
    [ACP,   ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP], #10
    [ACP,   ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP], #11
    [ACP,   ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP]  #12
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

pilaTipos=[]

def tipoResul(key):
    global renC, colC
    try:
        tip = mapTipos[key]
        if tip != '':
            pilaTipos.append(tip)
    except KeyError:
        erra(renC, colC, 'Error Semantico', 'Conflicto en tipos NO opera '+key)
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
    while idx < len(entrada) and estado != ERR \
        and estado != ACP:
        x = entrada[idx]
        if x == '\n'and estado in [0, 7, 9]:
            renC += 1
            colC = 0
        elif x == '\t' and estado == 0: 
            colC += 3
        else:
            colC += 1 
        idx += 1
        col = colCar( x )
        if col >=0 and col<=8:
            if estado == 7:
                lex = ''
                if x == '\n':
                    estado = 8
            else:
                estado=matran[estado][col]
            if estado not in [ERR, ACP]:
                estAnt = estado
                if estado == 9 or \
                    (estado not in [7, 9] and \
                    x not in [' ', '\t', '\n']):
                   lex += x

    #Clasificacion de Tokens, Lexemas
    if estado in [ACP, ERR]:
        idx -= 1
    else: estAnt = estado
    if estAnt == 3:
        tok = 'Dec'
        erra(renC, colC, "Error Lexico", "constante DECIMAL sin cerrar "+lex);
    elif estAnt == 9:
        tok = 'CtA'
        erra(renC, colC, "Error Lexico", "constante Alfabetica sin cerrar ");
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
        tok = 'Del'
    elif estAnt == 8:
        tok = 'Com'
    elif estAnt == 10:
        tok = 'CtA'
    elif estAnt == 11:
        tok = 'Del'
    elif estAnt == 12:
        tok = 'OpS'

    return tok, lex

def lexico():
    tok, lex = lexical()
    while tok == 'Com':
        tok, lex = lexical()
    
    return tok, lex

def dimen(): pass

def ctes(): pass

def const():
    global toke, lexe, renC, colC, bImp, conCod

def vars(): 
    global toke, lexe, renC, colC, bImp, conCod, tData
    toke, lexe = lexico()
    tipo()
    deli = ','
    dim1 = '0'
    while deli == ',':
        deli = ';'
        nIde = lexe
        if toke != 'Ide':
            erra(renC, colC, 'Error de Sintaxis', 'se esperaba Identificador y llego ' + lexe)
        toke, lexe = lexico()
        if lexe == '[': dimen()
        if lexe == '=': 
            toke, lexe = lexico()
            if lexe == '{':
                toke, lexe = lexico()
                ctes()
                toke, lexe = lexico()
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


def eSi(): pass

def asigna(): pass

def cfunc(): pass

def udim(): pass

def termino():
    global toke, lexe, renC, colC, bImp, conCod
    if lexe == '(':
        toke, lexe = lexico()
        expr()
        if lexe != ')':
           erra(renC, colC, 'Error de Sintaxis', 'se esperaba ) ' + lexe)
    elif toke == 'Ide': 
        nIde = lexe
        buscaInsTipo(nIde)
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
    op = ''
    if lexe == '-':
        op = '-'
        pilaTipos.append('-')
        toke, lexe = lexico()
    signo()
    if op == '-':
        tipKey = ''
        tp = pilaTipos.pop()
        op = pilaTipos.pop()
        tipKey = op + tp
        tipoResul(tipKey)
        insCodigo(['OPR', '0', '8'])


def multi():
    global toke, lexe, renC, colC, bImp
    expo()

def oprel():
    global toke, lexe, renC, colC, bImp
    suma()

def suma():
    global toke, lexe, renC, colC, bImp
    banS = True
    op = ''
    while banS:
        banS = False
        multi()
        if op in ['+', '-']:
            tipD   = pilaTipos.pop()
            op     = pilaTipos.pop()
            tipI   = pilaTipos.pop()
            tipKey = tipI + op + tipD 
            tipoResul(tipKey)
            if op == '+':
                insCodigo(['OPR','0', '2'])
            elif op == '-':
                insCodigo(['OPR','0', '3'])
            op = ''
        if lexe in ['+', '-']: 
            op = lexe
            banS = True
            pilaTipos.append(op)  
            toke, lexe = lexico()

def oprel():
    global toke, lexe, renC, colC, bImp
    suma()

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
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba ( ' + lexe)
    deli = ','
    while deli == ',':
        toke, lexe = lexico()
        expr()
        if lexe == ',':
            x = pilaTipos.pop()
            insCodigo(['OPR', '0', '20'])
        deli = lexe       
    if lexe != ')':
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba ) y llego ' + lexe)
    else:
        x = pilaTipos.pop()
        if bImp: insCodigo(['OPR', '0', '21'])
        else: insCodigo(['OPR', '0', '20'])
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
    elif lexe == 'lmp':
        insCodigo(['OPR', '0', '18'])
        toke, lexe = lexico()
    elif lexe == 'lee': lee()
    elif toke == 'Ide':
        toke, lexe = lexico()
        if lexe == '(': 
            cfunc()
        else: 
            asigna()


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
    if lexe != 'inicio':
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba inicio llego ' + lexe)
    toke, lexe = lexico()
    if lexe != 'fin':
        estatutos()
    if lexe != 'fin':
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba fin llego ' + lexe)
    toke, lexe = lexico()

def params(): pass

def funciones():
    global toke, lexe, conCod
    toke, lexe = lexico()
    nomF = lexe
    if toke != 'Ide' and lexe != 'principal':
        tipo()
    if toke == 'Ide' or lexe == 'principal':
        if lexe == 'principal':
            insTabSim('_P',['E', 'I', str(conCod), '0'])
        toke, lexe = lexico()
        if lexe != '(':
           erra(renC, colC, 'Error de Sintaxis', 'se esperaba ( llego ' + lexe)
        toke, lexe = lexico()
        if lexe != ')': params()                   
        if lexe != ')':
           erra(renC, colC, 'Error de Sintaxis', 'se esperaba ) llego ' + lexe)
        toke, lexe = lexico()
        block()
        if nomF == 'principal':
              insCodigo(['OPR', '0', '0'])
        else: insCodigo(['OPR', '0', '1'])

def programa():
    global toke, lexe, renC, colC
    toke, lexe = lexico()
    while lexe in ['constante','variable']: 
        varconst()
    if lexe != 'funcion':
        erra(renC, colC,'Error de Sintaxis', 
             'Un programa en CPAS debe tener al menos una FUNCION' + lexe)
    else:
        while lexe == 'funcion':
            funciones()
    
        
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
    
    if not(errB):
        print(archE, "COMPILO con Exito!!")
        archS = archE[0:len(archE)-3] + 'eje'
        try:
        # print(tabSim.items())
            with open(archS, 'w') as aSal:
                for x, y in tabSim.items():
                    aSal.write(x + ',')
                    aSal.write(y[0] + ',')
                    aSal.write(y[1] + ',')
                    aSal.write(str(y[2]) + ',')
                    aSal.write(str(y[3]) + ',')
                    aSal.write('#,\n')
                aSal.write('@\n')
                for x , y in codProg.items():
                    aSal.write(str(x) + ' ')                    
                    aSal.write(y[0] + ' ')                    
                    aSal.write(y[1] + ', ')                    
                    aSal.write(y[2] + '\n')                    
                aSal.close()
        except FileNotFoundError:
            print(archE, 'No existe, vuelve a intentar')