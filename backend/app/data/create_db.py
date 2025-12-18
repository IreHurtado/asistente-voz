from app.database.faqs_repository import crear_tabla_faq, insertar_faq
from app.data.faqs_data import FAQS

crear_tabla_faq()

for faq in FAQS:
    insertar_faq(
        faq["pregunta"],
        faq["respuesta"],
    )

print("✔️ Base de datos creada.")
