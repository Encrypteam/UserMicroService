import os

from main import create_app

from logging.config import dictConfig



dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'DEBUG',
        'handlers': ['wsgi']
    }
})

app = create_app()
app.app_context().push()



if __name__ == '__main__':
    app.run(debug=True, port=os.getenv('PORT'), host='0.0.0.0')
