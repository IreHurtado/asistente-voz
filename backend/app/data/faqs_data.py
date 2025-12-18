from app.flows.constants import *

# =========================
# FAQs DEL ASISTENTE (FAISS)
# =========================

FAQS = [

    # =====================================================
    # GENERALIDADES
    # =====================================================

    {
        "key": "documentos_generales",
        "pregunta": "¿Qué documentos se necesitan para realizar un trámite en la notaría?",
        "respuesta": (
            "Los documentos necesarios pueden variar según el tipo de trámite que desees realizar.\n\n"
            "Para poder orientarte correctamente, indícanos qué trámite necesitas "
            "(por ejemplo: compraventa, carta notarial, divorcio, transferencia vehicular, etc.) "
            "y con gusto te brindaremos la información correspondiente."
        )
    },

    {
        "key": "duracion_tramite",
        "pregunta": "¿Cuánto tiempo puede demorar un trámite notarial en general?",
        "respuesta": (
            "El tiempo de atención de un trámite notarial puede variar según el tipo de trámite "
            "y la documentación presentada.\n\n"
            "Cada caso es distinto, por lo que los plazos pueden cambiar."
        )
    },

    {
        "key": "atencion_con_cita",
        "pregunta": "¿Es necesario sacar una cita previa para ser atendido en la notaría?",
        "respuesta": (
            "Puedes apersonarte a la notaría con tus documentos y, "
            "de acuerdo al flujo de atención del día, serás atendido.\n\n"
            "Si deseas coordinar una atención previa, puedes comunicarte por nuestros canales de contacto."
        )
    },

    {
        "key": "horario",
        "pregunta": "¿Cuál es el horario de atención de la notaría?",
        "respuesta": (
            "Nuestro horario de atención es:\n\n"
            "Lunes a viernes: de 9:00 a. m. a 6:00 p. m.\n"
            "Sábados: de 9:00 a. m. a 1:00 p. m.\n"
            "Domingos: no atendemos."
        )
    },

    {
        "key": "ubicacion",
        "pregunta": "¿Dónde está ubicada la notaría y cómo puedo llegar?",
        "respuesta": (
            "La notaría se encuentra ubicada en:\n\n"
            "📍 Manuel Ubalde N.º 1060, distrito de El Porvenir.\n\n"
            "Puedes ver la ubicación exacta y cómo llegar en Google Maps aquí:\n"
            f"{MAPS_URL}"
        )
    },

    # =====================================================
    # ESCRITURAS PÚBLICAS
    # =====================================================

    {
        "key": "compraventa",
        "pregunta": "¿Cómo es el trámite de compraventa de una casa o inmueble en notaría?",
        "respuesta": (
            "Puedes revisar la información y los requisitos para realizar una compraventa aquí:\n"
            f"{ESCRITURAS_URL}"
        )
    },

    {
        "key": "donacion",
        "pregunta": "¿Qué se necesita para realizar una donación de bienes ante notaría?",
        "respuesta": (
            "Puedes revisar la información y los requisitos para la donación aquí:\n"
            f"{DONACION_URL}"
        )
    },

    {
        "key": "hipoteca",
        "pregunta": "¿En qué consiste la constitución de una hipoteca ante notaría?",
        "respuesta": (
            "Puedes revisar la información y los requisitos para la constitución de una hipoteca aquí:\n"
            f"{HIPOTECA_URL}"
        )
    },

    {
        "key": "levantamiento_hipoteca",
        "pregunta": "¿Cómo se realiza el levantamiento o cancelación de una hipoteca?",
        "respuesta": (
            "Puedes revisar la información y los requisitos para el levantamiento de hipoteca aquí:\n"
            f"{LEV_HIPOTECA_URL}"
        )
    },

    {
        "key": "anticipo_legitima",
        "pregunta": "¿Qué es un anticipo de legítima o adelanto de herencia?",
        "respuesta": (
            "Puedes revisar la información y los requisitos para el anticipo de legítima aquí:\n"
            f"{LEGITIMA_URL}"
        )
    },

    {
        "key": "constitucion_empresas",
        "pregunta": "¿Cómo se puede constituir una empresa o sociedad en notaría?",
        "respuesta": (
            "Puedes revisar la información y los requisitos para la constitución de empresas aquí:\n"
            f"{EMPRESAS_URL}"
        )
    },

    {
        "key": "modificacion_estatutos",
        "pregunta": "¿En qué casos se realiza la modificación de estatutos de una empresa?",
        "respuesta": (
            "Puedes revisar la información y los requisitos para la modificación de estatutos aquí:\n"
            f"{MOD_EST_URL}"
        )
    },

    {
        "key": "aumento_capital",
        "pregunta": "¿Cómo se realiza un aumento de capital social?",
        "respuesta": (
            "Puedes revisar la información y los requisitos para el aumento de capital aquí:\n"
            f"{CAPITAL_URL}"
        )
    },

    {
        "key": "constitucion_asociacion",
        "pregunta": "¿Cómo se constituye una asociación ante notaría?",
        "respuesta": (
            "Puedes revisar la información y los requisitos para la constitución de asociaciones aquí:\n"
            f"{ASOCIACION_URL}"
        )
    },

    {
        "key": "matrimonio",
        "pregunta": "¿Cómo se realiza un matrimonio civil notarial?",
        "respuesta": (
            "Puedes revisar la información y los requisitos para el matrimonio civil aquí:\n"
            f"{MATRIMONIO_URL}"
        )
    },

    # =====================================================
    # ASUNTOS NO CONTENCIOSOS
    # =====================================================

    {
        "key": "sucesion_intestada",
        "pregunta": "¿Qué es una sucesión intestada y cuándo se puede tramitar en notaría?",
        "respuesta": (
            "Puedes revisar los requisitos para la sucesión intestada aquí:\n"
            f"{NO_CONTENCIOSO_URL}"
        )
    },

    {
        "key": "rectificacion_partida",
        "pregunta": "¿En qué casos se puede solicitar la rectificación de una partida?",
        "respuesta": (
            "Puedes revisar la información y los requisitos para la rectificación de partidas aquí:\n"
            f"{RECTIFICACION_URL}"
        )
    },

    {
        "key": "union_hecho",
        "pregunta": "¿Qué es una unión de hecho y cómo se formaliza en notaría?",
        "respuesta": (
            "Puedes revisar la información y los requisitos para la unión de hecho aquí:\n"
            f"{UNION_HECHO_URL}"
        )
    },

    {
        "key": "cese_union",
        "pregunta": "¿Cómo se realiza el cese de una unión de hecho?",
        "respuesta": (
            "Puedes revisar la información y los requisitos para el cese de unión de hecho aquí:\n"
            f"{CESE_UNION_URL}"
        )
    },

    {
        "key": "divorcio",
        "pregunta": "¿En qué casos se puede realizar un divorcio notarial?",
        "respuesta": (
            "Puedes revisar la información y los requisitos del divorcio notarial aquí:\n"
            f"{DIVORCIO_URL}"
        )
    },

    {
        "key": "patrimonio_familiar",
        "pregunta": "¿Cómo se constituye un patrimonio familiar ante notaría?",
        "respuesta": (
            "Puedes revisar la información y los requisitos para la constitución de patrimonio familiar aquí:\n"
            f"{PATRIMONIO_URL}"
        )
    },

    {
        "key": "adopcion",
        "pregunta": "¿En qué consiste la adopción de personas capaces ante notaría?",
        "respuesta": (
            "Puedes revisar la información y los requisitos para la adopción de personas capaces aquí:\n"
            f"{ADOPCION_URL}"
        )
    },

    {
        "key": "prescripcion_inmueble",
        "pregunta": "¿Qué es la prescripción adquisitiva de un inmueble?",
        "respuesta": (
            "Puedes revisar la información y los requisitos para la prescripción de inmueble aquí:\n"
            f"{PRESC_INM_URL}"
        )
    },

    {
        "key": "prescripcion_vehicular",
        "pregunta": "¿Qué es la prescripción adquisitiva vehicular?",
        "respuesta": (
            "Puedes revisar la información y los requisitos para la prescripción vehicular aquí:\n"
            f"{PRESC_VEH_URL}"
        )
    },

    # =====================================================
    # TESTAMENTOS
    # =====================================================

    {
        "key": "testamentos",
        "pregunta": "¿Qué tipos de testamentos se pueden realizar en notaría?",
        "respuesta": (
            "Puedes revisar la información sobre testamentos y disposiciones de última voluntad aquí:\n"
            f"{TESTAMENTOS_URL}"
        )
    },

    # =====================================================
    # VEHICULARES
    # =====================================================

    {
        "key": "transferencia_vehiculo",
        "pregunta": "¿Cómo se realiza la transferencia de un automóvil en notaría?",
        "respuesta": (
            "Puedes revisar los requisitos para la transferencia vehicular aquí:\n"
            f"{VEHICULAR_URL}"
        )
    },

    {
        "key": "transferencia_moto",
        "pregunta": "¿Cómo se realiza la transferencia de una moto o vehículo menor?",
        "respuesta": (
            "Puedes revisar los requisitos para la transferencia de moto o vehículo menor aquí:\n"
            f"{MOTO_URL}"
        )
    },

    {
        "key": "cambio_caracteristicas",
        "pregunta": "¿En qué casos se realiza el cambio de características vehiculares?",
        "respuesta": (
            "Puedes revisar la información y requisitos para el cambio de características aquí:\n"
            f"{CARACTERISTICAS_URL}"
        )
    },

    {
        "key": "duplicado_tarjeta",
        "pregunta": "¿Cómo se solicita un duplicado de la tarjeta de propiedad vehicular?",
        "respuesta": (
            "Puedes revisar la información y requisitos para el duplicado de tarjeta de propiedad aquí:\n"
            f"{DUPLICADO_URL}"
        )
    },

    # =====================================================
    # EXTRAPROTOCOLAR
    # =====================================================

    {
        "key": "poderes_fuera_registro",
        "pregunta": "¿Qué son los poderes fuera de registro y cuándo se utilizan?",
        "respuesta": (
            "Puedes revisar la información y requisitos para poderes fuera de registro aquí:\n"
            f"{PODERES_URL}"
        )
    },

    {
        "key": "autorizacion_viaje",
        "pregunta": "¿Cómo se tramita una autorización de viaje para un menor de edad?",
        "respuesta": (
            "Puedes revisar los requisitos para la autorización de viaje aquí:\n"
            f"{AUT_VIAJE_URL}"
        )
    },

    {
        "key": "carta_notarial",
        "pregunta": "¿Qué es una carta notarial y para qué se utiliza?",
        "respuesta": (
            "Puedes revisar la información y requisitos para cartas notariales aquí:\n"
            f"{CARTA_NOTARIAL_URL}"
        )
    },

    {
        "key": "legalizacion_firmas",
        "pregunta": "¿En qué consiste la legalización de firmas ante notaría?",
        "respuesta": (
            "Puedes revisar la información sobre legalización de firmas aquí:\n"
            f"{LEGAL_FIRMAS_URL}"
        )
    },

    {
        "key": "legalizacion_copias",
        "pregunta": "¿Qué es la legalización de copias y cuándo se necesita?",
        "respuesta": (
            "Puedes revisar la información sobre legalización de copias aquí:\n"
            f"{COPIAS_URL}"
        )
    },

    {
        "key": "apertura_libro_natural",
        "pregunta": "¿Cómo se realiza la apertura de libros para persona natural?",
        "respuesta": (
            "Puedes revisar la información sobre la apertura de libros para persona natural aquí:\n"
            f"{LIBRO_NAT_URL}"
        )
    },

    {
        "key": "apertura_libro_juridica",
        "pregunta": "¿Cómo se realiza la apertura de libros para persona jurídica?",
        "respuesta": (
            "Puedes revisar la información sobre la apertura de libros para persona jurídica aquí:\n"
            f"{LIBRO_JUR_URL}"
        )
    },
]
