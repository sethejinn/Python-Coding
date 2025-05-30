class CV:
    def __init__(self):
        self.nombre_apellidos = ""
        self.email = ""
        self.telefono = ""
        self.estudios = []
        self.experiencia = []
        self.certificados = []
        self.idiomas = []

    def agregar_nombre_apellidos(self, nombre_apellidos):
        self.nombre_apellidos = nombre_apellidos

    def agregar_email(self, email):
        self.email = email

    def agregar_telefono(self, telefono):
        self.telefono = telefono

    def agregar_estudio(self, estudio):
        self.estudios.append(estudio)

    def agregar_experiencia(self, experiencia):
        self.experiencia.append(experiencia)

    def agregar_certificado(self, certificado):
        self.certificados.append(certificado)

    def agregar_idioma(self, idioma):
        self.idiomas.append(idioma)

    def limpiar_datos(self):
        self.nombre_apellidos = ""
        self.email = ""
        self.telefono = ""
        self.estudios = []
        self.experiencia = []
        self.certificados = []
        self.idiomas = []

    def generar_cv_html(self):
        html = f"""
        <div id="header"></div>
        <div class="left"></div>
        <div class="stuff">
          <br><br>
          <h1>CV</h1>
          <h2>{self.nombre_apellidos}</h2>
          <hr />
          <br>
          <p class="head">Contacto</p>
          <ul>
            <li>Email: {self.email}</li>
            <li>Teléfono: {self.telefono}</li>
          </ul>
          <p class="head">Estudios</p>
          <ul>
        """

        for estudio in self.estudios:
            html += f"<li>Año: {estudio[0]}, Título: {estudio[1]}</li>"

        html += """
          </ul>
          <p class="head">Experiencia Laboral</p>
          <ul>
        """

        for exp in self.experiencia:
            html += f"<li>Año: {exp[0]}, Descripción: {exp[1]}</li>"

        if self.certificados:
            html += """
              </ul>
              <p class="head">Certificados</p>
              <ul>
            """
            for certificado in self.certificados:
                html += f"<li>{certificado}</li>"

        if self.idiomas:
            html += """
              </ul>
              <p class="head">Idiomas</p>
              <ul>
            """
            for idioma in self.idiomas:
                html += f"<li>{idioma}</li>"

        html += """
          </ul>
        </div>
        <div class="right"></div>
        <div id="footer">
        </div>
        """
        return html

print("¡Bienvenido al CV Generator de MG!")

cv = CV()

nombre_apellidos = input("Introduce tu nombre y apellidos: ")
cv.agregar_nombre_apellidos(nombre_apellidos)

email = input("Introduce tu email: ")
cv.agregar_email(email)
telefono = input("Introduce tu número de teléfono: ")
cv.agregar_telefono(telefono)

while True:
    año_estudio = input("Introduce el año en el que cursaste tu formación: ")
    titulo_estudio = input("Introduce el título de tu formación: ")
    cv.agregar_estudio((año_estudio, titulo_estudio))
    agregar_otro = input("¿Quieres añadir otro estudio? (s/n): ")
    if agregar_otro.lower() != 's':
        break

while True:
    año_experiencia = input("Introduce el intervalo de tu experiencia laboral: ")
    descripcion_experiencia = input("Introduce la descripción de esta experiencia laboral: ")
    cv.agregar_experiencia((año_experiencia, descripcion_experiencia))
    agregar_otra = input("¿Quieres añadir otra experiencia laboral? (s/n): ")
    if agregar_otra.lower() != 's':
        break

agregar_certificados = input("¿Quieres añadir certificados? (s/n): ")
if agregar_certificados.lower() == 's':
    while True:
        certificado = input("Introduce un certificado: ")
        cv.agregar_certificado(certificado)
        agregar_otro = input("¿Quieres añadir otro certificado? (s/n): ")
        if agregar_otro.lower() != 's':
            break

agregar_idiomas = input("¿Quieres añadir idiomas? (s/n): ")
if agregar_idiomas.lower() == 's':
    while True:
        idioma = input("Introduce un idioma: ")
        cv.agregar_idioma(idioma)
        agregar_otro = input("¿Quieres añadir otro idioma? (s/n): ")
        if agregar_otro.lower() != 's':
            break

cv_html = cv.generar_cv_html()

with open("cv_generado.html", "w") as file:
    file.write(cv_html)

print("¡Gracias por usar CV Generator de MG! Tu CV ha sido generado como cv_generado.html!")
