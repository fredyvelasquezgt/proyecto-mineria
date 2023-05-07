

def get_ocupaciones_info():
    return {'Agricultores y trabajadores calificados de explotaciones agropecuarias con destino al mercado': 1,
            'Artesanos y operarios de las artes gráficas': 2,
            'Ayudantes de preparación de alimentos': 3,
            'Conductores de vehículos y operadores de equipos pesados móviles': 4,
            'Directores administradores y comerciales': 5,
            'Directores ejecutivos, personal directivo de administración pública, miembros del poder ejecutivo y cuerpos legislativos': 6,
            'Directores y gerentes de producción y operaciones': 7,
            'Empleados contables y encargados del registro de materiales': 8,
            'Empleados en trato directo con el público': 9,
            'Ensambladores': 10,
            'Especialistas en organización de la administración publica y de empresas': 11,
            'Gerentes de hoteles, restaurantes, comercios y otros servicios': 12,
            'Limpiadores y asistentes': 13,
            'No especificado en otro grupo': 14,
            'Oficiales de las fuerzas armadas': 15,
            'Oficiales y operarios de la construcción excluyendo electricistas': 16,
            'Oficiales y operarios de la metalurgia, la construcción mecánica y afines': 17,
            'Oficinistas': 18,
            'Operadores de instalaciones fijas y máquinas': 19,
            'Operarios y oficiales de procesamiento de alimentos, de la confección, ebanistas, otros artesanos y afines': 20,
            'Otro personal de apoyo administrativo': 21,
            'Otros miembros de las fuerzas armadas': 22,
            'Peones agropecuarios, pesqueros y forestales':  23,
            'Peones de la minería, la construcción, la industria manufacturera y el transporte': 24,
            'Personal de los servicios de protección': 25,
            'Profesionales de la enseñanza':  26,
            'Profesionales de la salud': 27,
            'Profesionales de las ciencias y de la ingeniería': 28,
            'Profesionales de las ciencias y la ingeniería de nivel medio': 29,
            'Profesionales de nivel medio de la salud': 30,
            'Profesionales de nivel medio de servicios jurídicos, sociales, culturales y afines': 31,
            'Profesionales de nivel medio en operaciones financieras y administrativas': 32,
            'Profesionales de tecnología de la información y las comunicaciones': 33,
            'Profesionales en derecho, en ciencias sociales y culturales': 34,
            'Recolectores de desechos y otras ocupaciones elementales': 35,
            'Trabajadores de los cuidados personales': 36,
            'Trabajadores de los servicios personales': 36,
            'Trabajadores especializados en electricidad y la elecrotecnología': 37,
            'Técnicos de la tecnología de la información y las comunicaciones': 38,
            'Vendedores': 39,
            'Vendedores ambulantes de servicios y afines': 40
            }

def map_code(code):
    content = {
        '61': 1, '73': 2, '94': 3, '83': 4, '12': 5, '11': 6, '13': 7, '43': 8, '42': 9, '82': 10,
        '24': 11, '14': 12, '91': 13, 'NE': 14, '01': 15, '71': 16, '72': 17, '41': 18, '81': 19, '75': 20,
        '44': 21, '03': 22, '92': 23, '93': 24, '54': 25, '23': 26, '22': 27, '21': 28, '31': 29, '32': 30,
        '34': 31, '33': 32, '25': 33, '26': 34, '96': 35, '51': 36, '74': 37, '35': 38, '52': 39, '95': 40, 
        '03': 22, '62': 41
    }
    return content.get(code[:2], 0)
