<script setup></script>

<PlaySquareTwoTone />

<template>
    <header>
      <p style="text-align: center">
        <img @click = 'openpage'
          alt="CameraPicture"
          class="Camera"
          scr="@/assets/camera.png"
          width="100"
          height="100"
          style="align: centre"
          />
        methods:{
            openpage(){

            }
        }
      </p>
    </header>
</template>

<style>
.Camera {
    position: relative;
    right: 80px;
    top: 30px;
}
</style>
