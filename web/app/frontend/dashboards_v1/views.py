from app import app
from flask import g, request, render_template, session, flash, redirect, \
    url_for, jsonify, request, abort, Response, session
 
from flask_login import login_required, login_user, logout_user, current_user 
import json
from app import query_db, execute_db
from app.frontend.dashboards_v1.manager import Manager
from app.frontend.dashboards_v1.users import User
from app import login
#from app import appbuilder 

@app.route('/dashboards_v2/index', methods=['GET'])
def dashboards_v2():
    m = {}
    
    return render_template('dashboards_v2/base.html',m=m)

@app.route('/dashboards', methods=['GET'])
@app.route('/dashboards/', methods=['GET'])
@login_required
def index_dashboard(): 
     
    #l = current_user.id.split(':')
    #empresa = l[2]
    #filial  = l[3]
    try:
        empresa = session.get('codigo_empresa_dashboard')
    except:
        empresa = ''

    try:
        filial = session.get('codigo_filial_dashboard')
    except:
        filial = ''
    
    if empresa == '':
        empresa = None

    if filial == '':
        filial = None
    
    
    session['data_ref'] = None
    #appbuilder = appbuilder
    #print(str(session))
    #print(str(current_user))
    #print(ab)
    m = Manager(current_user, empresa,filial)  
    
    if m.menu is None:
        m.menu = []
    data = {'analises':None}
    return render_template('dashboards_v1/dashboard.html',data=data,m=m,id_dashboard=0)

#login_user, logout_user
@app.route('/dashboards/<int:id_dash>', methods=['GET','POST'])
@login_required
def principal(id_dash):
    
    
    if request.method == 'GET':        

        #Recebe os dados de login, empresa e filial
        #empresa = current_user.id.split(':')[2]
        #filial = current_user.id.split(':')[3]
        try:
            empresa = session.get('codigo_empresa_dashboard')
        except:
            empresa = ''

        try:
            filial = session.get('codigo_filial_dashboard')
        except:
            filial = ''

        if empresa == '':
            empresa = None
        
        if filial == '':
            filial = None

        #Instancia objeto de Manager para controle
        m = Manager(current_user, empresa,filial)        
        
        #Recebe parametros das analises do dashboard         
        menu = session['menu']
        proximo = menu.pop(0)
        menu.append(proximo)
        session['menu'] = menu
        session['data_ref'] = None

        if id_dash in m.dashboards:
            data = m.get_data_dashboard(id_dash,empresa,filial)
        else:
            return render_template('dashboards_v1/permissao_negada.html',m=m,proximo=proximo)
        
      
        #menu = 'Expedição'
        if data is not None:
            return render_template('dashboards_v1/dashboard.html',data=data, m=m, id_dashboard=id_dash)


@app.route('/dashboards/<int:id_dash>/<data_ref>', methods=['GET','POST'])
@login_required
def principal_data(id_dash, data_ref):
    if request.method == 'GET':        

        #Recebe os dados de login, empresa e filial
        #empresa = current_user.id.split(':')[2]
        #filial = current_user.id.split(':')[3]
        empresa = ''
        filial = ''
        
        if empresa == '':
            empresa = None
        
        if filial == '':
            filial = None

        session['data_ref'] = data_ref
        #Instancia objeto de Manager para controle
        m = Manager(current_user, empresa,filial)        
        
        #Recebe parametros das analises do dashboard         
        menu = session['menu']
        proximo = menu.pop(0)
        menu.append(proximo)
        session['menu'] = menu
        
        if id_dash in m.dashboards:
            data = m.get_data_dashboard(id_dash,empresa,filial, data_ref)
        else:
            return render_template('dashboards_v1/permissao_negada.html',m=m,proximo=proximo,id_dashboard=id_dash)
                         
        #menu = 'Expedição'
        if data is not None:
            return render_template('dashboards_v1/dashboard.html',data=data, m=m)


@app.route('/dashboards/relogin', methods=['GET', 'POST'])     
@app.route('/dashboards/login', methods=['GET', 'POST'])
def login_dashboard():
    #print('Entrei aqui')
    if request.path == '/dashboards/relogin':
        msg = 'Login Inválido!'        
    else:
        msg = None

    if current_user.is_authenticated():                    
        return redirect('/dashboards/')        

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']  
        ambient  = request.form['ambient']
        cod_empresa  = request.form['cod_empresa']
        cod_filial   = request.form['cod_filial']
        
        #Autenticacao de Usuario
        username    = username.lower()
        password    = password.lower()
        cod_empresa = cod_empresa.lower()
        cod_filial  = cod_filial.lower()
        ambient     = ambient.lower()

        m = Manager(cod_empresa,cod_filial)  
        r = m.load_user(username,password,ambient)         
          
        if r is None:                       
            return redirect('/dashboards/relogin') 
        
        #Valida Empresa e Filial
        if cod_empresa != '':
            if m.load_empresa(cod_empresa,ambient) is None:
                return redirect('/dashboards/relogin') 

        if cod_filial != '':
            if m.load_filial(cod_empresa,cod_filial, ambient) is None:
                return redirect('/dashboards/relogin') 

        #Cria sessão do login bem sucedido
        user = User(username+':'+ambient+':'+cod_empresa+':'+cod_filial)
        login_user(user)            
        
        #Faz redirecionamento
        m.user = user
        m.id_db = 'softlog_' + user.id.split(':')[1]
        m.load_menu_dashboard()
        id_dash = m.dashboards[0]
        return redirect('/dashboards/%i' % (id_dash))
    else:
        return render_template('dashboards_v1/login.html',msg=msg)        


@app.route("/dashboards/reload_empresas/<codigo_empresa>/<int:id_dash>")
@login_required
def reload_empresas(codigo_empresa, id_dash):
    if codigo_empresa == 'todos':
        session['codigo_empresa_dashboard'] = ""
        session['codigo_filial_dashboard'] = ""
    else:
        session['codigo_empresa_dashboard'] = codigo_empresa

    if id_dash==0:
        return redirect('/dashboards/')
    else:
        return redirect('/dashboards/%i' % id_dash)


@app.route("/dashboards/reload_filiais/<codigo_empresa>/<codigo_filial>/<int:id_dash>")
@login_required
def reload_filiais(codigo_empresa, codigo_filial, id_dash):
    if codigo_empresa == 'todos':
        session['codigo_empresa_dashboard'] = ""
        session['codigo_filial_dashboard'] = ""
    elif codigo_filial == 'todos':
        session['codigo_filial_dashboard'] = ""
    else:
        session['codigo_filial_dashboard'] = codigo_filial

    if id_dash==0:
        return redirect('/dashboards/')
    else:
        return redirect('/dashboards/%i' % id_dash)

# somewhere to logout
@app.route("/dashboards/logout")
@login_required
def logout_dashboard():
    logout_user()   
    return redirect('/dashboards/')

#handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return redirect('/dashboards/login')    
    
## callback to reload the user object        
#@login_manager_dashboard.user_loader
#def load_user(userid):     
#    return User(userid)    

