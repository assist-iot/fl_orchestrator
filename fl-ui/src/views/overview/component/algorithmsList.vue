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
        style="
          margin-left: 10px;
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
      <el-button
        class="trainBtn"
        style="float:right;"
        :disabled="disabledTrainButton"
        @click="showTrainModelDialog"
      >
        <i class="el-icon-delete-solid">
          <span class="font-class">
            {{ $t("overview.TrainModel") }}
          </span>
        </i>
      </el-button>
    </div>
    <el-row style="background:#fff;margin-bottom:30px;">
      <!--
        highlight-current-row
      -->
      <!-- MODELS TABLE -->
      <el-table
        ref="singleRow"
        v-loading="listLoading"
        :data="filteredModelsByPagination"
        border
        fit
        style="width: 100%"
        @current-change="handleSelectionChange"
      >
        <el-table-column width="55">
          <template slot-scope="scope">
            <el-checkbox v-model="scope.row.checked" @change="selectRow" />
          </template>
        </el-table-column>
        <el-table-column
          :label="this.$t('overview.tableColumnModelName')"
          align="center"
        >
          <template slot-scope="{ row }">
            <span>{{ row.model_name }} </span>
            <el-popover
              placement="top"
              width="400"
              trigger="hover"
              title="About Algorithm"
            >
              <p>{{ row.meta.description }}</p>
              <i slot="reference" class="el-icon-info el-icon-right info" />
            </el-popover>
          </template>
        </el-table-column>
        <el-table-column
          :label="this.$t('overview.tableColumnModelVersion')"
          align="center"
        >
          <template slot-scope="{ row }">
            <span>{{ row.model_version }}</span>
          </template>
        </el-table-column>
        <el-table-column
          :label="this.$t('overview.tableColumnActions')"
          align="center"
          class-name="small-padding fixed-width"
        >
          <template slot-scope="{ row }">
            <el-button
              size="small"
              class="viewBtn"
              @click="showModel(row)"
            >
              <i class="el-icon-view">
                <span class="font-class">
                  {{ $t("overview.viewModel") }}
                </span>
              </i>
            </el-button>
            <el-button
              size="small"
              class="editBtn"
              @click="showEditModel(row)"
            >
              <i class="el-icon-edit">
                <span class="font-class">{{
                  $t("overview.editModel")
                }}</span>
              </i>
            </el-button>
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
    <!-- DIALOG TO TRAIN A MODEL -->
    <el-dialog
      :visible.sync="trainModelDialog"
      width="20%"
      :title="titleTrainModelDialog"
    >
      <div>
        <span style="padding: 10px;">
          {{ $t("overview.trainModelDialogQuestion") }}
        </span>
      </div>
      <div slot="footer" class="dialog-footer">
        <el-button type="danger" @click="startTrainModel()">
          {{ $t("common.start") }}
        </el-button>
        <el-button type="success" @click="hideTrainModelDialog()">
          {{ $t("common.close") }}
        </el-button>
      </div>
    </el-dialog>

    <!-- DIALOG TO SHOW MODEL -->
    <el-dialog
      :visible.sync="viewModel"
      width="80%"
      :title="titleViewModel"
    >
      <el-card class="box-card">
        <json-editor ref="jsonMetadata" v-model="model" />
      </el-card>

      <div slot="footer" class="dialog-footer">
        <el-button type="success" @click="closeViewModel()">
          {{ $t("common.close") }}
        </el-button>
      </div>
    </el-dialog>
    <!-- DIALOG FOR EDITING SOME PROPERTIES OF THE MODEL -->
    <el-dialog :visible.sync="editModelDialog" :title="this.$t('overview.editModelDialogTitle')" class="dialog-class">
      <EditModal :row-selected="rowSelected" @close="closeEditModel" @modelConfig="modelConfig" />
    </el-dialog>

    <VShell
      class="shell"
      :banner="shellConfig.banner"
      :commands="shellConfig.commands"
      :shell_input="send_to_terminal"
      :model_name="model_name"
      @shell_output="prompt"
      @sendValue="recieveName()"
    />
  </div>
</template>

