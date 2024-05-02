<template>
  <div>
    <div class="app-container footer-container">
      <span class="footer-content">
        This project has received funding from European Union's Horizon 2020 research an innovation programme under grant agreement No 957258</span>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {}
  }
}
</script>

<style lang="scss" scoped>
.footer-container {
  background: white;
  border-top: 1px solid #dee2e6;
  position: fixed;
  bottom: 0;
  width: 100%;
  line-height: 5px;
  height: 20px;
  box-sizing: border-box;
}

.footer-content {
  line-height: 5px;
  vertical-align: middle;
  font-size: 12px;
}

/* .footer-container img {
   width: 100%;
} */

.footer-img {
  width: 40px;
  height: 40px;
  float: right;
}

.img-container {
  width: 100%;
}
</style>
