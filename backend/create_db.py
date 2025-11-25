from app.database.faqs_repository import crear_tabla_faq, insertar_faq

crear_tabla_faq()

datos = [
    ("¿Qué servicios ofrecen?", "Ofrecemos servicios notariales."),
    ("¿Cuál es el horario de atención?", "Atendemos de lunes a viernes de 9am a 6pm."),
    ("¿Dónde puedo ver mis facturas?", "En la página web, sección Facturación.")
]

for p, r in datos:
    insertar_faq(p, r)

print("✔️ Base de datos creada con ejemplos.")
