

auditivo=0
visual=0
cinestesico=0

print(
 """
+================================================+
| INSTRUCCIONES: Elige una opción con la que más |
| te identifiques de cada una de las preguntas,  | 
| marca la letra que corresponde.                |
+================================================+
""")

print("""

█████████
█▄█████▄█
█▼▼▼▼▼
█
█▲▲▲▲▲
█████████
██ ██

""")

print("""

 ───────▄▄▄▄▄▄▄▄───────
 ───────▄▄▄▄▄▄▄▄───────
 ─────▄▄▄▄▄▄▄▄▄▄▄▄───────
 ─────▄▄▄▄▄▄▄▄▄▄▄▄───────
 ────▄▄▄▄▄▄▄▄▄▄▄▄▄▄───────
 ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ jd
 ─────█─▄──────▄─█──
 ─────█─▄▀█──█▀▄─█──
 ────▐▌──────────▐▌──
 ────█▌▀▄──▄▄──▄▀▐█──
 ───▐██──▀▀──▀▀──██▌──
 ──▄████▄──▐▌──▄████▄─
 ─▄████▄█──▐▌──█▄████▄─
  ..........▄▄▄▄........   
                          
""")

nombre=input("Escribe tu nombre por favor: ")
print("\nEmpecemos con una frase, te parece !!",nombre, "¡¡ Recuerda que\n eres tan importante y tan sabio, como las metas que fijes,\n solo tu eres dueño de tu destino y tu futuro. \n\n\n Recuerda las instrucciones de arriba...\n\n \n Empecemos:  ")
print("           ")
print(nombre, """ \n
1. ¿Cuál de las siguientes actividades disfrutas más?
a) Escuchar música
b) Ver películas
c) Bailar con buena música
""")

resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        auditivo+=1
        break
    elif resp == "B":
        visual+=1
        break
    elif resp == "C":
        cinestesico+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    

print("           ")
print("siguiente pregunta:")
print(nombre, """ \n
2. ¿Qué programa de televisión prefieres?
a) Reportajes de descubrimientos y lugares
b) Cómico y de entretenimiento
c) Noticias del mundo
""")

resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        visual+=1
        break
    elif resp == "B":
        cinestesico+=1
        break
    elif resp == "C":
        auditivo+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta  :")
    

print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
3. Cuando conversas con otra persona, tú:
a) La escuchas atentamente
b) La observas 
c) Tiendes a tocarla
""")

resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        auditivo+=1
        break
    elif resp == "B":
        visual+=1
        break
    elif resp == "C":
        cinestesico+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    

print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
4. Si pudieras adquirir uno de los siguientes artículos, ¿cuál 
elegirías?
a) Un jacuzzi
b) Un estereo
c) Un televisor
""")

resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        cinestesico+=1
        break
    elif resp == "B":
        auditivo+=1
        break
    elif resp == "C":
        visual+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    

print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
5. ¿Qué prefieres hacer un sábado por la tarde?
a) Quedarte en casa
b) Ir a un concierto
c) ir al cine
""")
resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        cinestesico+=1
        break
    elif resp == "B":
        auditivo+=1
        break
    elif resp == "C":
        visual+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
6. ¿Qué tipo de exámenes se te facilitan más?
a) Examen oral
b) Examen escrito
c) Examen de opcion multiple
""")
resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        auditivo+=1
        break
    elif resp == "B":
        visual+=1
        break
    elif resp == "C":
        cinestesico+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
7. ¿Cómo te orientas más fácilmente?
a) Mediante el uso de un mapa
b) Pidiendo indicaciones
c) A través de la intuición
""")
resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        visual+=1
        break
    elif resp == "B":
        auditivo+=1
        break
    elif resp == "C":
        cinestesico+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
8. ¿En qué prefieres ocupar tu tiempo en un lugar de descanso?
a) Pensar
b) Caminar por los alrededores
c) Descansar
""")
resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        auditivo+=1
        break
    elif resp == "B":
        visual+=1
        break
    elif resp == "C":
        cinestesico+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
