<template>
  <div :style="getStyle">
    <div v-if="!preview" class="preview" @click="editImage = !editImage">
      <el-tooltip v-if="!editImage" class="item" effect="dark" :content="$t('dashboard.editURL')" placement="top-start">
        <i class="el-icon-edit" />
      </el-tooltip>
      <i v-else="!editImage" class="el-icon-close" />
      <!--<i v-if="!editImage" class="fa fa-pencil" aria-hidden="true" />-->

      <!--<i v-else="!editImage" class="fa fa-times" aria-hidden="true" />-->
    </div>
    <iframe v-if="editImage" :src="item.location" />
    <input v-if="editImage" v-model="item.location" type="text" class="edit" @blur="save">
  </div>
</template>
<script>
import { mapActions } from 'vuex'
export default {
  props: ['preview', 'contenteditable', 'item', 'itemIndex'],
  data() {
    return {
      editImage: false
    }
  },
  computed: {
    getStyle() {
      return 'background-image:url(' + this.item.location + '); height: 100%; background-size: contain; background-repeat: no-repeat; border: 2px solid #000000; border-radius: 5px; background-position: center;'
    }
  },
  methods: {
    ...mapActions([
      'saveItem'
    ]),
    save(e) {
      this.item.location = e.target.value
      this.saveItem({ item: this.item, index: this.itemIndex })
    }
  }
}
</script>

<style scoped>
  .preview {
    position: absolute;
    left: 4px;
    top: 2px;
  }
  .edit {
    padding-left: 20px;
    width: 100%;
  }
</style>
