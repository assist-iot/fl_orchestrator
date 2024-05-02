<template>
  <div class="app-container" :style="bgc">
    <div class="filter-container">
      <el-input
        v-model="searchText"
        placeholder="Search"
        style="width: 200px;"
        class="filter-item"
        @keyup.enter.native="handleFilter"
      />
      <el-button
        v-waves
        class="filter-item"
        style="margin-left: 10px;border-color: #1890ff;color: #1890ff;backgroundColor: rgb(240,242,245);"
        icon="el-icon-search"
        @click="handleFilter"
      >
        <span class="font-class">
          {{ $t("models.search") }}
        </span>
      </el-button>
      <el-button
        v-waves
        class="filter-item"
        style="margin-left: 10px;
          border-color: #1890ff;
          color: #1890ff;
          backgroundcolor: rgb(240, 242, 245);
        "
        icon="el-icon-refresh"
        @click="getList"
      />
      <!--
      <el-button
        class="trainBtn"
        style="float:right;"
        @click="stopInterval"
      >
        <i class="el-icon-delete-solid">
          <span class="font-class">
            Stop interval
          </span>
        </i>
      </el-button>
      -->
    </div>
    <el-row style="background:#fff;margin-bottom:30px;">
      <!--
        highlight-current-row
      -->
      <!-- MODELS TABLE -->
      <el-table
        ref="singleRow"
        v-loading="listLoading"
        :data="list"
        border
        fit
        style="width: 100%"
        @expand-change="handleExpandChange"
      >
        <el-table-column
          width="55"
          type="expand"
        >
          <template slot-scope=" { row } ">
            <div v-for="(item) in list" :key="item.name">
              <tableComponent
                v-if="row.name == item.name"
                :table-list="tableData[item.name]"
                :total="total"
              />
            </div>

          </template>
        </el-table-column>
        <el-table-column
          :label="this.$t('availableModel.tableColumnModelName')"
          align="center"
        >
          <template slot-scope=" props ">
            <span>{{ props.row.name }}</span>
          </template>
        </el-table-column>
        <el-table-column
          :label="this.$t('availableModel.tableColumnModelDescription')"
          align="center"
        >
          <template slot-scope=" props ">
            <span>{{ props.row.description }}</span>
          </template>
        </el-table-column>
      </el-table>
    </el-row>
    <pagination
      v-show="total > 0"
      :total="total"
      :page.sync="listQuery.page"
      :limit.sync="listQuery.limit"
      @pagination="getList"
    />
  </div>
</template>

<script>
import waves from '@/directive/waves' // waves directive
import Pagination from '@/components/Pagination' // secondary package based on
import tableComponent from './tableComponent.vue'
/* import JsonEditor from '@/components/JsonEditor' */

import { getAvailablesModels, downloadModel } from '@/api/FL_API'

export default {
  name: 'NotificationList',
  components: { Pagination, tableComponent },
  directives: { waves },
  data() {
    return {
      tableData: [],
      bgc: {
        backgroundColor: 'rgb(240,242,245)',
        height: '100%',
        width: '100%'
      },
      listQuery: {
        page: 1,
        limit: 10,
        id: undefined
      },
      listLoading: true,
      searchText: '',
      list: [],
      total: 0,
      requiredText: '',
      trainModelDialog: false,
      modelToTrain: '',
      deleteAllNotificationDialog: false,
      viewModel: false,
      model: null,
      titleViewModel: '',
      editModelDialog: false,
      modelProperties: {},
      label_widthColumn: '185px',
      rowSelected: {},
      disabledTrainButton: true,
      existConfigurationRegister: false,
      titleTrainModelDialog: '',
      intervalId: null,
      classificationList: [],
      regressionList: [],
      baseList: [],
      classificationName: 'weights/classification/base2/10',
      regressionName: 'weights/base/base2/732',
      baseName: 'weights/base/base2/10'
    }
  },
  computed: {
    filteredModelsByPagination() {
      const page = this.listQuery.page
      const limit = this.listQuery.limit
      if (Math.ceil(this.filteredModelsBySearchTextLength / limit) >= page) {
        return this.filteredModelsBySearchText.slice(
          (page - 1) * limit,
          page * limit
        )
      } else {
        return this.filteredModelsBySearchText.slice(0, limit)
      }
    },
    filteredModelsBySearchText() {
      // return this.list.filter(img => img.RepoTags[0].toLowerCase().includes(this.searchText.toLowerCase()))
      return this.list.filter(model =>
        model.name.toLowerCase().includes(this.searchText.toLowerCase())
      )
    },

    filteredModelsBySearchTextLength() {
      return this.filteredModelsBySearchText.length
    }
  },
  watch: {
    lang() {
      this.commonTranslation()
    }
  },

  mounted() {
    // this.getList()
  },

  created() {
    this.getList()
    this.commonTranslation()
  },

  methods: {
    commonTranslation() {
      this.requiredText = ' ' + this.$t('common.required')
    },
    handleExpandChange(row, expandedRow) {
      if (expandedRow.length > 0) {
        this.classificationList.push(row)
      }
    },
    async downloadModel(model) {
      await downloadModel(model).then(response => {
        this.b64toBlob(response.message).then(blob => this.saveFile(blob, 'model.pkl'))
      })
    },
    async b64toBlob(base64, type = 'application/octet-stream') {
      return await fetch(`data:${type};base64,${base64}`).then(res => res.blob())
    },
    saveFile(blob, filename) {
      if (window.navigator.msSaveOrOpenBlob) {
        window.navigator.msSaveOrOpenBlob(blob, filename)
      } else {
        const a = document.createElement('a')
        document.body.appendChild(a)
        const url = window.URL.createObjectURL(blob)
        a.href = url
        a.download = filename
        a.click()
        setTimeout(() => {
          window.URL.revokeObjectURL(url)
          document.body.removeChild(a)
        }, 0)
      }
    },
    getList() {
      this.listLoading = true
      var array = []
      var object = {}
      const page = this.listQuery.page
      const limit = this.listQuery.limit
      const startIndex = (page - 1) * limit

      getAvailablesModels().then(response => {
        const uniqueName = Array.from(new Set(response.message.map(item => item.filename)))
        uniqueName.forEach(item => {
          object = {
            'name': item,
            'description': 'Here is the description of the model'
          }
          array.push(object)
        })
        this.total = array.length
        this.list = array.slice(startIndex,(startIndex + limit))
        
        var data_arr = []
        this.tableData.push(response.message)
        uniqueName.forEach(function(name, index) {
          data_arr[name] = []
          response.message.forEach(function(item, index) {
            if (name === item.filename) {
              data_arr[name].push(item)
            }
          })
        })
        this.tableData = data_arr
        setTimeout(() => {
          this.listLoading = false
        }, 1.5 * 1000)
      })
    },

    handleFilter() {},

    stopInterval() {
      clearInterval(this.intervalId)
    }
  }
}
</script>

<style lang="scss" scoped>
</style>
