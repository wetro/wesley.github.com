import flask, flask.views
app = flask.Flask(__name__)


@app.route('/')
def hello():
	return flask.render_template('index.html')


app.debug = True
app.run()		

# if __name__ == "__main__":
# 	app.run()

	
# import flask, flask.views
# app = flask.Flask(__name__)


# class About(flask.views.MethodView):
#    def get(self):
#        return flask.render_template('about.html')

    
# class View(flask.views.MethodView):
#     def get(self):
#         return flask.render_template('index.html')
        
#     def post(self):
#         return "Worked"
    
# @app.route('/about.html')
# def me():
#    return flask.render_template('index.html')



    
# app.add_url_rule('/',view_func=View.as_view('main'), methods = ['GET','POST'] )
# app.('me',view_func=About.as_view('main'), methods = ['GET','POST'])
# app.debug = True
# app.run()

