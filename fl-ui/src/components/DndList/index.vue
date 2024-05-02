<template>
  <div class="dndList">
    <div :style="{width:width1}" class="dndList-list">
      <h3>{{ UsedListTitle }}</h3>
      <draggable :set-data="setData" :list="usedFields" group="article" class="dragArea">
        <div v-for="element in usedFields" :key="element.id" class="list-complete-item">
          <div class="list-complete-item-handle">
            {{ element.id }}
            <!--[{{ element.author }}] {{ element.title }}-->
          </div>
          <div style="position:absolute;right:0px;">
            <span style="float: right ;margin-top: -20px;margin-right:5px;" @click="deleteEle(element)">
              <i style="color:#ff4949" class="el-icon-delete" />
            </span>
          </div>
        </div>
      </draggable>
    </div>
    <div :style="{width:width2}" class="dndList-list">
      <h3>{{ AvailableListTitle }}</h3>
      <draggable :list="availableFields" group="article" class="dragArea">
        <div v-for="element in availableFields" :key="element.id" class="list-complete-item">
          <div class="list-complete-item-handle2" @click="pushEle(element)">
            {{ element.id }}
            <!--[{{ element.author }}] {{ element.title }}-->
          </div>
        </div>
      </draggable>
    </div>
  </div>
</template>

<script>
import draggable from 'vuedraggable'
export default {
  name: 'DndList',
  components: { draggable },
  props: {
    usedFields: {
      type: Array,
      default() {
        return []
      }
    },
    availableFields: {
      type: Array,
      default() {
        return []
      }
    },
    usedListTitle: {
      type: String,
      default: 'Used Items'
    },
    availableListTitle: {
      type: String,
      default: 'Available Items'
    },
    width1: {
      type: String,
      default: '48%'
    },
    width2: {
      type: String,
      default: '48%'
    }
  },
  methods: {
    isNotInUsed(v) {
      return this.usedFields.every(k => v.id !== k.id)
    },
    isNotInAvailable(v) {
      return this.availableFields.every(k => v.id !== k.id)
    },
    deleteEle(ele) {
      for (const item of this.usedFields) {
        if (item.id === ele.id) {
          const index = this.usedFields.indexOf(item)
          this.usedFields.splice(index, 1)
          break
        }
      }
      if (this.isNotInAvailable(ele)) {
        this.availableFields.unshift(ele)
      }
    },
    pushEle(ele) {
      for (const item of this.availableFields) {
        if (item.id === ele.id) {
          const index = this.availableFields.indexOf(item)
          this.availableFields.splice(index, 1)
          break
        }
      }
      if (this.isNotInUsed(ele)) {
        this.usedFields.push(ele)
      }
    },
    setData(dataTransfer) {
      // to avoid Firefox bug
      // Detail see : https://github.com/RubaXa/Sortable/issues/1012
      dataTransfer.setData('Text', '')
    }
  }
}
</script>

<style lang="scss" scoped>
.dndList {
  background: #fff;
  padding-bottom: 40px;
  &:after {
    content: "";
    display: table;
    clear: both;
  }
  .dndList-list {
    float: left;
    padding-bottom: 30px;
    &:first-of-type {
      margin-right: 2%;
    }
    .dragArea {
      margin-top: 15px;
      min-height: 50px;
      padding-bottom: 30px;
    }
  }
}
.list-complete-item {
  cursor: pointer;
  position: relative;
  font-size: 14px;
  padding: 5px 12px;
  margin-top: 4px;
  border: 1px solid #bfcbd9;
  transition: all 1s;
}
.list-complete-item-handle {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  margin-right: 50px;
}
.list-complete-item-handle2 {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  margin-right: 20px;
}
.list-complete-item.sortable-chosen {
  background: #4AB7BD;
}
.list-complete-item.sortable-ghost {
  background: #30B08F;
}
.list-complete-enter,
.list-complete-leave-active {
  opacity: 0;
}
</style>
