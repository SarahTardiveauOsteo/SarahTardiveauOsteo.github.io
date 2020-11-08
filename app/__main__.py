import os

from flask import Flask, render_template

from database.tools import initialize_databases, create_tables


DIR_APP = os.path.abspath(os.path.dirname(__file__))
DIR_TEMPLATES = os.path.join(DIR_APP, "templates")
DIR_STATIC = os.path.join(DIR_APP, "static")

application = Flask(__name__, template_folder=DIR_TEMPLATES, static_folder=DIR_STATIC)


@application.route("/")
def root():
    return render_template("index.html")


@application.route("/services/consulter-calendrier")
def consulter_calendrier():
    return False


@application.route("/services/deplacer-rdv")
def deplacer_rdv():
    return False


@application.route("/services/reserver-rdv")
def reserver_rdv():
    return False


@application.route("/services/annuler-rdv")
def annuler_rdv():
    return False


def run_development():
    # port = "80"  # HTTP port
    port = "443"  # HTTPS port

    # Setup SSL
    domain_name = "sarahtardiveau-osteo.fr"
    ssl_context = (
        '/etc/letsencrypt/live/' + domain_name + '/cert.pem',    # Certification
        '/etc/letsencrypt/live/' + domain_name + '/privkey.pem'  # Private key
    )

    application.run(host="0.0.0.0", ssl_context=ssl_context, port=port, debug=False)


def run_debug():
    port = "5000"  # Default Flask port
    application.run(host="127.0.0.1", port=port, debug=True)


if __name__ == "__main__":
    run_debug()
