import pygame
import sys
import random
import time

# --- Inicialización de Pygame ---
pygame.init()

# --- Configuración de la Pantalla ---
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_title("Scorpion Tracker (ALPHA ACCESS: GRANTED)")

# --- Colores "Hacker" ---
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 100, 0) # Para el fondo del texto

# --- Configuración de Fuente y Texto ---
# Usamos la fuente monoespaciada predeterminada para el efecto de terminal
font = pygame.font.Font(pygame.font.get_default_font(), 18)
header_font = pygame.font.Font(pygame.font.get_default_font(), 24)
scorp_font = pygame.font.Font(pygame.font.get_default_font(), 30) # Símbolo de escorpión más grande

# --- Configuración del "Escorpión" (el símbolo que sigue al mouse) ---
scorp_symbol = "^" # Símbolo simple para el escorpión
scorp_pos = [WIDTH // 2, HEIGHT // 2] # Empieza en el centro
scorp_speed = 4 # Velocidad constante de movimiento (píxeles por frame)

# --- Configuración del Texto de la Terminal (para el efecto de fondo) ---
terminal_lines = [
    "[!] ACCESS: GRANTED",
    "[+] INITIATING SCORPION TRACKING PROTOCOL",
    "[+] SYSTEM_ROOT_ACCESS: ACTIVE",
    "[+] MONITORING PERIPHERAL_BUS/MOUSE_INTERFACE",
    "[+] DEPLOYING KERNEL_MODULE: SCORPION_FOLLOW_v1.0",
    "[+] TARGETING MOUSE_CURSOR",
    "",
    "[...] BUSY: PROCESSING D_BUS EVENTS",
    "",
]
line_height = 20
max_lines = 20
scroll_speed = 0.4 # Segundos entre nuevas líneas de registro
last_scroll_time = time.time()

# --- Bucle Principal del Juego ---
running = True
clock = pygame.time.Clock() # Para limitar los FPS

while running:
    # 1. Manejo de Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Actualización de Lógica

    # A. Simulación de Registro de Terminal (desplazamiento de texto de fondo)
    if time.time() - last_scroll_time > scroll_speed:
        new_line = f"[LOG {time.strftime('%H:%M:%S')}] {random.choice(['D_BUS_EVENT', 'SYS_CALL', 'MODULE_UPDATE: OK', 'PACKET_SENT', 'PACKET_RECEIVED', 'I/O_EVENT'])}: {hex(random.randint(0, 0xFFFFFFFF))}"
        terminal_lines.append(new_line)
        if len(terminal_lines) > max_lines:
            terminal_lines.pop(0) # Eliminar la línea más antigua
        last_scroll_time = time.time()

    # B. Lógica de Seguimiento del Escorpión
    mouse_pos = pygame.mouse.get_pos() # Obtener posición del mouse

    # Calcular la dirección y distancia hacia el mouse
    dx = mouse_pos[0] - scorp_pos[0]
    dy = mouse_pos[1] - scorp_pos[1]
    dist = (dx**2 + dy**2)**0.5 # Teorema de Pitágoras para la distancia

    # Mover el escorpión hacia el mouse si está lo suficientemente lejos
    if dist > scorp_speed:
        # Normalizar el vector de dirección (para mantener velocidad constante)
        dx /= dist
        dy /= dist
        # Mover el escorpión a velocidad constante
        scorp_pos[0] += dx * scorp_speed
        scorp_pos[1] += dy * scorp_speed
    else:
        # Snap a la posición del mouse si está muy cerca (para evitar parpadeo)
        scorp_pos[0] = mouse_pos[0]
        scorp_pos[1] = mouse_pos[1]

    # 3. Dibujado en Pantalla

    # Limpiar la pantalla (fondo negro)
    screen.fill(BLACK)

    # A. Dibujar Texto de Terminal de Fondo
    y_offset = 20
    for line in terminal_lines:
        text_surface = font.render(line, True, DARK_GREEN)
        screen.blit(text_surface, (20, y_offset))
        y_offset += line_height

    # B. Dibujar Mensaje de "ACESS GRANTED" (como en la imagen)
    header_text = header_font.render("SYSTEM ACCESS: GRANTED", True, GREEN)
    screen.blit(header_text, (WIDTH - 300, 20))

    # C. Dibujar el "Escorpión" Digital
    # Usamos un símbolo simple como '^' que sigue al mouse
    scorp_surface = scorp_font.render(scorp_symbol, True, GREEN)
    # Centrar el texto en su posición actual
    scorp_rect = scorp_surface.get_rect(center=(int(scorp_pos[0]), int(scorp_pos[1])))
    screen.blit(scorp_surface, scorp_rect)

    # 4. Actualizar la Pantalla y Limitar FPS
    pygame.display.flip() # Actualizar el frame completo
    clock.tick(60) # Limitar a 60 frames por segundo

# --- Salida Limpia ---
pygame.quit()
sys.exit()