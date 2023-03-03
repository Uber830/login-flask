from app import app, error_handler

# run aplication
if __name__ == "__main__":
    #app.config.from_object(config["development"])
    app.register_error_handler(404 ,error_handler)
    app.run(debug=True)