<script>
import waves from '@/directive/waves' // waves directive
import Pagination from '@/components/Pagination' // secondary package based on
import JsonEditor from '@/components/JsonEditor'
import { getModelsList, getShowConfiguration, configurationByModel, startTrainingModel, callEnablers, modelShell, downloadModel, loadModelData } from '@/api/FL_API'
import VShell from '../../../../node_modules/vue-shell/src/v-shell.vue'
import assist_logo from '@/assets/dataports_images/assist_logo.png'
import EditModal from './editmodal.vue'
export default {
  name: 'NotificationList',
  components: { JsonEditor, Pagination, VShell, EditModal },
  directives: { waves },
  data() {
    return {
      activeTab: '',
      handlers: {
        click: this.onClick,
        change: this.onChange
      },
      send_to_terminal: '',
      shellConfig: {
        banner: {
          header: this.$t('shell.header'),
          subHeader: this.$t('shell.subHeader'),
          helpHeader: '',
          emoji: {},
          /* sign: 'ASSIST-IoT $', */
          img: {
            align: 'left',
            link: assist_logo,
            width: 50,
            height: 50
          }
        }
      },
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
      label_widthColumn: '190px',
      rowSelected: {},
      disabledTrainButton: true,
      existConfigurationRegister: false,
      titleTrainModelDialog: '',
      intervalId: null,
      total_rounds: 0,
      rounds: 0,
      model_name: '',
      model_version: '',
      training_id: 0,
      intervalID: null,
      epochsText: '',
      errorLog: false,
      defaultConfig: {},
      stop_description: '',
      stop_data: {}
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
        model.model_name.toLowerCase().includes(this.searchText.toLowerCase())
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
  beforeMount() {
    this.loadData()
  },
  mounted() {
    // this.getList()
  },

  created() {
    this.getList()
    this.commonTranslation()
    this.$store.watch(
      (state) => {
        return this.$store.state.socket.message
      },
      (newValue, oldValue) => {
        var arr = newValue.split(',')
        var status = arr[0]
        switch (status) {
          case 'SUCCESS':
            var include = arr[2].includes(':')
            if (arr.length === 4 && !include) {
              var rounds = arr[3]
              this.rounds = rounds
              this.prompt('rounds')
            } else if (arr.length === 4) {
              var epochArr = arr[2].split(':')
              var epochs = parseInt(epochArr[1]) + 1
              var total_epochs = epochArr[2]
              this.epochsText = this.$t('overview.epoch') + ' ' + epochs + '/' + total_epochs
              this.prompt('epochs')
            }

            break
          case 'ERROR':
            this.errorLog = true
            break
          case 'STOP':
            var stop_arr = newValue.split(',ORCHESTRATOR,')
            var data_split = stop_arr[1].split('},')
            this.stop_description = data_split[1]
            var concatenateString = data_split[0] + '}'
            var serialize = JSON.parse(concatenateString)
            this.stop_data = serialize
            if (Object.keys(this.stop_data).length !== 2) {
              this.model_name = this.stop_data['model_name']
            } else {
              this.trainModelDialog = false
              this.modelToTrain = ''
            }
            this.prompt('stop')
            break
        }
      }

    )
  },
  methods: {
    modelConfig(data) { this.defaultConfig = data },
    async recieveName() {
      var name = window.localStorage.getItem('shell_model_name', name)
      if (name) {
        //name = name.replace(/ /g, '')
        const data = await modelShell(name, this.model_version, this.rowSelected['configuration_id'].toString())
        console.log('data', data)
        if (data.message.length === 1) {
          var newFilename = data.message[0].filename.split('/')
          var model_name = newFilename[1]
          var model_version = newFilename[2]
          var dataObj = {
            'model_name': model_name,
            'model_version': model_version,
            'training_id': data.message[0].training_id
          }
          await downloadModel(dataObj).then(response => {
            this.b64toBlob(response.message).then(blob => this.saveFile(blob, 'model.pkl'))
          })
        }
      }
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
    commonTranslation() {
      this.requiredText = ' ' + this.$t('common.required')
    },
    prompt(type) {
      switch (type) {
        case 'rounds':
          this.send_to_terminal = '--> ' + this.$t('overview.round') + ' ' + this.rounds + '/' + this.total_rounds + this.$t('overview.successfully')
          if (this.rounds === this.total_rounds) {
            this.send_to_terminal = '--> ' + this.$t('overview.round') + ' ' + this.rounds + '/' + this.total_rounds + this.$t('overview.successfully') + '<br/></br>--> ' + this.$t('overview.finished') + ', ' + this.$t('overview.findModel') + ' '+ this.model_name +' '+ this.$t('overview.modelText') + ' <a style="color:yellow">' + this.$t('overview.hereDownload') + '</a>'
          }
          break
        case 'epochs':
          this.send_to_terminal = '--> ' + this.epochsText
          break
        case 'start':
          this.send_to_terminal = '--> ' + this.$t('overview.trainStart')
          break
        case 'error':
          this.send_to_terminal = '--> ' + this.$t('overview.errorTrain')
          break
        case 'stop':
          if (Object.keys(this.stop_data).length === 2) {
            this.send_to_terminal = '--> ' + this.$t('overview.stopEnoughLo')
          } else {
            this.send_to_terminal = '--> ' + this.$t('overview.finished') + '.' + this.$t('overview.stopMetricTarget') + '<br/></br>--> ' + this.$t('overview.finished') + ', ' + this.$t('overview.findModel') + ' ' + this.model_name + ' ' + this.$t('overview.modelText') + ' <a style="color:yellow">' + this.$t('overview.hereDownload') + '</a>'
          }
          break
      }
    },
    loadData() {
      loadModelData().then(response => {})
    },
    getList() {
      const page = this.listQuery.page
      const limit = this.listQuery.limit
      const startIndex = (page - 1) * limit
      this.listLoading = true
      getModelsList().then(response => {
        response.message.forEach(item => {
          item.checked = false
        })
        var data = response.message
        this.list = data.slice(startIndex,(startIndex + limit))
        this.total = data.length
        setTimeout(() => {
          this.listLoading = false
        }, 1.5 * 1000)
      })
    },

    handleFilter() {},

    showTrainModelDialog() {
      this.titleTrainModelDialog = this.$t('overview.trainModelDialogTitle') + this.rowSelected.model_name
      this.trainModelDialog = true
      this.modelToTrain = this.modelProperties
    },

    startTrainModel() {
      var model = this.modelToTrain
      if ('__ob__' in model && '__ob__' in this.defaultConfig) {
        this.total_rounds = model.number_of_rounds
        this.errorLog = false
      } else if ('__ob__' in model) {
        model = this.defaultConfig
        this.total_rounds = model.number_of_rounds
        this.errorLog = false
      }
      this.model_version = model.model_version
      this.training_id = model.training_id
      if (this.errorLog === false) {
        this.prompt('start')
      } else {
        this.prompt('error')
      }
      this.rowSelected['configuration_id'] = model['configuration_id']
      startTrainingModel(model).then(response => {
        if (response.message.close) {
          this.hideTrainModelDialog()
          this.$notify({
            title: this.$t('common.success'),
            message: this.$t('overview.FLTrainingstarted'),
            type: 'success',
            duration: 2000
          })
          // Deactivate register selected in the models' table
          this.deactivateTable()
          // Call FL Local Opertions & FL Training Collector to recover its status
          // this.intervalId = setInterval(this.recoverStatus, 10000) // 10 segundos
        }
      })
    },

    hideTrainModelDialog() {
      this.trainModelDialog = false
      this.modelToTrain = ''
    },

    showModel(row) {
      this.titleViewModel = ''
      this.titleViewModel = this.$t('overview.viewModel') + ': ' + row.model_name

      this.model = ''
      // this.model = row
      getShowConfiguration({ 'model_name': this.rowSelected.model_name }).then(response => {
        if (response.message === null) {
          this.model = {}
        } else {
          this.model = response.message
        }
      })
      this.viewModel = true
    },

    closeViewModel() {
      this.viewModel = false
    },

    showEditModel(row) {
      this.rowSelected = row
      this.editModelDialog = true
    },

    existsConfiguration(row) {
      configurationByModel(row.model_name).then(response => {
        if (response.message.data.length === 0) {
          this.disabledTrainButton = true
        } else {
          // this.total_rounds = response.message.data[0].number_of_rounds
          this.model_name = row.model_name
          this.disabledTrainButton = false
        }
      })
    },

    closeEditModel(data) {
      if (typeof data === 'object') {
        this.modelProperties = data.message.data
        this.total_rounds = data.message.data.number_of_rounds
      } else {
        this.modelProperties = {}
      }
      /* this.rowSelected = {} */
      this.editModelDialog = false
    },

    // For managing the selected rows
    handleSelectionChange(row) {
      this.list.forEach(item => {
        if (item.model_name !== row.model_name) {
          item.checked = false
        }
      })
      this.rowSelected = row
      this.existsConfiguration(row)
    },

    selectRow(val) {
      if (val === false) {
        this.disabledTrainButton = true
      } else {
        this.existsConfiguration(this.rowSelected)
      }
    },

    deactivateTable() {
      this.list.forEach(item => {
        item.checked = false
      })
      this.disabledTrainButton = true
    },

    recoverStatus() {
      callEnablers().then(response => {})
    },

    stopInterval() {
      clearInterval(this.intervalId)
    }
  }
}
</script>

<style lang="scss" scoped>
.viewBtn {
  color: #fff;
  background-color: #9da408;
  border-color: #9da408;
}
.editBtn {
  background-color: #e8f4ff;
  border-color: #1890ff;
  color: #1890ff;
}
.trainBtn {
  color: #fff;
  background-color: #409167;
  border-color: #409167;
}
.info{
  font-size: 20px;
  cursor: pointer;
}
.shell{
  padding-top: 20px;
}
.dialog-class{
  height: auto !important;
  margin-top: 6vh !important;
}
</style>
