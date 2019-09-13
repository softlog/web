from flask_babel import format_currency, numbers
import datetime
import geocoder
import hashlib

def format_value(v):    

    if str(type(v)) == "<class 'decimal.Decimal'>":
        return numbers.format_currency(v, 'COP', u'#,##0.00', locale='es_ES', currency_digits=False)

    if str(type(v)) == "<class 'datetime.datetime'>":
        return '{:%d/%m/%Y %H:%M}'.format(v)

    if str(type(v)) == "<class 'datetime.date'>":
        return '{:%d/%m/%Y}'.format(v)

    if v is None:
        return ''

    return v

def get_location(endereco, bairro, cidade, cep, nome):

    
    api_google = """AIzaSyDyKlnwxQjl9wilIcZyXZb8OPr_-fioDqY """

    if nome.find('LTDA') > -1:
        e = nome
        r = geocoder.google(e,key=api_google)
        if r.ok:
            print("Usando api Google")
            return [r.latlng[1],r.latlng[0]]
        else:
            print("Não encontrou com api google")
    
    e = endereco.split(',')[0] + ', ' + cidade + ', ' + cep
    
    r = geocoder.google(e,key=api_google)

    if r.ok:
        return [r.latlng[1],r.latlng[0]]

    return None
    e = endereco.split(',')[0] + ', ' + cidade + ', ' + cep
    
    r = geocoder.osm(e)

    if r.ok:
        return [r.osm['x'], r.osm['y']]

    return None    

    if r.ok:
        return [r.osm['x'], r.osm['y']]
    
    e = endereco.split(',')[0] + ', ' + cidade 

    r = geocoder.osm(e)
    if r.ok:
        return [r.osm['x'], r.osm['y']]

    return None

def calcula_hash(texto):    
    hash_object = hashlib.sha1(texto.encode())
    return hash_object.hexdigest()


def format_dmy_to_ymd(date_str):
    """Recebe uma data em string no formato dmy,
    retorna a data em string no formato ymd"""
    format_str = '%d-%m-%Y' # The format
    try:
        datetime_obj = datetime.datetime.strptime(date_str, format_str)
        return '{:%Y-%m-%d}'.format(datetime_obj)
    except:
        format_str = '%d/%m/%Y' # The format

    try:
        datetime_obj = datetime.datetime.strptime(date_str, format_str)
        return '{:%Y-%m-%d}'.format(datetime_obj)
    except:
        format_str = '%d%m%Y' # The format

    try:
        datetime_obj = datetime.datetime.strptime(date_str, format_str)
        return '{:%Y-%m-%d}'.format(datetime_obj)
    except:
        return None
