import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 900, 600
UI_HEIGHT = 80

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Paint UI")

# ---------- COLORS ----------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 50, 50)
GREEN = (50, 200, 70)
BLUE = (50, 120, 255)
GRAY = (200, 200, 200)
DARK = (80, 80, 80)

# ---------- STATE ----------
current_color = BLACK
tool = "pen"
drawing = False
start_pos = None
last_pos = None

brush_size = 6
eraser_size = 16

# Canvas surface
canvas = pygame.Surface((WIDTH, HEIGHT - UI_HEIGHT))
canvas.fill(WHITE)

font = pygame.font.SysFont("Verdana", 16)

# ---------- BUTTON ----------
class Button:
    def __init__(self, x, y, w, h, text, value):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.value = value

    def draw(self, surface, active=False):
        pygame.draw.rect(surface, DARK if active else GRAY, self.rect)
        label = font.render(self.text, True, WHITE if active else BLACK)
        surface.blit(label, (self.rect.x + 5, self.rect.y + 8))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# ---------- UI ----------
tool_buttons = [
    Button(10, 10, 80, 30, "Pen", "pen"),
    Button(100, 10, 80, 30, "Rect", "rect"),
    Button(190, 10, 80, 30, "Circle", "circle"),
    Button(280, 10, 80, 30, "Eraser", "eraser"),
    Button(370, 10, 80, 30, "Square", "square"),
    Button(460, 10, 100, 30, "RightTri", "rtri"),
    Button(570, 10, 120, 30, "EqTri", "etri"),
    Button(700, 10, 100, 30, "Rhombus", "rhombus"),
]

color_buttons = [
    Button(10, 45, 40, 25, "", RED),
    Button(60, 45, 40, 25, "", GREEN),
    Button(110, 45, 40, 25, "", BLUE),
    Button(160, 45, 40, 25, "", BLACK),
]

# ---------- SMOOTH DRAW ----------
def draw_smooth_line(surface, color, start, end, width):
    # Draw smooth line using small circles
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    dist = max(1, int(math.hypot(dx, dy)))

    for i in range(dist):
        x = int(start[0] + dx * i / dist)
        y = int(start[1] + dy * i / dist)
        pygame.draw.circle(surface, color, (x, y), width)

# ---------- PREVIEW ----------
def draw_preview(surface, tool, start_pos, end_pos, color):
    # Draw temporary preview (not saved to canvas)

    if tool == "rect":
        rect = pygame.Rect(start_pos,
            (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
        pygame.draw.rect(surface, color, rect, 2)

    elif tool == "circle":
        radius = int(math.hypot(end_pos[0]-start_pos[0],
                                end_pos[1]-start_pos[1]))
        pygame.draw.circle(surface, color, start_pos, radius, 2)

    elif tool == "square":
        size = min(abs(end_pos[0]-start_pos[0]),
                   abs(end_pos[1]-start_pos[1]))
        rect = pygame.Rect(start_pos, (size, size))
        pygame.draw.rect(surface, color, rect, 2)

    elif tool == "rtri":
        points = [
            start_pos,
            (end_pos[0], start_pos[1]),
            (start_pos[0], end_pos[1])
        ]
        pygame.draw.polygon(surface, color, points, 2)

    elif tool == "etri":
        side = abs(end_pos[0] - start_pos[0])
        height = int(side * math.sqrt(3) / 2)

        points = [
            (start_pos[0], start_pos[1]),
            (start_pos[0] + side, start_pos[1]),
            (start_pos[0] + side // 2, start_pos[1] - height)
        ]
        pygame.draw.polygon(surface, color, points, 2)

    elif tool == "rhombus":
        cx = (start_pos[0] + end_pos[0]) // 2
        cy = (start_pos[1] + end_pos[1]) // 2

        points = [
            (cx, start_pos[1]),
            (end_pos[0], cy),
            (cx, end_pos[1]),
            (start_pos[0], cy)
        ]
        pygame.draw.polygon(surface, color, points, 2)

# ---------- MAIN LOOP ----------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # ---------- MOUSE DOWN ----------
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # Select tool
            for btn in tool_buttons:
                if btn.is_clicked((x, y)):
                    tool = btn.value

            # Select color
            for btn in color_buttons:
                if btn.is_clicked((x, y)):
                    current_color = btn.value

            # Start drawing
            if y > UI_HEIGHT:
                drawing = True
                start_pos = (x, y - UI_HEIGHT)
                last_pos = start_pos

        # ---------- MOUSE UP ----------
        if event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                end_pos = (event.pos[0], event.pos[1] - UI_HEIGHT)

                if tool == "rect":
                    rect = pygame.Rect(start_pos,
                        (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                    pygame.draw.rect(canvas, current_color, rect, 2)

                elif tool == "circle":
                    radius = int(math.hypot(end_pos[0]-start_pos[0],
                                            end_pos[1]-start_pos[1]))
                    pygame.draw.circle(canvas, current_color, start_pos, radius, 2)

                elif tool == "square":
                    size = min(abs(end_pos[0]-start_pos[0]),
                               abs(end_pos[1]-start_pos[1]))
                    rect = pygame.Rect(start_pos, (size, size))
                    pygame.draw.rect(canvas, current_color, rect, 2)

                elif tool == "rtri":
                    points = [
                        start_pos,
                        (end_pos[0], start_pos[1]),
                        (start_pos[0], end_pos[1])
                    ]
                    pygame.draw.polygon(canvas, current_color, points, 2)

                elif tool == "etri":
                    side = abs(end_pos[0] - start_pos[0])
                    height = int(side * math.sqrt(3) / 2)

                    points = [
                        (start_pos[0], start_pos[1]),
                        (start_pos[0] + side, start_pos[1]),
                        (start_pos[0] + side // 2, start_pos[1] - height)
                    ]
                    pygame.draw.polygon(canvas, current_color, points, 2)

                elif tool == "rhombus":
                    cx = (start_pos[0] + end_pos[0]) // 2
                    cy = (start_pos[1] + end_pos[1]) // 2

                    points = [
                        (cx, start_pos[1]),
                        (end_pos[0], cy),
                        (cx, end_pos[1]),
                        (start_pos[0], cy)
                    ]
                    pygame.draw.polygon(canvas, current_color, points, 2)

            drawing = False

    # ---------- FREE DRAW ----------
    if drawing:
        mx, my = pygame.mouse.get_pos()
        my -= UI_HEIGHT

        if my >= 0:
            current_pos = (mx, my)

            if tool == "pen":
                draw_smooth_line(canvas, current_color, last_pos, current_pos, brush_size)

            elif tool == "eraser":
                draw_smooth_line(canvas, WHITE, last_pos, current_pos, eraser_size)

            last_pos = current_pos

    # ---------- RENDER ----------
    screen.fill(WHITE)

    # Draw canvas
    screen.blit(canvas, (0, UI_HEIGHT))

    # ---------- PREVIEW DRAW ----------
    if drawing and start_pos:
        mx, my = pygame.mouse.get_pos()
        if my > UI_HEIGHT:
            draw_preview(screen, tool, start_pos, (mx, my - UI_HEIGHT), current_color)

    # Draw UI background
    pygame.draw.rect(screen, (230, 230, 230), (0, 0, WIDTH, UI_HEIGHT))

    # Draw buttons
    for btn in tool_buttons:
        btn.draw(screen, tool == btn.value)

    for btn in color_buttons:
        pygame.draw.rect(screen, btn.value, btn.rect)

    pygame.display.update()