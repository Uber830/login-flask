from app import app, status_401, status_404, csrf

# run aplication
if __name__ == "__main__":
    #app.config.from_object(config["development"])
    app.register_error_handler(401 ,status_401)
    app.register_error_handler(404 ,status_404)
    csrf.init_app(app)
    app.run(debug=True)
