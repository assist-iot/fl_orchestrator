<template>
  <div>
    <div class="app-container" :style="bgc">
      <el-tabs class="title-home-card" type="border-card" dark slider-color="green" centered color="green">
        <h1 class="title-home">{{ this.$t('home.title') }}</h1>
      </el-tabs>
      <div class="flex-container">
        <el-button plain class="btn-home" @click="redirect('overview')"><i class="el-icon-s-tools" /> {{ this.$t('home.newTraining') }}</el-button>
        <el-button plain class="btn-home" @click="redirect('models')"><i class="el-icon-check" /> {{ this.$t('home.viewAvailableModels') }}</el-button>
      </div>
      <Footer />
    </div>
  </div>
</template>

<script>
import Footer from '../footer/FooterComponent.vue'
export default {
  components: {
    Footer
  },
  data() {
    return {
      bgc: {
        backgroundColor: 'rgb(240,242,245)',
        height: '100%',
        width: '100%',
        overflow: 'scroll',
        position: 'absolute'
      },
      list: null
    }
  },
  methods: {
    redirect(type) {
      switch (type) {
        case 'overview':
          this.$router.push({ name: 'overview' })
          break
        case 'models':
          this.$router.push({ name: 'models' })
          break
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.title-home-card {
    margin-top: 20px;
    text-align: center;
    .title-home{
        font-weight: bold;
        color: #1E1D33;
    }
}
.flex-container {
    display: flex;
    justify-content: center;
/*     align-items: center; */
    flex-direction: row;
    margin-top: 20px;
    height: 70%;
}
.btn-home {
    background-color: #fff;
    border-radius: 0px !important;
    box-shadow: 2px 2px 9px -1px rgba(0,0,0,0.75);
    border-radius: 5px;
    border: none;
    padding: 10px;
    margin-top: 20px;
    width: 50%;
    height: 50%;
    font-size: 30px;
}
</style>
