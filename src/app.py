import random

def generate_chapter_outline(chapter_number, central_idea):
    sections = [
        "Introducción",
        "Antecedentes teóricos",
        "Metodología",
        "Análisis",
        "Conclusiones"
    ]
    
    outline = f"Capítulo {chapter_number}: {central_idea}\n\n"
    
    for section in sections:
        outline += f"{section}:\n"
        for _ in range(3):  # Generate 3 subsections for each section
            subsection = f"- {random.choice(['Análisis', 'Discusión', 'Evaluación', 'Exploración'])} de {random.choice(['conceptos', 'teorías', 'métodos', 'resultados'])} relacionados con {central_idea}\n"
            outline += subsection
        outline += "\n"
    
    return outline

def main():
    print("Bienvenido al Generador de Esquemas de Tesis")
    
    thesis_title = input("Título de la tesis: ")
    thesis_statement = input("Enunciado de la tesis: ")
    print("Bibliografía (un autor por línea, presiona Enter dos veces para terminar):")
    bibliography = []
    while True:
        line = input()
        if line:
            bibliography.append(line)
        else:
            break
    bibliography = "\n".join(bibliography)
    
    chapters = {}
    current_chapter = 1
    
    while True:
        print(f"\nCapítulo {current_chapter}")
        central_idea = input(f"Idea central del capítulo {current_chapter}: ")
        
        print("Generando esquema del capítulo...")
        chapter_outline = generate_chapter_outline(current_chapter, central_idea)
        chapters[current_chapter] = chapter_outline
        print(f"Esquema del capítulo {current_chapter} generado con éxito!")
        
        print("\nEsquema del capítulo:")
        print(chapter_outline)
        
        next_chapter = input("\n¿Deseas generar otro capítulo? (s/n): ").lower()
        if next_chapter != 's':
            break
        
        current_chapter += 1
    
    print("\nResumen de esquemas de capítulos generados:")
    for chapter_num, outline in chapters.items():
        print(f"\nCapítulo {chapter_num}:")
        print(outline)

if __name__ == "__main__":
    main()