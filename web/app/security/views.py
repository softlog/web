from werkzeug.security import generate_password_hash
from wtforms import validators, PasswordField
from wtforms.validators import EqualTo

from flask_login import current_user, login_user, logout_user, login_required
from flask import flash, redirect, session, url_for, request, g, make_response, jsonify, abort, session
from flask import render_template, _app_ctx_stack, escape
from app.security.sqla.models import User
from app.security.forms import LoginForm
from app import app
from app import db, login

from app.models.gerais import Filial

@app.route('/sessao/')
def sessao():
    return escape(session)
@app.route('/login/<x_ambiente>', methods=['GET', 'POST'])
@app.route('/login/', methods=['GET', 'POST'],  defaults={'x_ambiente': None})
def login_frontend(x_ambiente):     
    
    if current_user is not None:
        if g.user.is_authenticated: 
                if g.user.categoria==2:
                    return redirect('/portal/webtracking/')
                else:
                    return redirect('/')


    form = LoginForm() 
        #logout_user()       

    if request.method == 'POST':
        
        usuario = form.username.data
        password = form.password.data
        if x_ambiente is not None:
            form.ambiente.data = x_ambiente
            form.empresa.data = '000'
            form.filial.data = '000'
        
        ambiente = form.ambiente.data
        
        codigo_empresa = form.empresa.data
        codigo_filial = form.filial.data          
                
        if not ambiente and not x_ambiente:            
            return render_template('security/login.html',msg="Informe o ambiente!",form=form)

        if not usuario:
            #flash(as_unicode(self.invalid_login_message), 'warning')            
            return render_template('security/login.html',msg="Informe o usuário!",form=form)

        if not password:
            return render_template('security/login.html',msg="Informe a senha!",form=form)
       
        if not codigo_empresa:
            return render_template('security/login.html',msg="Informe o código da empresa!",form=form)

        if not codigo_filial:
            return render_template('security/login.html',msg="Informe o código da filial!",form=form)


    if form.validate_on_submit():

        user = db.session.query(User).filter(User.login_name==usuario).order_by(User.categoria).first()
        
        if user is None or not user.check_password(password):
            ##flash('Usuario ou Senha incorretos')
            if x_ambiente is None:
                return render_template('security/login.html',msg="Usuário ou Senha incorreto!",form=form)
            else:
                return render_template('security/login.html/%s' % x_ambiente, msg="Usuário ou Senha incorreto!",form=form)
        

        filial = db.session.query(Filial)\
            .filter(Filial.codigo_empresa == codigo_empresa,\
            Filial.codigo_filial==codigo_filial).first()
        
        if not filial:
            if user.categoria == 2:
                filial = db.session.query(Filial).filter(Filial.ativa == 1).first()
            
            if filial:
                codigo_empresa = filial.codigo_empresa
                codigo_filial = filial.codigo_filial
            else:
                return render_template('security/login.html',msg="Filial Inexistente!",form=form)

        session['ambiente'] = ambiente
        session['codigo_empresa'] = codigo_empresa
        session['codigo_filial'] = codigo_filial
        session['codigo_empresa_dashboard'] = codigo_empresa
        session['codigo_filial_dashboard'] = codigo_filial

        login_user(user,remember=False)   
        if user.categoria==2:
            return redirect('/portal/webtracking/')
        return redirect('/index/')    
                      
        
            
        #login_user(user, remember=False, filial=filial)
        #return redirect(self.appbuilder.get_url_for_index)
    
    return render_template('security/login.html',form=form, ambiente=x_ambiente)
    #return self.render_template(self.login_template,
    #                title=self.title,
    #                form=form,
    #                appbuilder=self.appbuilder) 


@app.route("/logout")
@login_required
def logout_frontend():
    try:
        session.pop('ambiente')
        session.pop('codigo_empresa')
        session.pop('codigo_filial')
        session.pop('codigo_empresa_dashboard')
        session.pop('codigo_filial_dashboard')
    except:
        pass

    logout_user()
    return redirect('/')


@login.user_loader
def load_user(id):
    #print("Carregando Usuario", id)
    try:
        ambiente = session.get('ambiente')            
        from app import get_uri_db   
        id_db_tny = ambiente.lower()
        uri = None
        if id_db_tny is not None and getattr(_app_ctx_stack.top,'uri_request',None) is None:
            uri =  get_uri_db(id_db_tny)                
            getattr(_app_ctx_stack.top,'uri_request',None)
            setattr(_app_ctx_stack.top,'uri_request',uri)
    except:
        pass
    

    user =  db.session.query(User).filter(User.id_usuario==id).first()    
    
    return user

