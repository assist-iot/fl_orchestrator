<template>
  <div>
    <div class="app-container" :style="bgc">
      <el-tabs type="border-card" dark slider-color="green" centered color="green">
        <el-tab-pane :label="this.$t('overview.models')">
          <AlgorithmsList />

        </el-tab-pane>
      </el-tabs>
      <Footer />
    </div>
  </div>
</template>

<script>
import AlgorithmsList from './component/algorithmsList.vue'
import Footer from '../footer/FooterComponent.vue'
export default {
  components: {
    AlgorithmsList,
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
  }
}
</script>

<style lang="scss" scoped>
</style>
