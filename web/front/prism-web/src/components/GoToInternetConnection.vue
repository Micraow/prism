<script setup>
</script>

<template>
  <header>
    <p style="text-align: center">
      <img @click='turnpage' alt="WiFiPicture" class="WiFi" src="@/assets/wifi_no_problem.png" width="50" height="50"
        style="position: relative;" />

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

<script>
export default {
  methods: {
    turnpage() {
      this.$router.push('/InternetConnection')
    }
  }
}
</script>