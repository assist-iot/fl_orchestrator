<template>
  <div>
    <div v-if="!isFooter" class="sidebar-logo-container" :class="{'collapse':collapse}">
      <transition name="sidebarLogoFade">
        <router-link v-if="collapse" key="collapse" class="sidebar-logo-link" to="/dataports">
          <img v-if="logo" :src="logo" class="sidebar-logo">
          <h1 v-else class="sidebar-title" style="font-size: 20px">{{ title }} </h1>
        </router-link>
        <router-link v-else key="expand" class="sidebar-logo-link" to="/">
          <img v-if="logo" :src="logo" class="sidebar-logo">
          <h1 class="sidebar-title" style="font-size: 20px">{{ title }} </h1>
        </router-link>
      </transition>
    </div>

    <!--<div v-else class="sidebar-logo-container" :class="{'collapse':collapse}">
      <transition name="sidebarLogoFade">
        <router-link v-if="collapse" key="collapse" class="sidebar-logo-link" to="/prodevelop">
          <img v-if="logoProde" :src="logoProde" class="sidebar-logo">
          <h1 v-else class="sidebar-title" style="font-size: 20px">{{ titleProde }} </h1>
        </router-link>
        <router-link v-else key="expand" class="sidebar-logo-link" to="/prodevelop">
          <img v-if="logoProde" :src="logoProde" class="sidebar-logo">
          <h1 class="sidebar-title" style="font-size: 20px">{{ titleProde }} </h1>
        </router-link>
      </transition>
    </div> -->
  </div>
</template>

<script>
// import dplogo from '@/assets/dataports_images/dp_logo.png
import assist_logo from '../../../assets/dataports_images/assist_logo.png'
import prode from '@/assets/dataports_images/prodeLogo.png'

export default {
  name: 'SidebarLogo',
  props: {
    collapse: {
      type: Boolean,
      required: true
    },
    isFooter: {
      type: Boolean,
      required: false
    }
  },
  data() {
    return {
      title: 'ASSIST-IoT',
      titleProde: 'Prodevelop',
      logo: assist_logo,
      logoProde: prode
    }
  }
}
</script>

<style lang="scss" scoped>
.sidebarLogoFade-enter-active {
  transition: opacity 1.5s;
}

.sidebarLogoFade-enter,
.sidebarLogoFade-leave-to {
  opacity: 0;
}

.sidebar-logo-container {
  position: relative;
  width: 100%;
  height: 50px;
  line-height: 50px;
  background: #2b2f3a;
  text-align: center;
  overflow: hidden;
  border-bottom: 2px solid #7EB89C;

  & .sidebar-logo-link {
    height: 100%;
    width: 100%;

    & .sidebar-logo {
      width: 32px;
      height: 32px;
      vertical-align: middle;
      margin-right: 12px;
    }

    & .sidebar-title {
      display: inline-block;
      margin: 0;
      color: #fff;
      font-weight: 600;
      line-height: 50px;
      font-size: 14px;
      font-family: Avenir, Helvetica Neue, Arial, Helvetica, sans-serif;
      vertical-align: middle;
    }
  }

  &.collapse {
    .sidebar-logo {
      margin-right: 0px;
    }
  }
}
</style>
