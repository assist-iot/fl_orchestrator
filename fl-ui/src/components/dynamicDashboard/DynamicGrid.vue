<script>
import VueGridLayout from 'vue-grid-layout'

export default {
  name: 'DynamicGrid',
  components: {
    'vue-grid-layout': VueGridLayout.GridLayout,
    'vue-grid-item': VueGridLayout.GridItem
  },
  props: {
    autoResize: {
      type: Boolean,
      default: true
    },
    editing: {
      type: Boolean,
      default: false
    },
    margin: {
      type: Array,
      default: () => [10, 10]
    },
    numCols: {
      type: Number,
      default: 24
    },
    responsive: {
      type: Boolean,
      default: true
    },
    rowHeight: {
      type: Number,
      default: 15
    },
    size: {
      type: String,
      default: 'md'
    }
  },
  data() {
    return {
      currentSize: this.size,
      gridItems: [],
      isReady: false,
      itemKey: 1,
      items: [],
      layouts: {
        xs: [],
        sm: [],
        md: [],
        lg: [],
        xl: []
      },
      selectedItem: null
    }
  },
  computed: {
    layout: {
      get() { return this.responsive ? this.layouts[this.currentSize] : this.layouts.md },
      set(value) {
        if (this.responsive) {
          this.layouts[this.currentSize] = value
        } else {
          this.layout.md = value
        }
      }
    }
  },
  watch: {
    editing(to) {
      if (!to) {
        // Reset selected item once the edit mode is turned off
        this.selectElement(null)
      }
    }
  },
  methods: {
    removeElement(item) {
      if (item === this.selectedItem) {
        this.selectElement(null)
      }
      this.gridItems.splice(item.i, 1)
      this.items.splice(item.i, 1)
      breakpoints.forEach(function(size) {
        this.layouts[size].splice(item.i, 1)
        this.layouts[size].forEach(function(layout, i) {
          if (layout.i > item.i) {
            layout.i--
          }
        })
      }, this)
      this.$emit('itemRemoved', item)
    },
    selectElement(item) {
      if (item === this.selectedItem) {
        // Don't invoke too many events...
        return
      }
      if (this.editing || item == null) {
        this.selectedItem = item
        this.$emit('itemSelected', item)
      }
      if (item == null) {
        // Hide the placeholder in case a drag event is still going
        this.$children[0].placeholder.i = -1
        const focusedItem = this.$el.querySelector(':focus')
        if (focusedItem != null) {
          focusedItem.blur()
        }
      }
    }
  },
  render(createElement) {
    // FIXME See note in addElement()
    if (!this.isReady) {
      this.$nextTick(function() {
        this.isReady = true
      })
    }
    // Render everything
    const gridLayout = createElement('vue-grid-layout',
      {
        props: {
          layout: this.layout,
          colNum: this.numCols,
          rowHeight: this.rowHeight,
          isDraggable: this.editing,
          isResizable: this.editing,
          verticalCompact: true,
          margin: this.margin,
          useCssTransforms: false
        }
      },
      this.gridItems.map(function(gridItem, index) {
        // Render replacement for virtual grid item component
        const item = this.items[index]; const layout = this.layout[index]
        const rowHeight = this.rowHeight; const numCols = this.numCols; const margin = this.margin
        const el = createElement('vue-grid-item',
          {
            attrs: this.editing ? { tabIndex: (index + 1) } : {},
            key: this.items[index].key,
            on: {
              requestHeight(height) {
                layout.minH = layout.maxH = (height <= rowHeight) ? 1 : Math.ceil((margin[1] + height) / (rowHeight + margin[1]))
                if (layout.h != layout.minH) {
                  layout.h = layout.minH
                  gridLayout.componentInstance.layoutUpdate()
                }
              },
              requestWidth(width) {
                const colWidth = gridLayout.componentInstance.width / numCols
                layout.minW = layout.maxW = (width <= colWidth) ? 1 : Math.ceil((margin[0] + width) / (colWidth + margin[0]))
                if (layout.w !== layout.minH) {
                  layout.w = layout.minW
                  gridLayout.componentInstance.layoutUpdate()
                }
              }
            },
            nativeOn: {
              blur(e) { el.context.selectElement(null) },
              focus(e) { el.context.selectElement(el.componentInstance) }
            },
            props: layout,
            style: (layout.w + layout.h === 0) ? { display: 'none' } : {}
          },
          [
            createElement('span',
              {
                class: { 'close-icon': true },
                on: {
                  click(e) { el.context.removeElement(el.componentInstance) }
                },
                style: (!this.editing) ? { display: 'none' } : {}
              },
              ['x']
            ),
            gridItem.componentOptions.children
          ])
        // Load saved data on next tick
        if (!item.settingsLoaded) {
          this.$nextTick(function() {
            const instance = gridItem.componentOptions.children[0].componentInstance
            if (!item.settingsLoaded && instance !== undefined) {
              const loadFn = instance.load
              if (loadFn !== undefined) {
                loadFn(item.settings)
              }
              item.settingsLoaded = true
              el.context.$emit('itemAdded', instance.$parent)
            }
          })
        }
        return el
      }, this)
    )
    return gridLayout
  }
}
</script>

<style lang="scss" scoped>
.vue-grid-item > * {
	height: 100%;
	width: 100%;
}
.vue-grid-item:focus {
	background-color: red;
}
.vue-grid-item:focus > * {
	opacity: 0.8;
}
.vue-grid-item.vue-resizable > * {
	pointer-events: none;
}
.vue-grid-item > .close-icon {
	top: 3px;
	box-sizing: border-box;
	cursor: pointer;
	height: 12px;
	padding: 0 3px 3px 0;
	pointer-events: all;
	position: absolute;
	right: 0;
	width: 12px;
	z-index: 1;
}
.vue-grid-item.vue-resizable > span.vue-resizable-handle {
	pointer-events: all;
	z-index: 1;
}
</style>
