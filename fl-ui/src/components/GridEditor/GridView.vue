<template>
  <div>
    <div style="text-align: center;">
      <div class="site-title"> Dashboard</div>
      <span v-if="!preview">
        <el-button size="small" type="info" @click="addTitleGridItem">
          {{ $t('dashboard.title') }}
        </el-button>
        <el-button size="small" type="info" @click="addContentGridItem">
          {{ $t('dashboard.text') }}
        </el-button>
        <el-button size="small" type="info" @click="addImageGridItem">
          {{ $t('dashboard.image') }}
        </el-button>
        <el-button size="small" type="info" @click="addVisualizationGridItem">
          {{ $t('dashboard.visualization') }}
        </el-button>
        <el-button size="small" type="info" @click="addIframeWidgetItem">
          {{ $t('dashboard.Iframe') }}
        </el-button>
        <el-button size="small" type="info" @click="clearLayout">
          {{ $t('dashboard.clearLayout') }}
        </el-button>
        <!--<button class="btn btn-outline-primary" @click="addTitleGridItem"> H1 </button>
        <button class="btn btn-outline-primary" @click="addContentGridItem"> Content </button>
        <button class="btn btn-outline-primary" @click="addImageGridItem"> Image </button>-->
      </span>
      <el-button size="small" type="info" @click="disableGrid">
        <span v-if="preview">{{ $t('dashboard.edit') }}</span>
        <span v-else="preview">{{ $t('dashboard.preview') }}</span>
      </el-button>
      <el-button v-if="!preview" size="small" type="info" @click="saveLayout">
        <span>{{ $t('dashboard.save') }}</span>
      </el-button>
      <el-button v-if="!preview & storedLayout !== null" size="small" type="info" @click="load">
        <!--<el-button v-if="preview & storedLayout !== null" size="small" type="info" @click="load">-->
        <span>{{ $t('dashboard.load') }}</span>
      </el-button>
      <!--<button class="btn btn-outline-primary" @click="disableGrid">
        <span v-if="preview"> Edit </span>
        <span v-else="preview"> Preview </span>
      </button>-->
    </div>
    <hr>
    <grid-layout
      ref="grid"
      :layout="getResources"
      :col-num="12"
      :row-height="30"
      :is-draggable="isDraggable"
      :is-resizable="isResizable"
      :is-mirrored="false"
      :vertical-compact="true"
      :margin="[10, 10]"
      :use-css-transforms="true"
      @layout-created="layoutCreatedEvent"
      @layout-before-mount="layoutBeforeMountEvent"
      @layout-mounted="layoutMountedEvent"
      @layout-ready="layoutReadyEvent"
      @layout-updated="layoutUpdatedEvent"
    >
      <grid-item
        v-for="(item, index) in getResources"
        :key="index"
        :class="{ 'editMode' : !preview }"
        :auto-size="true"
        :x="item.x"
        :y="item.y"
        :w="item.w"
        :h="item.h"
        :i="item.i"
        @resize="resizeEvent"
        @move="moveEvent"
        @resized="resizedEvent"
        @container-resized="containerResizedEvent"
        @moved="movedEvent"
      >
        <div v-if="!preview" style="position: absolute; bottom: 0px; left: 4px;" @click="removeItem({key: index})">
          <el-tooltip class="item" effect="dark" :content="$t('dashboard.delete')" placement="top-start">
            <i class="el-icon-delete" />
          </el-tooltip>
          <!--<i class="fa fa-trash" aria-hidden="true" />-->
        </div>
        <text-widget
          v-if="item.type == 'title'"
          :preview="preview"
          :contenteditable="contenteditable"
          :item="item"
          :item-index="index"
        />

        <text-area-widget
          v-if="item.type == 'content'"
          :preview="preview"
          :contenteditable="contenteditable"
          :item="item"
          :item-index="index"
        />

        <image-widget
          v-if="item.type == 'image'"
          :preview="preview"
          :contenteditable="contenteditable"
          :item="item"
          :item-index="index"
        />

        <visualization-widget
          v-if="item.type == 'visualization'"
          :preview="preview"
          :contenteditable="contenteditable"
          :item="item"
          :item-index="index"
        />

        <iframe-widget
          v-if="item.type == 'iframe'"
          :preview="preview"
          :contenteditable="contenteditable"
          :item="item"
          :item-index="index"
        />
      </grid-item>
    </grid-layout>
  </div>
