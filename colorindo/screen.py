import pygame

class Screen:
    width = 800
    height = 800
    origin_x = width // 2
    origin_y = height // 2

    @staticmethod
    def display(self, faces, colors, gap):
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Projeção Paralela com Pygame")
        clock = pygame.time.Clock()

        old_colors = pygame.time.get_ticks()
        colors_sequence = colors.copy()
        running = True
        while running:
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE)) or event.type == pygame.QUIT:
                    running = False

            screen.fill((0, 0, 0))

            # rotaciona as cores das faces
            new_colors = pygame.time.get_ticks()
            if (new_colors - old_colors > gap):
                first_color = colors_sequence.pop(0)
                colors_sequence.append(first_color)
                old_colors = new_colors

            # desenha as faces na tela
            for i in range(len(faces)):
                face = faces[i]
                color = colors_sequence[i]
                pygame.draw.polygon(screen, color, face, 0)

            # escreve o texto na tela
            font = pygame.font.Font(None, 36)
            timestamp = font.render(f"Tempo: {old_colors / 1000:.1f} s", True, (255, 255, 255))
            timestamp_rect = timestamp.get_rect(topleft=(50, 50))
            screen.blit(timestamp, timestamp_rect)

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()