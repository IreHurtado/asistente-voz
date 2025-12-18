import re
from app.flows.constants import *

def normalizar(texto: str) -> str:
    texto = texto.lower()
    texto = texto.replace("á", "a").replace("é", "e").replace("í", "i") \
                 .replace("ó", "o").replace("ú", "u")
    texto = re.sub(r"[^\w\s]", "", texto)
    return texto.strip()

# =====================================================
# INTENTS GENERALES (NO FAISS)
# =====================================================

GENERAL_INTENTS = [
    
    {
    "key": "caso_personal",
    "patterns": [
        "mi caso es",
        "en mi caso",
        "mi situacion",
        "es diferente",
        "es distinto",
        "perdi el documento",
        "solo tengo copia",
        "es urgente",
        "urgente",
        "estoy fuera del pais",
        "no estoy en peru",
        "somos varios",
        "uno no quiere firmar",
        "no quiere firmar",
        "mi caso es especial",
        "el menor vive conmigo",
        "el menor no vive conmigo",
        "el padre vive en el extranjero",
        "estoy confundido",
        "estoy confundida",
        "me explicaron mal",
        "no entiendo",
        "no me queda claro",
        "vive en el extranjero",
        "vive fuera",
        "esta fuera del pais",
        "esta en madrid",
        "no esta en peru",
        "el papa vive",
        "la mama vive",
        "uno vive afuera",
        "no puede venir",
        "no puede viajar",
        "no puede firmar",
        "no esta presente"
        
    ],
    "respuesta": (
        "Entendemos que cada trámite notarial puede tener situaciones particulares.\n\n"
        "Para poder orientarte correctamente, necesitamos conocer "
        "qué trámite deseas realizar y cuáles son los documentos que tienes disponibles.\n\n"
        "Con esa información podremos indicarte los requisitos y, de ser el caso, "
        "el costo aproximado del trámite.\n\n"
        "Envíanos los detalles por WhatsApp y con gusto te ayudamos:\n"
        f"{WHATSAPP_URL}"
    )
    },


    {
        "key": "precios",
        "patterns": [
            "precio",
            "precios",
            "costo",
            "cuanto cuesta",
            "cuanto vale",
            "tarifa",
            "cuanto cobran"
        ],
        "respuesta": (
            "El costo de un trámite notarial depende del tipo de trámite "
            "y de los documentos que se presenten.\n\n"
            "Si deseas conocer los requisitos del trámite, indícanos primero "
            "qué trámite necesitas realizar.\n\n"
            "Y para poder cotizar tu caso específico, "
            "envíanos los documentos o detalles por WhatsApp:\n"
            f"{WHATSAPP_URL}"
        )
    },

    {
    "key": "recojo_tarjeta_vehicular",
    "patterns": [
        "recojo de tarjeta vehicular",
        "recoger tarjeta vehicular",
        "mi tarjeta ya esta lista",
        "cuando recojo mi tarjeta",
        "ya salio mi tarjeta",
        "quiero recoger mi tarjeta"
    ],
    "respuesta": (
        "Para confirmar si tu tarjeta de identificación vehicular ya está lista "
        "o coordinar su recojo, envíanos por WhatsApp una foto de tu boleta "
        "para ubicarla rápidamente:\n\n"
        f"{WHATSAPP_URL}"
    )
    },


    {
        "key": "recojo_documentos",
        "patterns": [
            "recoger documento",
            "estado de tramite",
            "estado de mi tramite",
            "firme hace días",
            "deje documentos"
        ],
        "respuesta": (
            "Con gusto te ayudamos a verificar el estado de tu trámite o el recojo de tu documento.\n\n"
            "Por favor envíanos por WhatsApp una foto de tu boleta o, en su defecto, "
            "tu nombre completo y DNI:\n"
            f"{WHATSAPP_URL}"
        )
    },

    {
        "key": "contacto_notario",
        "patterns": [
            "hablar con el notario",
            "quiero hablar con el notario",
            "otro numero",
            "numero del notario",
            "hablar con abogado"
        ],
        "respuesta": (
            "La atención telefónica y por WhatsApp es realizada por el personal administrativo "
            "de la notaría, quienes se encargan de recibir consultas y orientar sobre los trámites.\n\n"
            "La atención directa del notario o de un abogado se realiza de manera presencial "
            "o a través de los canales correspondientes según el trámite.\n\n"
            "Para cualquier consulta inicial, puedes comunicarte por WhatsApp:\n"
            f"{WHATSAPP_URL}"
        )
    },

    
    {
    "key": "carta_notarial_direccion",
    "patterns": [
        "mandar carta",
        "enviar carta",
        "carta a una direccion",
        "carta a domicilio",
        "mandar carta a",
        "mandar carta notarial"
    ],
    "respuesta": (
        "Para enviar una carta notarial a una dirección específica, "
        "revisa los requisitos generales aquí:\n"
        f"{CARTA_NOTARIAL_URL}\n\n"
        "Para confirmar si se puede diligenciar a esa dirección, "
        "envíanos los datos por WhatsApp:\n"
        f"{WHATSAPP_URL}"
    )
    },
    
    {
    "key": "festivos",
    "patterns": [
        "hoy atienden",
        "abren hoy",
        "atienden hoy",
        "atienden hoy feriado",
        "hoy es feriado",
        "abren feriado",
        "atienden feriado"
    ],
    "respuesta": (
        "La atención puede variar según la fecha.\n\n"
        "Para saber si atendemos hoy, te recomendamos revisar nuestro Facebook oficial:\n"
        f"{FACEBOOK_URL}"
    )
    },



    {
        "key": "quejas",
        "patterns": [
            "queja",
            "quejarme",
            "reclamo",
            "reclamar",
            "me atendieron mal",
            "atienden mal",
            "atienden fatal",
            "mal servicio",
            "no atienden bien",
            "me trataron mal",
            "pesima atencion",

        ],
        "respuesta": (
            "Lamentamos el inconveniente.\n\n"
            "Para poder ayudarte mejor y revisar tu caso con detalle, "
            "por favor escríbenos por WhatsApp:\n"
            f"{WHATSAPP_URL}"
        )
    },


]

SALUDOS = [
    "hola",
    "buenas",
    "buen",
    "buenos",
    "buenas",
    "dia",
    "dias",
    "tardes",
    "noches"
]


# =====================================================
# DETECTORES
# =====================================================

def detectar_saludo(texto: str) -> str | None:
    texto_norm = normalizar(texto)
    palabras = texto_norm.split()

    # límite suave para evitar frases largas
    if len(palabras) <= 4:
        if all(p in SALUDOS for p in palabras):
                return (
                    "¡Hola! 😊\n\n"
                    "¿En qué trámite notarial puedo ayudarte?\n"
                )
    return None

def detectar_intent_general(texto: str) -> str | None:
    texto_norm = normalizar(texto)

    for intent in GENERAL_INTENTS:
        for patron in intent["patterns"]:
            if re.search(rf"\b{re.escape(patron)}\b", texto_norm):
                return intent["respuesta"]

    return None