</template>
<script>
import { mapGetters, mapActions } from 'vuex'
import TextWidget from './TextWidget'
import TextAreaWidget from './TextAreaWidget'
import ImageWidget from './ImageWidget'
import VisualizationWidget from './VisualizationWidget'
import IframeWidget from './IframeWidget'
import { GridLayout, GridItem } from 'vue-grid-layout'
export default {
  name: 'Gridview',
  components: { GridLayout, GridItem, TextWidget, TextAreaWidget, ImageWidget, VisualizationWidget, IframeWidget },
  data() {
    return {
      isDraggable: false,
      isResizable: false,
      preview: true,
      contenteditable: false,
      storedLayout: null
    }
  },
  computed: {
    ...mapGetters([
      'getResources'
    ])
  },
  methods: {
    ...mapActions([
      'addTitleGridItem',
      'addContentGridItem',
      'addImageGridItem',
      'addVisualizationGridItem',
      'addIframeWidgetItem',
      'removeItem'
    ]),
    disableGrid() {
      this.isDraggable = !this.isDraggable
      this.isResizable = !this.isResizable
      this.preview = !this.preview
      this.contenteditable = !this.contenteditable
    },
    layoutCreatedEvent(newLayout) {
      console.log('Created layout: ', newLayout)
    },
    layoutBeforeMountEvent(newLayout) {
      console.log('beforeMount layout: ', newLayout)
    },
    layoutMountedEvent(newLayout) {
      console.log('Mounted layout: ', newLayout)
    },
    layoutReadyEvent(newLayout) {
      console.log('Ready layout: ', newLayout)
    },
    layoutUpdatedEvent(newLayout) {
      console.log('Updated layout: ', newLayout)
    },
    moveEvent(i, newX, newY) {
      console.log('MOVE i=' + i + ', X=' + newX + ', Y=' + newY)
    },
    resizeEvent(i, newH, newW, newHPx, newWPx) {
      console.log('RESIZE i=' + i + ', H=' + newH + ', W=' + newW + ', H(px)=' + newHPx + ', W(px)=' + newWPx)
    },
    movedEvent(i, newX, newY) {
      console.log('MOVED i=' + i + ', X=' + newX + ', Y=' + newY)
    },
    containerResizedEvent() {

    },
    resizedEvent() {

    },
    load() {
      /* console.log('Load layout')
      console.log(this.storedLayout)
      console.log(JSON.parse(this.storedLayout)) */
      this.$store.commit('setResources', JSON.parse(this.storedLayout))
    },
    saveLayout() {
      var saveLayout = this.$refs.grid.layout
      this.storedLayout = saveLayout
      this.storedLayout = JSON.stringify(saveLayout)
      console.log(this.storedLayout)
    },
    clearLayout() {
      this.$store.commit('setResources', [])
    }
  }
}
</script>
<style>
.editMode {
  background-color: #fafafa;
  border-radius: 5px;
}
.site-title {
  font-family: 'Lilita One', cursive;
  font-size: 50px;
  /* color: #F48FB1; */
  text-align: center;
}
.heading1 {
  font-family: 'Cambria', cursive;
  font-size: 30px;
  border: 0;
  border-bottom: 1px solid #8c8c8c;
  /* font-family: 'Crushed', cursive;
  font-size: 35px;
  border: none;
  color: #2196F3; */
}
.heading2 {
  font-family: 'Cambria';
  font-weight: bold;
  font-size: 20px;
  padding: 10px 5px;
  /* font-family: 'Patrick Hand', cursive;
  font-size: 20px;
  border: none;
  color: #3096f3;
  background-color: #FFF9C4;
  width: 100%;
  padding: 10px 5px; */
}
.heading3 {
  font-family: 'Cambria';
  font-style: italic;
  font-size: 16px;
  padding: 0 7px;
  /* font-family: 'Homemade Apple', cursive;
  font-size: 20px;
  border: none;
  color: #66d2b3;
  padding: 0 7px; */
}
.content {
  font-family: 'Times New Roman';
  font-size: 16px;
  /* color: #2196F3; */
}
i:hover {
  cursor:pointer;
}
</style>
