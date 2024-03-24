<template>
  <Paragraph
    header="h1"
    emoji="👋"
    title="Hi, I'm Jens">
    <template v-slot:content>
      I'm a 19-year-old from Rotterdam, The Netherlands.
      I'm a very active person, always getting excited about new ideas.
      I'm pretty much the definition of a self-taught programmer,
      and I think it's very important to keep on learning and growing your skills every single day.
    </template>
  </Paragraph>

  <Paragraph
    header="h2"
    emoji="⚙️"
    title="Activities and goals">
    <template v-slot:content>
      I'm very active in Dutch coding communities regarding websites, Minecraft, hosting, and discord-related software.
      I love to help people with coding problems and brainstorming creative ideas and solutions.
      My future goal is to expand my teaching reach with workshops (which I am already working on) and educational/inspirational videos.
      Please also contact me for any questions or offers in this regard :)
    </template>
  </Paragraph>

  <Paragraph
    header="h2"
    emoji="✏️"
    title="Projects">
    <template v-slot:content>
      I've made a magnitude of projects of various levels of usefulness.
      These are some of my popular (free-to-use) projects:
      <ul>
        <li><a href="https://jens.skin/">Jens's Skin Generator</a></li>
        <li><a href="https://skin-render.jensderuiter.dev/">Skin Renderer</a></li>
        <li><a href="https://bingomc.net/">BingoMC</a></li>
        <li><a href="https://github.com/jensjeflensje/minecraft_imagery">Minecraft Imagery (ImageryAPI)</a></li>
        <li><a href="https://butwhe.re">Butwhe.re</a></li>
      </ul>
      These are some other projects I made:
      <ul>
        <li><a href="https://github.com/jensjeflensje/minecraft_hats">Minecraft Hats (propeller cap)</a></li>
        <li><a href="https://github.com/jensjeflensje/minecraft_typewriter">Minecraft Typewriter</a></li>
        <li><a href="https://github.com/jensjeflensje/minecraft_seed_finder">Minecraft Seed Finder</a></li>
        <li><a href="https://github.com/jensjeflensje/BalloonsByJens">BalloonsByJens</a></li>
        <li><a href="https://github.com/jensjeflensje/minecraft_subway">Minecraft Subway</a></li>
        <li><a href="https://github.com/jensjeflensje/minecraft_blockanimation">Minecraft Block Animation</a></li>
        <li><a href="https://github.com/jensjeflensje/backgroundx">BackgroundX</a></li>
        <li><a href="https://github.com/jensjeflensje/minecraft_sheepvideo">Minecraft Sheepvideo</a></li>
        <li><a href="https://github.com/jensjeflensje/marktplaats-py">marktplaats-py</a></li>
      </ul>
    </template>
  </Paragraph>

</template>

<script setup lang="ts">
import Paragraph from '@/components/Paragraph.vue'
</script>

<style scoped>
</style>
