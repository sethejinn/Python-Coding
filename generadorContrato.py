from datetime import datetime

def generar_contrato():
    print("Generador de Contratos Laborales (España)\n")

    empresa = input("Nombre de la empresa: ")
    cif = input("CIF de la empresa: ")
    domicilio_social = input("Domicilio social: ")
    representante = input("Representante legal: ")

    nombre_trabajador = input("Nombre completo del trabajador: ")
    dni = input("DNI/NIE: ")
    domicilio = input("Domicilio del trabajador: ")
    discapacidad = input("¿Discapacidad reconocida? (sí/no): ")

    tipo_contrato = input("Tipo de contrato (indefinido / obra y servicio / eventual / interinidad): ").lower()
    fecha_inicio = input("Fecha de inicio (DD/MM/AAAA): ")
    fecha_fin = ""
    if tipo_contrato != "indefinido":
        fecha_fin = input("Fecha de finalización (DD/MM/AAAA): ")

    puesto = input("Puesto de trabajo: ")
    grupo = input("Grupo profesional: ")
    nivel = input("Nivel: ")
    area = input("Área funcional: ")
    ubicacion = input("Centro de trabajo: ")
    salario = input("Salario bruto anual (€): ")
    jornada = input("Jornada (completa/parcial): ")
    vacaciones = input("Vacaciones anuales (días): ")

    fecha_actual = datetime.today().strftime("%d de %B de %Y")

    texto = f"""
CONTRATO DE TRABAJO

En {domicilio_social}, a {fecha_actual}

REUNIDOS

De una parte, {representante}, en nombre y representación de la empresa {empresa}, con CIF {cif}, y domicilio social en {domicilio_social}.

Y de otra, D./Dña. {nombre_trabajador}, con DNI/NIE nº {dni}, y domicilio en {domicilio}.

Ambas partes, reconociéndose plena capacidad para contratar, acuerdan suscribir el presente contrato de trabajo con arreglo a las siguientes

CLÁUSULAS

Primera. Tipo de contrato: {tipo_contrato.upper()}
"""
    if tipo_contrato != "indefinido":
        texto += f"   Duración determinada: desde el {fecha_inicio} hasta el {fecha_fin}.\n"
    else:
        texto += f"   De duración indefinida, con inicio el {fecha_inicio}.\n"

    texto += f"""
Segunda. Puesto de trabajo: {puesto}
Grupo profesional: {grupo}, Nivel: {nivel}, Área funcional: {area}
Centro de trabajo: {ubicacion}

Tercera. Jornada: {jornada}
Retribución anual bruta: {salario} €
Vacaciones: {vacaciones} días naturales por año

Cuarta. Legislación aplicable: Este contrato se regirá por el Estatuto de los Trabajadores, el convenio colectivo aplicable y demás normativa vigente.

Quinta. Discapacidad: {"El trabajador posee discapacidad reconocida y se adoptarán las adaptaciones necesarias." if discapacidad.lower() == "sí" else "El trabajador no acredita discapacidad reconocida."}

Leído el presente contrato, lo firman ambas partes por duplicado en el lugar y fecha indicados.

Firmado:

_________________________           _________________________
{empresa}                              {nombre_trabajador}
(Representante)                       (Trabajador/a)
"""

    with open("contrato_laboral.txt", "w", encoding="utf-8") as f:
        f.write(texto)

    print("\nContrato generado como 'contrato_laboral.txt'.")

if __name__ == "__main__":
    generar_contrato()
