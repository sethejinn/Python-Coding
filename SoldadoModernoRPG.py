import random
import time

class Soldado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.vida = 100
        self.ataque = 15
        self.defensa = 8
        self.morale = 100
        self.armas = {'Pistola': 10, 'Rifle de asalto': 20, 'Escopeta': 25}
        self.municion = {'Pistola': 30, 'Rifle de asalto': 20, 'Escopeta': 10}
        self.botiquines = 3
        self.estrategia = 'Estándar'
        self.ubicacion = 'Campamento Base'
        self.experiencia = 0
        self.camo = 'Estándar'
        self.habilidades = ['Disparo certero', 'Escudo temporal']
        self.mision = None
        self.suministros = {'agua': 10, 'comida': 5}
    
    def subir_nivel(self):
        self.nivel += 1
        self.vida += 30
        self.ataque += 10
        self.defensa += 5
        self.morale = 100
        self.experiencia = 0
        print(f'{self.nombre} ha subido al nivel {self.nivel}!')
    
    def recibir_dano(self, dano):
        dano_real = max(0, dano - self.defensa)
        self.vida -= dano_real
        self.morale -= 5
        print(f'{self.nombre} ha recibido {dano_real} de daño. Vida restante: {self.vida}')
    
    def usar_botiquin(self):
        if self.botiquines > 0:
            self.vida += 40
            self.botiquines -= 1
            print(f'{self.nombre} usó un botiquín. Vida actual: {self.vida}')
        else:
            print('No tienes botiquines disponibles.')
    
    def gestionar_suministros(self):
        if self.suministros['agua'] > 0 and self.suministros['comida'] > 0:
            self.suministros['agua'] -= 1
            self.suministros['comida'] -= 1
            self.morale += 20
            print(f'{self.nombre} ha consumido suministros. Moral actual: {self.morale}')
        else:
            print(f'{self.nombre} se está quedando sin suministros.')
    
    def obtener_arma(self, arma, dano):
        self.armas[arma] = dano
        print(f'Has obtenido un(a) {arma} con daño {dano}!')
    
    def cambiar_estrategia(self, nueva_estrategia):
        self.estrategia = nueva_estrategia
        print(f'{self.nombre} cambió su estrategia a {self.estrategia}')
    
    def cambiar_camo(self, nuevo_camo):
        self.camo = nuevo_camo
        print(f'{self.nombre} cambió su camuflaje a {self.camo}')
    
    def moverse(self, nueva_ubicacion):
        self.ubicacion = nueva_ubicacion
        print(f'{self.nombre} se ha movido a {self.ubicacion}')
    
    def llamar_apoyo_helicoptero(self):
        print(f'{self.nombre} llama un helicóptero para apoyo aéreo. ¡Aguanta!')
    
    def solicitar_artilleria(self):
        print(f'{self.nombre} solicita un ataque de artillería sobre las posiciones enemigas.')
    
    def recibir_refuerzos(self):
        print(f'{self.nombre} ha recibido refuerzos, soldados adicionales para ayudar en la batalla.')
    
    def lanzar_granada(self, granada, enemigo):
        granada.usar(enemigo)
    
    def usar_habilidad(self, habilidad, enemigo):
        if habilidad == 'Disparo certero':
            dano_extra = random.randint(10, 20)
            enemigo.recibir_dano(dano_extra)
            print(f'{self.nombre} usa Disparo certero. ¡{dano_extra} de daño adicional!')
        elif habilidad == 'Escudo temporal':
            self.defensa += 10
            print(f'{self.nombre} activa Escudo temporal. Defensa aumentada a {self.defensa}')
        else:
            print('Habilidad no disponible.')
    
    def aceptar_mision(self, mision):
        self.mision = mision
        print(f'{self.nombre} ha aceptado la misión: {mision.descripcion}')
    
    def completar_mision(self):
        if self.mision:
            print(f'{self.nombre} ha completado la misión: {self.mision.descripcion}')
            self.mision.recompensar(self)
            self.mision = None
        else:
            print('No tienes misión activa.')

class Mision:
    def __init__(self, descripcion, recompensa_arma=None, recompensa_experiencia=None):
        self.descripcion = descripcion
        self.recompensa_arma = recompensa_arma
        self.recompensa_experiencia = recompensa_experiencia
    
    def recompensar(self, soldado):
        if self.recompensa_arma:
            soldado.obtener_arma(self.recompensa_arma[0], self.recompensa_arma[1])
        if self.recompensa_experiencia:
            soldado.experiencia += self.recompensa_experiencia
        print(f'{soldado.nombre} ha recibido sus recompensas.')