9. ¿Qué te halaga más?
a) Que te digan que tienes buen aspecto
b) Que te digan que tienes un trato muy agradable
c) Que te digan que tienes una conversación interesante
""")
resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        visual+=1
        break
    elif resp == "B":
        cinestesico+=1
        break
    elif resp == "C":
        auditivo+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
10. ¿Cuál de estos ambientes te atrae más?
a) Uno en el que se sienta un clima agradable
b) Uno en el que se escuchen las olas del mar
c) Uno con una hermosa vista al océano

""")
resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        cinestesico+=1
        break
    elif resp == "B":
        auditivo+=1
        break
    elif resp == "C":
        visual+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
11. ¿De qué manera se te facilita aprender algo?
a) Repitiendo en voz alta
b) Escribiéndolo varias veces
c) Relacionándolo con algo divertido
""")
resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        auditivo+=1
        break
    elif resp == "B":
        visual+=1
        break
    elif resp == "C":
        cinestesico+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
12. ¿A qué evento preferirías asistir?
a) A una reunión social
b) A una exposición de arte
c) A una conferencia
""")
resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        cinestesico+=1
        break
    elif resp == "B":
        visual+=1
        break
    elif resp == "C":
        auditivo+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
13. ¿De qué manera te formas una opinión de otras personas?
a) Por la sinceridad en su voz
b) Por la forma de estrecharte la mano
c) Por su aspecto
""")
resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        auditivo+=1
        break
    elif resp == "B":
        cinestesico+=1
        break
    elif resp == "C":
        visual+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
14. ¿Cómo te consideras?
a) Atlético
b) Intelectual
c) Sociable
""")
resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        visual+=1
        break
    elif resp == "B":
        auditivo+=1
        break
    elif resp == "C":
        cinestesico+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
15. ¿Qué tipo de películas te gustan más?
a) Clásicas
b) De acción
c) De amor
""")
resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        auditivo+=1
        break
    elif resp == "B":
        visual+=1
        break
    elif resp == "C":
        cinestesico+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
16. ¿Cómo prefieres mantenerte en contacto con otra persona?
a) por correo electrónico
b) Tomando un café juntos
c) Por teléfono
""")
resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        visual+=1
        break
    elif resp == "B":
        cinestesico+=1
        break
    elif resp == "C":
        auditivo+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
17. ¿Cuál de las siguientes frases se identifican más contigo?
a) Me gusta que mi coche se sienta bien al conducirlo
b) Percibo hasta el mas ligero ruido que hace mi coche
c) Es importante que mi coche esté limpio por fuera y por dentro
""")
resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        cinestesico+=1
        break
    elif resp == "B":
        auditivo+=1
        break
    elif resp == "C":
        visual+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
18. ¿Cómo prefieres pasar el tiempo con tu novia o novio?
a) Conversando
b) Acariciándose
c) Mirando algo juntos
""")
resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        auditivo+=1
        break
    elif resp == "B":
        cinestesico+=1
        break
    elif resp == "C":
        visual+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")


print(nombre, """ \n
19. Si no encuentras las llaves en una bolsa
a) La buscas mirando
b) Sacudes la bolsa para oír el ruido
c) Buscas al tacto
""")
resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        visual+=1
        break
    elif resp == "B":
        auditivo+=1
        break
    elif resp == "C":
        cinestesico+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
20. Cuando tratas de recordar algo, ¿cómo lo haces?
a) A través de imágenes
b) A través de emociones
c) A través de sonidos
""")
resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        visual+=1
        break
    elif resp == "B":
        cinestesico+=1
        break
    elif resp == "C":
        auditivo+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
21. Si tuvieras dinero, ¿qué harías?
a) Comprar una casa
b) Viajar y conocer el mundo
c) Adquirir un estudio de grabación
""")
resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        cinestesico+=1
        break
    elif resp == "B":
        visual+=1
        break
    elif resp == "C":
        auditivo+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
22. ¿Con qué frase te identificas más?
a) Reconozco a las personas por su voz
b) No recuerdo el aspecto de la gente
c) Recuerdo el aspecto de alguien, pero no su nombre
""")
resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        auditivo+=1
        break
    elif resp == "B":
        cinestesico+=1
        break
    elif resp == "C":
        visual+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
23. Si tuvieras que quedarte en una isla desierta, ¿qué preferirías llevar contigo?
a) Algunos buenos libros
b) Un radio portátil de alta frecuencia
c) Golosinas y comida enlatada
""")
resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        visual+=1
        break
    elif resp == "B":
        auditivo+=1
        break
    elif resp == "C":
        cinestesico+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
