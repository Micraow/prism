<script setup></script>
<template>
    <header>
      <p style="text-align: center">
        <img @click = 'turnpage'
          alt="WiFiPicture"
          class="WiFi"
          scr="@/assets/wifi_no_problem.png"
          width="50"
          height="50"
          style="position: relative;"
          />
        methods:{
            turnpage(){
                this.$router.push('/InternetConnection')
            }
        }
      </p>
    </header>
</template>

<style>
.WiFi {
    position: relative;
    right: 80px;
    top: 30px;
}
</style>
