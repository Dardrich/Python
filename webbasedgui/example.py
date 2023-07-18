from dotenv import load_dotenv

load_dotenv()

# from flask import Flask, render_template_string
# app = Flask(__name__)

# @app.route('/')
# @app.route('/<username>')
# def named_page(username="Stranger"):
#     page = '''
# <!DOCTYPE html>
# <html>
#     <head>
#         <meta charset="utf-9"/>
#         <title>{{ template_name }}</title>  
#     </head>
#     <body>
#         <h1 style="color:orange">DDP-1</h1>
#         <p>
#             Web-Based GUI(<i>Graphical User Interface</i>)
#         </p>
#         <p> Hello <b style="color:"pink">{{template_name}} </b>. Selamat belajar <b style="color:yellow">Python</b></p>
#     </body>
# </html>
# '''
#     return render_template_string(page, template_name=username)

# if __name__ == "__main__":
#     app.run(debug=True)