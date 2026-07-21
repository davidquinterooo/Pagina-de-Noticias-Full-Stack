<template>
  <aside class="d-flex flex-nowrap">
    <div
      class="d-flex flex-row align-items-stretch flex-shrink-0"
      style="width: 290px"
    >   
      <div class="list-group list-group-flush scrollarea">
          <div class="d-flex flex-column w-100 justify-content-start gap-2">

            <div class="video-container mt-3" 
            style="
            position: relative; 
            width: 100%; 
            height: 150px; 
            background: #000; 
            overflow: hidden;">
              <!-- Estado 1: Se muestra la portada forzada en Máxima Resolución (HD) -->
              <div v-if="!videoCargado" @click="videoCargado = true" 
              style="
              cursor: pointer; 
              width: 100%; 
              height: 100%;">
                <img 
                  src="\portadahd.jpg" 
                  alt="Portada HD" 
                  style="width: 100%; 
                  height: 100%; 
                  object-fit: cover;"
                />
                <!-- Botón de Play superpuesto -->
                <div style="
                position: absolute; 
                top: 50%; 
                left: 50%; 
                transform: translate(-50%, -50%); 
                width: 50px; 
                height: 50px; 
                background: rgba(0,0,0,0.7);  
                display: flex; 
                align-items: center; 
                justify-content: center; 
                color: white;"
                >
                  <BootstrapIcon class="icon-play" name="play-fill" />
                </div>
              </div>

              <!-- Estado 2: El iframe real solo se renderiza al hacer clic -->
              <iframe 
                v-else
                width="100%" 
                height="100%" 
                src="https://www.youtube.com/embed/bSkzWpcWz-o?si=6joufc2fn2QIy8-2" 
                title="Reproductor de video" 
                frameborder="0" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                allowfullscreen>
              </iframe>
            </div>

            <h2 class="mb-1 fs-2 links-sidebar fw-bold mt-4">Lo mas popular</h2>
            <a class="links-article fs-6 mt-3" href="#">
              Opcion 1: Advertencias previas y códigos secretos: canciller iraní desvela los entretelones de la guerra
            </a>
            <a class="links-article fs-6 mt-3" href="#">
              Opcion 2: ¿Por qué China, sin pisar el campo de juego, gana en el Mundial organizado por EE.UU.?
            </a>
            <a class="links-article fs-6 mt-3" href="#">
              Opcion 3: Infraestructura portuaria y buques en llamas: nuevos ataques rusos reducen la capacidad bélica de Ucrania
            </a>
            <a class="links-article fs-6 mt-3" href="#">
              Opcion 4: Infraestructura portuaria y buques en llamas: nuevos ataques rusos reducen la capacidad bélica de Ucrania
            </a>
            <a class="links-article fs-6 mt-3 mb-1" href="#">
              Opcion 5: Misiles iraníes en el cielo de Israel rumbo a Jordania (VIDEOS)
            </a>
          </div>
      </div>
    </div>
  </aside>
</template>

<script setup>
import { ref } from 'vue'
const videoCargado = ref(false)
</script>