24. ¿Cuál de los siguientes entretenimientos prefieres?
a) Tocar un instrumento musical
b) Sacar fotografías
c) Actividades manuales
""")
resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        auditivo+=1
        break
    elif resp == "B":
        visual+=1
        break
    elif resp == "C":
        cinestesico+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
25. ¿Cómo es tu forma de vestir?
a) Impecable
b) Informal
c) Muy informal
""")
resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        visual+=1
        break
    elif resp == "B":
        auditivo+=1
        break
    elif resp == "C":
        cinestesico+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
26. ¿Qué es lo que más te gusta de una fogata nocturna?
a) El calor del fuego y los bombones asados
b) El sonido del fuego quemando la leña
c) Mirar el fuego y las estrellas
""")
resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        cinestesico+=1
        break
    elif resp == "B":
        auditivo+=1
        break
    elif resp == "C":
        visual+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
27. ¿Cómo se te facilita entender algo?
a) Cuando te lo explican verbalmente
b) Cuando utilizan medios visuales
c) Cuando se realiza a través de alguna actividad
""")
resp=input("ingresa tu respuesta:  ")
while resp!="      ":
    resp=resp.upper()
    if resp == "A":
        auditivo+=1
        break
    elif resp == "B":
        visual+=1
        break
    elif resp == "C":
        cinestesico+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
28. ¿Por qué te distingues?
a) Por tener una gran intuición
b) Por ser un buen conversador
c) Por ser un buen observador
""")
resp=input("ingresa tu respuesta:  ")
while resp!="      ":
    resp=resp.upper()
    if resp == "A":
        cinestesico+=1
        break
    elif resp == "B":
        auditivo+=1
        break
    elif resp == "C":
        visual+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
29. ¿Qué es lo que más disfrutas de un amanecer?
a) La emoción de vivir un nuevo día
b) Las tonalidades del cielo
c) El canto de las aves
""")
resp=input("ingresa tu respuesta:  ")
while resp!="      ":
    resp=resp.upper()
    if resp == "A":
        cinestesico+=1
        break
    elif resp == "B":
        visual+=1
        break
    elif resp == "C":
        auditivo+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
30. Si pudieras elegir ¿qué preferirías ser?
a) Un gran médico
b) Un gran músico
c) Un gran pintor
""")
resp=input("ingresa tu respuesta:  ")
while resp!="      ":
    resp=resp.upper()
    if resp == "A":
        cinestesico+=1
        break
    elif resp == "B":
        auditivo+=1
        break
    elif resp == "C":
        visual+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
31. Cuando eliges tu ropa, ¿qué es lo más importante para ti?
a) Que sea adecuada
b) Que luzca bien
c) Que sea cómoda
""")
resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        auditivo+=1
        break
    elif resp == "B":
        visual+=1
        break
    elif resp == "C":
        cinestesico+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
32. ¿Qué es lo que más disfrutas de una habitación?
a) Que sea silenciosa
b) Que sea confortable
c) Que esté limpia y ordenada
""")
resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        auditivo+=1
        break
    elif resp == "B":
        cinestesico+=1
        break
    elif resp == "C":
        visual+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")


print(nombre, """ \n
33. ¿Qué es más sexy para ti?
a) Una iluminación tenue
b) El perfume
c) Cierto tipo de música
""")
resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        visual+=1
        break
    elif resp == "B":
        cinestesico+=1
        break
    elif resp == "C":
        auditivo+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
34. ¿A qué tipo de espectáculo preferirías asistir?
a) A un concierto de música
b) A un espectáculo de magia
c) A una muestra gastronómica
""")
resp=input("ingresa tu respuesta:  ")
while resp!="      ":
    resp=resp.upper()
    if resp == "A":
        auditivo+=1
        break
    elif resp == "B":
        visual+=1
        break
    elif resp == "C":
        cinestesico+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