class Enemigo:
    def __init__(self, nombre, vida, ataque, estrategia, tipo, armamento=None):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.estrategia = estrategia
        self.tipo = tipo
        self.armamento = armamento if armamento else {'Pistola': 12, 'Rifle de asalto': 18}
    
    def recibir_dano(self, dano):
        self.vida -= dano
        print(f'{self.nombre} ha recibido {dano} de daño. Vida restante: {self.vida}')
    
    def atacar(self, soldado):
        soldado.recibir_dano(self.ataque)
        print(f'{self.nombre} ataca a {soldado.nombre} con {self.ataque} de daño.')
    
    def cambiar_estrategia(self, nueva_estrategia):
        self.estrategia = nueva_estrategia
        print(f'{self.nombre} cambió su estrategia a {self.estrategia}')
    
    def equipar_arma(self, arma, dano):
        self.armamento[arma] = dano
        print(f'{self.nombre} ha equipado un(a) {arma} con daño {dano}!')

class Granadas:
    def __init__(self, tipo, dano):
        self.tipo = tipo
        self.dano = dano
    
    def usar(self, enemigo):
        enemigo.recibir_dano(self.dano)
        print(f'¡Granada {self.tipo} lanzada! Causa {self.dano} de daño.')

class Artilleria:
    def __init__(self):
        self.dano = 50
    
    def lanzar(self, enemigo):
        enemigo.recibir_dano(self.dano)
        print(f'¡Ataque de artillería lanzado! Causa {self.dano} de daño.')

class Vehiculo:
    def __init__(self, nombre, vida, ataque, tipo):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.tipo = tipo
    
    def recibir_dano(self, dano):
        self.vida -= dano
        print(f'{self.nombre} ha recibido {dano} de daño. Vida restante: {self.vida}')
    
    def atacar(self, enemigo):
        enemigo.recibir_dano(self.ataque)
        print(f'{self.nombre} ataca a {enemigo.nombre} con {self.ataque} de daño.')

class Clima:
    def __init__(self):
        self.condiciones = ['Soleado', 'Lluvia', 'Tormenta', 'Niebla']
    
    def afectar_combate(self):
        clima = random.choice(self.condiciones)
        if clima == 'Soleado':
            print('El clima es soleado. ¡Buen momento para atacar!')
        elif clima == 'Lluvia':
            print('La lluvia dificulta la puntería.')
        elif clima == 'Tormenta':
            print('La tormenta reduce la visibilidad y los daños son más impredecibles.')
        elif clima == 'Niebla':
            print('La niebla hace que sea más difícil localizar a los enemigos.')

def combate(soldado, enemigo, clima):
    print(f'¡Un {enemigo.nombre} ha aparecido!')
    while soldado.vida > 0 and enemigo.vida > 0:
        clima.afectar_combate()
        accion = input('¿Qué quieres hacer? (Atacar / Usar botiquín / Cambiar estrategia / Cambiar camuflaje / Llamar apoyo aéreo / Solicitar artillería / Recibir refuerzos / Lanzar granada / Usar habilidad / Gestionar suministros) ').lower()
        if accion == 'atacar':
            dano = random.randint(soldado.ataque - 5, soldado.ataque + 5)
            enemigo.recibir_dano(dano)
        elif accion == 'usar botiquín':
            soldado.usar_botiquin()
        elif accion == 'cambiar estrategia':
            estrategia = input('¿Nueva estrategia? (Ofensiva / Defensiva / Sigilosa) ').capitalize()
            soldado.cambiar_estrategia(estrategia)
        elif accion == 'cambiar camuflaje':
            camo = input('¿Nuevo camuflaje? (Selva / Desierto / Urbano) ').capitalize()
            soldado.cambiar_camo(camo)
        elif accion == 'llamar apoyo aéreo':
            soldado.llamar_apoyo_helicoptero()
        elif accion == 'solicitar artillería':
            artilleria = Artilleria()
            artilleria.lanzar(enemigo)
        elif accion == 'recibir refuerzos':
            soldado.recibir_refuerzos()
        elif accion == 'lanzar granada':
            tipo = input('¿Granada de tipo? (Fragmentación / Humo) ').capitalize()
            granada = Granadas(tipo, random.randint(20, 40))
            soldado.lanzar_granada(granada, enemigo)
        elif accion == 'usar habilidad':
            habilidad = input('¿Qué habilidad usar? (Disparo certero / Escudo temporal) ').capitalize()
            soldado.usar_habilidad(habilidad, enemigo)
        elif accion == 'gestionar suministros':
            soldado.gestionar_suministros()

        enemigo.atacar(soldado)
        time.sleep(1)
    
    if soldado.vida <= 0:
        print(f'{soldado.nombre} ha caído en combate...')
    else:
        print(f'{soldado.nombre} ha derrotado a {enemigo.nombre}!')

def juego():
    soldado = Soldado(input('Nombre del soldado: '))
    clima = Clima()
    enemigo = Enemigo('Soldado enemigo', 100, 15, 'Ofensivo', 'Tierra')
    
    combate(soldado, enemigo, clima)

if __name__ == '__main__':
    juego()
