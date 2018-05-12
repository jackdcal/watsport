import pycountry
#from django.utils.text import slugify


''''

def get_unique_slug(model_instance, slug_field_name):
    """
    Takes a model instance, sluggable field name (such as 'title') of that
    model as string, slug field name (such as 'slug') of the model as string;
    returns a unique slug as string.
    """
    #slugable_fields_attr = model_instance.__str__()-model_instance.date
    slug = slugify(model_instance.__str__()'-{model_instance.date}')
    unique_slug = slug
    extension = 1
    ModelClass = model_instance.__class__
 
    while ModelClass._default_manager.filter(
        **{slug_field_name: unique_slug}
    ).exists():
        unique_slug = '{}-{}'.format(slug, extension)
        extension += 1
 
    return unique_slug


#def getcountry():

 #   countries_list = ()
 #   for country in pycountry.countries:
 #       countries_list += ((country.alpha_2, country.name),)
#
#    return countries_list

#countr_l = getcountry()
#print(countr_l)

#def findcountry():
#    uk = pycountry.countries.get(alpha_2='GB')
#    return uk
#gb = findcountry()
#print(gb)



##def subdiv():
#    subcountry = pycountry.subdivisions.get(country_code='GB')
#    return subcountry
#hit = subdiv()
#print(hit)

#def findeng():
#    all = pycountry.subdivisions.get(country_code='GB')
#    provinces = []
#    provincelist = list(pycountry.subdivisions.get(country_code='GB'))
#    for p in provincelist:
#        provinces.append((p.code.split('-')[1], p.name))
#    provinces = sorted(provinces)
#    return provinces
#eng = findeng()
#print(eng)

#def uksub():
#    provinces = []
#    provincelist = list(pycountry.subdivisions.get(country_code='GB'))
#    provinces = provincelist[0].parent
    #provinces = sorted(provinces)
#   return provinces
#parent = uksub()
#print(parent)

def getcountry():

    countries_list = ()
    uk_home_nations = (England, Scotland, Wales, Northern Ireland)
    for country in pycountry.countries:
        countries_list += ((country.alpha_2, country.name),)
        countries

    return countries_list

countr_l = getcountry()

def ukhomenation():
    prov = ()
    provincelist = list(pycountry.subdivisions.get(country_code='GB'))
    a = ()
    for p in provincelist:
        try:
            a = (p.parent.code,p.parent.name)
            prov += ((a),)
        except AttributeError:
            break
    prov = sorted(list(set(prov)))
    return (prov)
hnation = ukhomenation()
print(hnation)
'''

def ukhomenation():
    prov = ()
    provincelist = list(pycountry.subdivisions.get(country_code='GB'))
    a = ('',)
    for p in provincelist:
        try:
            a = (p.parent.code,p.parent.name)
            prov += ((a),)
        except AttributeError:
            break
    prov = set(prov)
    prov = tuple(prov)
    return (prov)


def getcountry():
    countries_list = ()
    ukhn = ukhomenation()
    for country in pycountry.countries:
        countries_list += ((country.alpha_2, country.name),)
    countries_list += ukhn
    countries_list = tuple(sorted(countries_list, key=lambda country:country[1]))

    return countries_list

re = ukhomenation()
countr_l = getcountry()

#print(countr_l)
country = 'Russian Federation'

def findcode():

    xval = [item[0] for item in countr_l if item[1] == country]
            #xval = pycountry.countries.get(name=self.country)
    country_code = xval[0]
    return country_code
rrr = findcode()
print (rrr)