35. ¿Qué te atrae más de una persona?
a) Su trato y forma de ser
b) Su aspecto físico
c) Su conversación
""")
resp=input("ingresa tu respuesta:  ")
while resp!="      ":
    resp=resp.upper()
    if resp == "A":
        cinestesico+=1
        break
    elif resp == "B":
        visual+=1
        break
    elif resp == "C":
        auditivo+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
36. Cuando vas de compras, ¿en dónde pasas mucho tiempo?
a) En una librería
b) En una perfumería
c) En una tienda de discos
""")
resp=input("ingresa tu respuesta:  ")
while resp!="      ":
    resp=resp.upper()
    if resp == "A":
        visual+=1
        break
    elif resp == "B":
        cinestesico+=1
        break
    elif resp == "C":
        auditivo+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
37. ¿Cuál es tu idea de una noche romántica?
a) A la luz de las velas
b) Con música romántica
c) Bailando tranquilamente
""")
resp=input("ingresa tu respuesta:  ")
while resp!="       ":
    resp=resp.upper()
    if resp == "A":
        visual+=1
        break
    elif resp == "B":
        auditivo+=1
        break
    elif resp == "C":
        cinestesico+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
38. ¿Qué es lo que más disfrutas de viajar?
a) ñConocer personas y hacer nuevos amigos
b) Conocer lugares nuevos
c) Aprender sobre otras costumbres
""")
resp=input("ingresa tu respuesta:  ")
while resp!="      ":
    resp=resp.upper()
    if resp == "A":
        cinestesico+=1
        break
    elif resp == "B":
        visual+=1
        break
    elif resp == "C":
        auditivo+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
39. Cuando estás en la ciudad, ¿qué es lo que más hechas de menos del campo?
a) El aire limpio y refrescante
b) Los paisajes
c) La tranquilidad
""")
resp=input("ingresa tu respuesta:  ")
while resp!="     ":
    resp=resp.upper()
    if resp == "A":
        cinestesico+=1
        break
    elif resp == "B":
        visual+=1
        break
    elif resp == "C":
        auditivo+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
print("           ")
print("siguiente pregunta:")

print(nombre, """ \n
40. Si te ofrecieran uno de los siguientes empleos, ¿cuál elegirías?
a) Director de una estación de radio
b) Director de un club deportivo
c) Director de una revista
""")
resp=input("ingresa tu respuesta:  ")
while resp!="      ":
    resp=resp.upper()
    if resp == "A":
        auditivo+=1
        break
    elif resp == "B":
        cinestesico+=1
        break
    elif resp == "C":
        visual+=1
        break
    print("Respuesta equivocada, recuerda A,B o C")
    resp=input("ingresa tu respuesta:  ")
    
    
print("           ")
print("Has finalizado satisfactoriamente tu Test de estilo de aprendizaje")
print("           ")
print("           ")
print("Visual:  ",visual,"     ",2.5 *visual,"%   De estilo de aprendizaje visual.")
print("Auditivo:  ",auditivo,"     ",2.5 *auditivo,"%   De estilo de aprendizaje auditivo.")
print("Cinestesico:  ",cinestesico,"     ",2.5 *cinestesico,"%   De estilo de aprendizaje cinestesico.")

print("""
 ─────▄▄▄▄▄▄▄▄▄▄▄▄───────
 ─────▄▄▄▄▄▄▄▄▄▄▄▄───────
 ────▄▄▄▄▄▄▄▄▄▄▄▄▄▄───────
 ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
 ─────█─▄──────▄─█──
 ─────█─▄▀█──█▀▄─█──
 ────▐▌──────────▐▌──
 ────█▌▀▄──▄▄──▄▀▐█──
 ───▐██──▀▀──▀▀──██▌──
 ──▄████▄──▐▌──▄████▄─

""")

print("""

Referencia: De la Parra Paz, Eric, Herencia de vida para tus hijos. 
Crecimiento integral con técnicas PNL, Ed. Grijalbo.
México, 2004, págs. 88-95 1 00 DGB/DCA/12-2004

A codigo por Jhojan Adarme, Mind Health #Psicomorfosis
jhojan.adarme@seresmindhealth.com

""") 