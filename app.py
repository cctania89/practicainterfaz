import web
urls = (
    '/', 'aplication.controllers.index.Index',
    '/acercade', 'aplication.controllers.acercade.Acercade',
    '/insertar', 'aplication.controllers.insertar.Insertar',

)
render = web.template.render('templates/', base='master')


class index:        
    def GET(self):
        datos = ['Tania', '00258847@red.unid.mx']
	return render.index(datos)
    


class acercade:
    def GET(self):
	return render.acercade()

class insertar:
    def GET(self):
	return render.insertar()
  
 
if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
